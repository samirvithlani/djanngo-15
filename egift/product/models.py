from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=25)
    product_price = models.FloatField()
    product_qty = models.IntegerField()
    product_desc = models.TextField()
    product_creation_date = models.DateTimeField()
    product_availablity = models.BooleanField(null=True)

    #product_Product
    class Meta:
        db_table = "product"

class Country(models.Model):
    country_name = models.CharField(max_length=25)
    country_code = models.IntegerField()
    country_cap = models.CharField(max_length=25)

    class Meta:
        db_table = "country"
