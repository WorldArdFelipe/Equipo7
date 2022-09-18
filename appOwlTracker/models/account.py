from importlib.metadata import requires
from typing_extensions import Required
from django.db import models

class account(models.Model):
    
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=64)
    password = models.IntegerField( max_length=64)
    id_banck_account = models.SmallIntegerField()
    
    
    
    