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

class Course(models.Model):
    course_name = models.CharField(max_length=25)
    course_duration = models.CharField(max_length=25)
    course_fee = models.FloatField()
    class Meta:
        db_table = "course"
    
    def __str__(self):
        pass     
        
        
        
class Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    sname = models.CharField(max_length=25)
    semail = models.CharField(max_length=25)
    sage = models.IntegerField()
    
    class Meta:
        db_table = "student"

    def __str__(self):
        return self.sname      


class Demo(models.Model):
     username = models.CharField(max_length = 99, unique = True)
     profile_pic = models.ImageField(upload_to = "profile_pic", default="profile_pic/p1.jpg")
     
     
     
     @property
     def imageURL(self):
        try:
            url = self.profile_pic.url
        except:
            url = ''
        return url


class Category(models.Model):
    cat_name = models.CharField(max_length=25)
    
    class Meta:
        db_table = "category"
        
    def __str__(self):
        return self.cat_name    
        


class Brand(models.Model):
    brand_name = models.CharField(max_length=25)    
        
    class Meta:
        db_table = 'brand'
        
    def __str__(self):
        return self.brand_name


class Gifts(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    gift_name = models.CharField(max_length=25)
    gift_price = models.FloatField()
    gift_qty = models.IntegerField()
    gift_availability = models.BooleanField(null=True)
    
    class Meta:
        db_table = "gifts"
       
    def __str__(self):
        return self.gift_name        