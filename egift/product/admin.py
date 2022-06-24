from django.contrib import admin

from .models import Country, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Country)