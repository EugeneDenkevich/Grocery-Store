from django.contrib import admin

from .models import User, Delivery, Product

admin.site.register(User)
admin.site.register(Delivery)
admin.site.register(Product)