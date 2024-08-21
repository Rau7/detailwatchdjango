from rest_framework import serializers
from .models import User, Address, Geo, Company, Album, Photo, Todo, Post, Comment

# simple serializers for each model
# the important or the tricky one is userserializer that includes address and company
# user model got no fields like address and company, but we use address and company serializers-
#- to use it in user serializer

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ['lat', 'lng']

class AddressSerializer(serializers.ModelSerializer):
    geo = GeoSerializer()

    class Meta:
        model = Address
        fields = ['street', 'suite', 'city', 'zipcode', 'geo']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    company = CompanySerializer()

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'address', 'phone', 'website', 'company']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'user', 'title']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'album', 'title', 'url', 'thumbnail_url']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user', 'title', 'completed']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'body']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'name', 'email', 'body']