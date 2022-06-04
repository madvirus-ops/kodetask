from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return self.name
class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    def __str__(self):
        return self.street

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(People, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    def __str__(self):
        return self.name

class Bio(models.Model):
    user = models.OneToOneField(People, on_delete=models.CASCADE)
    bio = models.TextField()
    def __str__(self):
        return self.bio

        