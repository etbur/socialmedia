from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, permissions
from .serializers import PostSerializer, TagSerializer, LikeSerializer, CommentSerializer, NotificationSerializer, FollowSerializer
from .models import Post, Tag, Like, Comment, Notification, Follow
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your views here.
class index(APIView):
    async def get(self, request):
        return Response('hello!')

# Tag view
class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]

# Like view
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

# Comment view
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

# Post view
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]

 

# Notification view
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    async def perform_create(self, serializer):
        channel_layer = get_channel_layer()
        await async_to_sync(channel_layer.group_send)(
            f'user_{self.request.user.id}',
            {
                'type': 'new_notification',
                'notification': serializer.data
            }
        )
        serializer.save(user=self.request.user)

# Follow view
class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    