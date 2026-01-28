from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    ROLE_CHOICES =(
           ('seller', 'seller'),
           ('buyer', 'buyer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = PhoneNumberField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Country(models.Model):
    country_name = models.CharField(max_length=64)

    def __str__(self):
        return self.country_name


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE,related_name='regions')
    region_name = models.CharField(max_length=64)


    def __str__(self):
        return self.region_name


class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities')
    city_name = models.CharField(max_length=64)
    city_image = models.ImageField(upload_to='city_image/', null=True, blank=True)

    def __str__(self):
        return self.city_name


class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='districts')
    district_name = models.CharField(max_length=64)

    def __str__(self):
        return self.district_name


class Property(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    PROPERTY_TYPE = (
         ('apartment', 'apartment'),
         ('house', 'house'),
         ('room', 'room'),
         ('plot', 'plot'),
         ('dacha', 'dacha'),
         ('parking/garage', 'parking/garage     ')
    )
    property_type = models.CharField(max_length=30, choices=PROPERTY_TYPE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='properties')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='properties')
    district = models.ForeignKey(District,on_delete=models.CASCADE, related_name='properties')
    address = models.CharField(max_length=150)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()
    total_floors = models.PositiveSmallIntegerField()
    CONDITION_TYPE = (
        ('self-finishing', 'self-finishing'),
        ('euro renovation', 'euro renovation'),
        ('good', 'good'),
        ('average', 'average'),
        ('not completed', 'not completed'),
    )
    condition = models.CharField(max_length=35, choices=CONDITION_TYPE)
    documents = models.BooleanField(default=True)
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='properties')

    def __str__(self):
        return self.title


class PropertyImages(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    property_image= models.ImageField(upload_to='property_image/', null=True, blank=True)


class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='author')
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='seller')
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i))for i in range(1,6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.rating



