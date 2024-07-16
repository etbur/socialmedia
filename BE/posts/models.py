from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=100, blank=True)
    audience = models.CharField(max_length=20, default='public')
    # Add fields for multimedia content (images, videos) if needed
