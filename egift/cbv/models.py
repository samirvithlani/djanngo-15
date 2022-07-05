from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publishDate = models.DateField()
    
    class Meta:
        db_table = 'news'


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_venue = models.CharField(max_length=100)
    event_pic = models.ImageField(upload_to = "event_pic")
        
    class Meta:
        db_table = "event"
    
    @property
    def imageURL(self):
        try:
            url = self.event_pic.url
        except:
            url = ''
        return url    