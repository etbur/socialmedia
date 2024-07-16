from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    video = models.FileField(upload_to='posts', null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    audience = models.CharField(max_length=50, choices=[
        ('public', 'Public'),
        ('friends', 'Friends'),
        ('groups', 'Specific Groups')
    ], default='public')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    post_comments = models.ManyToManyField('Comment',related_name='post_comments', blank=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.author.username}'s comment on {self.post.title}"

