from django.urls import path
from .consumers import NotificationConsumer,PostConsumer,PostFetchConsumer  ,LikeConsumer,FollowConsumer,CommentConsumer

websocket_urlpatterns = [
    path('ws/posts/', PostConsumer.as_asgi()),
    path('ws/posts/like/', LikeConsumer.as_asgi()),
    path('ws/posts/comment/',CommentConsumer.as_asgi()),
    path('ws/posts/follow/', FollowConsumer.as_asgi()),
    path('ws/notifications/', NotificationConsumer.as_asgi()),
    
    
]