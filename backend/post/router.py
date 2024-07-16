from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TagViewSet, LikeViewSet, CommentViewSet, PostViewSet, NotificationViewSet, FollowViewSet

router = DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'posts', PostViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'follows', FollowViewSet)
