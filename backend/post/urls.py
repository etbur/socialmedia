from django.urls import path
from .views import index
urlpatterns=[
  path('get/',index.as_view()),
]