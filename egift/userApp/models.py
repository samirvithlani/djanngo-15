from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length = 99, unique = True)
    #password = models.CharField(max_length=255, blank=False)
    email = models.EmailField(_('email address') ,max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_deleted = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        db_table = "User"
    
        
        
    
