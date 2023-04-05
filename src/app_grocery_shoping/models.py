from pickle import FALSE
from django.db import models


class User(models.Model):

    fullname = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False, primary_key=True)
    image = models.ImageField(upload_to='uploads')
    day_of_birth = models.DateField(null=True)


    def __str__(self) -> str:
        return f'{self.fullname}'

class Delivery(models.Model):

    METHODS = [('p', 'Pick up in the pick-up point'),
               ('d', 'Deliver to my appartment')]

    country = models.CharField(blank=False, max_length=100)
    city = models.CharField(blank=False, max_length=100)
    address = models.CharField(blank=False, max_length=200)
    phone = models.CharField(blank=False, max_length=100)
    comment = models.TextField(max_length=300)
    method = models.CharField(choices=METHODS, max_length=1, blank=False)

    user = models.ForeignKey('User', on_delete=models.CASCADE)

CATEGORY = [('Fruits', 'Fruits'), ('Vegetables', 'Vegitables'), ('Milk-and-meat', 'Milk and Meat')]

class Cart(models.Model):

    product = models.CharField(blank=False, max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    user = models.ForeignKey('User', on_delete=models.CASCADE)

class Product(models.Model):

    name = models.CharField(blank=False, max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    company = models.CharField(blank=False, max_length=100)
    image = models.ImageField(upload_to='uploads')

    category = models.CharField(choices=CATEGORY, max_length=20, blank=False)