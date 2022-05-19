from secrets import choice
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MembershipModels(models.Model):
   
    CHOICES = (
        ('basic', 'basic'),
        ('premium', 'premium'),
        ('enterprice', 'enterprice'),
        ('custom', 'custom'),
    )

    membership = models.CharField(choices=CHOICES, default='basic', max_length=16)    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
       return self.membership

