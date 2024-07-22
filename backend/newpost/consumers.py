import base64
import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Post,Tag,Like,Comment,Follow ,Notification
from .serializers import PostSerializer,NotificationSerializer
from django.core.exceptions import SynchronousOnlyOperation
from django.core.files.storage import default_storage
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from asgiref.sync import sync_to_async
from .utils import mark_notification_read, follow_user, unfollow_user
class PostConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'posts'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')

        try:
            if action == 'create':
                post_data = data.get('post')
                post = await self.create_post(post_data)
                await self.channel_layer.group_send(
                    self.group_name,
                    {
                        'type': 'post_created',
                        'post': PostSerializer(post).data
                    }
                )
            else:
                await self.send(text_data=json.dumps({'error': 'Invalid action'}))
        except SynchronousOnlyOperation as e:
            await self.send(text_data=json.dumps({
                'error': f'An error occurred while processing the request: {str(e)}'
            }))

    @database_sync_to_async
    def create_post(self, post_data):
        tags = post_data.pop('tags', [])
        post = Post.objects.create(**post_data)

        tag_objects = []
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            tag_objects.append(tag)

        post.tags.set(tag_objects)
        post.save()

        return post

   
class PostFetchConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'post_fetch'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')

        if action == 'fetch':
            filters = data.get('filters', {})
            posts = await self.fetch_posts(filters)
            serializer = PostSerializer(posts, many=True)
            response = {
                'action': 'fetch_response',
                'posts': serializer.data
            }
            await self.send(text_data=json.dumps(response))
        else:
            await self.send(text_data=json.dumps({'error': 'Invalid action'}))

    @database_sync_to_async
    def fetch_posts(self, filters):
        posts = Post.objects.all()
        if filters.get('category'):
            posts = posts.filter(category=filters['category'])
        if filters.get('tag'):
            posts = posts.filter(tags__name__in=[filters['tag']])
        return posts

class LikeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        post_id = text_data_json['post_id']

        if action == 'create':
            await self.create_like(post_id)
        elif action == 'delete':
            await self.delete_like(post_id)

    @sync_to_async
    def create_like(self, post_id):
        like, created = Like.objects.get_or_create(user=self.user, post_id=post_id)
        if created:
            # Notify the post owner about the new like
            post = like.post
            Notification.objects.create(
                user=post.user,
                post=post,
                like=like,
                message=f"{self.user.username} liked your post."
            )

    @sync_to_async
    def delete_like(self, post_id):
        like = Like.objects.filter(user=self.user, post_id=post_id).first()
        if like:
            like.delete()
            # Notify the post owner about the unlike
            post = like.post
            Notification.objects.create(
                user=post.user,
                post=post,
                like=like,
                message=f"{self.user.username} unliked your post."
            )

class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        post_id = text_data_json['post_id']
        content = text_data_json['content']

        if action == 'create':
            await self.create_comment(post_id, content)

    @sync_to_async
    def create_comment(self, post_id, content):
        comment = Comment.objects.create(user=self.user, post_id=post_id, content=content)
        # Notify the post owner about the new comment
        post = comment.post
        Notification.objects.create(
            user=post.user,
            post=post,
            comment=comment,
            message=f"{self.user.username} commented on your post."
        )


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        notification_id = text_data_json['notification_id']

        if action == 'mark_read':
            await self.mark_notification_read(notification_id)

    async def mark_notification_read(self, notification_id):
        await mark_notification_read(self.user, notification_id)

class FollowConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        followed_user_id = text_data_json['followed_user_id']

        if action == 'follow':
            await self.follow_user(followed_user_id)
        elif action == 'unfollow':
            await self.unfollow_user(followed_user_id)

    async def follow_user(self, followed_user_id):
        await follow_user(self.user, followed_user_id)

    async def unfollow_user(self, followed_user_id):
        await unfollow_user(self.user, followed_user_id)