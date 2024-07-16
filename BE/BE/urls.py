from django.urls import path, include

urlpatterns = [
    path('api/', include('posts.urls')),
    # Add other URLs as needed
]
