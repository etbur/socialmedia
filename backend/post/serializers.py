from rest_framework.serializers import ModelSerializer
from .models import Post,Tag,Comment
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'