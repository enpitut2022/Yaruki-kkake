from django.urls import path
from .views import index, start

urlpatterns = [
  path("", index),
  path("start", start),
]