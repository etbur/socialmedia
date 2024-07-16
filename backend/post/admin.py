from django.contrib import admin
from .models import Post,Tag,Like,Comment,Notification,Follow

# Register your models here.
admin.register(Post)
admin.register(Tag)
admin.register(Like)
admin.register(Comment)
admin.register(Notification)
admin.register(Follow)
