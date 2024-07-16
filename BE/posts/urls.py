from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
]
