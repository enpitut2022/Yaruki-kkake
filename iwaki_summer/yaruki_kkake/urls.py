from django.urls import path
from .views import index, start, doing

urlpatterns = [
  path("", index, name='index'),
  path("start", start, name='start'),
  path("doing", doing, name='doing'),
]