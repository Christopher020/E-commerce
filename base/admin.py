from django.contrib import admin

# Register your models here.
from .models import Product, Topic

admin.site.register(Product)
admin.site.register(Topic)