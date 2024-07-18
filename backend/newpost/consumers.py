
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async
# from .models import Post
# from .serializers import PostSerializer, NotificationSerializer
# from channels.layers import get_channel_layer


# class PostConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.group_name = 'posts'
#         await self.channel_layer.group_add(
#             self.group_name,
#             self.channel_name
#         )
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.group_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         action = data.get('action')

#         if action == 'create':
#             post_data = data.get('post')
#             post = await self.create_post(post_data)
#             await self.channel_layer.group_send(
#                 self.group_name,
#                 {
#                     'type': 'post_created',
#                     'post': PostSerializer(post).data
#                 }
#             )
#         elif action == 'fetch':
#             posts = await self.fetch_posts()
#             await self.send(text_data=json.dumps({
#                 'action': 'fetch_response',
#                 'posts': PostSerializer(posts, many=True).data
#             }))
#         else:
#             await self.send(text_data=json.dumps({
#                 'error': 'Invalid action'
#             }))

#     @database_sync_to_async
#     def create_post(self, post_data):
#         tags = post_data.pop('tags', [])
#         post = Post.objects.create(**post_data)
#         post.tags.add(*tags)
#         return post

#     @database_sync_to_async
#     def fetch_posts(self):
#         return Post.objects.all()

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Post
from .serializers import PostSerializer, NotificationSerializer
# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Post
from .serializers import PostSerializer
from django.core.exceptions import SynchronousOnlyOperation

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
            elif action == 'fetch':
                posts = await self.fetch_posts()
                serializer = PostSerializer(posts, many=True)
                response = {
                    'action': 'fetch_response',
                    'posts': serializer.data
                }
                await self.send(text_data=json.dumps(response))
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
        post.tags.add(*tags)
        return post

    @database_sync_to_async
    def fetch_posts(self):
        return list(Post.objects.all().order_by('-created_at'))


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.group_name = f'user_{self.user.id}'

        # Join the group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def new_notification(self, event):
        notification = event['notification']

        # Send the notification to the WebSocket
        await self.send(text_data=json.dumps({
            'type': 'new_notification',
            'notification': NotificationSerializer(notification).data
        }))