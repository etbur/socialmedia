
# import json
# from channels.generic.websocket import SyncConsumer
# from channels.db import database_sync_to_async
# from .models import Post
# from .serializers import PostSerializer
# from channels.generic.websocket import AsyncWebsocketConsumer
# from .serializers import NotificationSerializer
# from channels.layers import get_channel_layer
# # your_app/consumers.py

# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async
# from .models import Post
# from .serializers import PostSerializer
# import json

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

# class NotificationConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.user = self.scope['user']
#         self.group_name = f'user_{self.user.id}'

#         # Join the group
#         await self.channel_layer.group_add(
#             self.group_name,
#             self.channel_name
#         )

#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave the group
#         await self.channel_layer.group_discard(
#             self.group_name,
#             self.channel_name
#         )

#     async def new_notification(self, event):
#         notification = event['notification']

#         # Send the notification to the WebSocket
#         await self.send(text_data=json.dumps({
#             'type': 'new_notification',
#             'notification': notification
#         }))
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Post
from .serializers import PostSerializer, NotificationSerializer
from channels.layers import get_channel_layer

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
            await self.send(text_data=json.dumps({
                'error': 'Invalid action'
            }))

    @database_sync_to_async
    def create_post(self, post_data):
        tags = post_data.pop('tags', [])
        post = Post.objects.create(**post_data)
        post.tags.add(*tags)
        return post

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