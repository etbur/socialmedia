from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tags', views.TagViewSet, basename='tag')
router.register(r'likes', views.LikeViewSet, basename='like')
router.register(r'comments', views.CommentViewSet, basename='comment')
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'follows', views.FollowViewSet, basename='follow')
