from django.urls import path
from .consumers import NotificationConsumer,PostConsumer,PostFetchConsumer

websocket_urlpatterns = [
    path('ws/notifications/', NotificationConsumer.as_asgi()),
    path('ws/posts/', PostConsumer.as_asgi()),
    path('ws/posts/fetch', PostFetchConsumer.as_asgi()),
]