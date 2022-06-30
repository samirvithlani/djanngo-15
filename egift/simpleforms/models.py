from django.db import models

# Create your models here.
TASK_PRIORITY =[
    ("Low","Low"),
    ("Medium","Medium"),
    ("High","High")
]
class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_time = models.IntegerField()
    task_description = models.TextField()
    task_proiority = models.CharField(choices=TASK_PRIORITY,max_length=200)