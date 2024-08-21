from rest_framework import viewsets
from .models import User, Address, Geo, Company, Album, Photo, Todo, Post, Comment
from .serializers import UserSerializer, AlbumSerializer, PhotoSerializer, TodoSerializer, PostSerializer, CommentSerializer

# adding a new user includes address and company objects
# desutructuring address and company objects and adding them to their related fields
# same rules apply for update operations
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # desutructuring address and company from request
        address_data = self.request.data.pop('address')
        company_data = self.request.data.pop('company')

        # get geo object from address object
        geo_data = address_data.pop('geo')
        geo = Geo.objects.create(**geo_data)
        address = Address.objects.create(geo=geo, **address_data)
        company = Company.objects.create(**company_data)

        serializer.save(address=address, company=company)

    def perform_update(self, serializer):
        instance = self.get_object()

        address_data = self.request.data.get('address', {})
        company_data = self.request.data.get('company', {})

        if address_data:
            geo_data = address_data.pop('geo', {})
            geo, _ = Geo.objects.update_or_create(defaults=geo_data, id=instance.address.geo.id)
            address = Address.objects.update_or_create(
                defaults={**address_data, 'geo': geo},
                id=instance.address.id
            )[0]
        else:
            address = instance.address

        if company_data:
            company, _ = Company.objects.update_or_create(defaults=company_data, id=instance.company.id)
        else:
            company = instance.company

        serializer.save(address=address, company=company)

# for all viewsets inherits ModelViewSet's behaviour
# including all CRUD operations
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer