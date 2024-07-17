from django.urls import path
from .consumers import NotificationConsumer,PostConsumer

websocket_urlpatterns = [
    path('ws/notifications/', NotificationConsumer.as_asgi()),
    path('ws/posts/', PostConsumer.as_asgi()),
]