from django.urls import path
from .views import index, start, start2, doing

urlpatterns = [
  path("", index, name='index'),
  path("start", start, name='start'),
  path("start2", start2, name='start2'),
  path("doing", doing, name='doing'),
]