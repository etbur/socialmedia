
import json
from channels.generic.websocket import SyncConsumer
from channels.db import database_sync_to_async
from .models import Post
from .serializers import PostSerializer
from channels.generic.websocket import AsyncWebsocketConsumer
from .serializers import NotificationSerializer
from channels.layers import get_channel_layer
# your_app/consumers.py

class PostConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        self.channel_layer = get_channel_layer()
        self.room_name = 'post'
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def websocket_receive(self, event):
        data = event.get('text', None)
        if data:
            data = json.loads(data)  # Load JSON data
            action = data.get('action', None)
            payload = data.get('post', None)
            if action == 'create' and payload:
                response = await self.create_post(payload)
                if response:
                    await self.send(text_data=json.dumps({'type': 'post.created', 'post': response}))

    @database_sync_to_async
    def create_post(self, payload):
        serializer = PostSerializer(data=payload)  # Directly pass payload
        if serializer.is_valid():
            post = serializer.save()
            return PostSerializer(post).data
        return None  # Handle invalid data

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
            'notification': notification
        }))