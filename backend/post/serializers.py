from rest_framework import serializers
from .models import Post, Tag, Like, Comment,Notification,Follow

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    tags = TagSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), required=False)
    comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False)
    like = serializers.PrimaryKeyRelatedField(queryset=Like.objects.all(), required=False)

    class Meta:
        model = Notification
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.StringRelatedField()
    followed = serializers.StringRelatedField()

    class Meta:
        model = Follow
        fields = '__all__'