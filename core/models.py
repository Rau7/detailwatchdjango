from django.db import models


#for the sake of simplicity and nested objects used in user model
#company, address fields are divided into their own models
#also geo model is created from inside of address field given in sample json

class Geo(models.Model):
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)

    def __str__(self):
        return f"Lat: {self.lat}, Lng: {self.lng}"

#geo model is related to address model (onetoone field)
class Address(models.Model):
    street = models.CharField(max_length=200)
    suite = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    geo = models.OneToOneField(Geo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.street}, {self.city}"


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    website = models.URLField()
    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# album model is related to user model (foreignkey)
class Album(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


# photo model is related to album model (foreignkey) it can be done with onetoone field also
# others are also can be done with onetoone field
class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title
    
# todo model is related to user model (foreignkey)
class Todo(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
# post model is related to user model (foreignkey)
class Post(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
    
# comment model is related to post model (foreignkey)
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name