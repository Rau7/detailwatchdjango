from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import  UserViewSet, PhotoViewSet, AlbumViewSet, TodoViewSet, PostViewSet, CommentViewSet
from rest_framework import routers


router = routers.DefaultRouter();

router.register('users', UserViewSet)

router.register('photos', PhotoViewSet)

router.register('albums', AlbumViewSet)

router.register('todos', TodoViewSet)

router.register('posts', PostViewSet)

router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
