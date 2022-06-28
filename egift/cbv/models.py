from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publishDate = models.DateField()
    
    class Meta:
        db_table = 'news'
    
    