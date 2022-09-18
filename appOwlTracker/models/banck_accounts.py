from importlib.metadata import requires
from typing_extensions import Required
from django.db import models

class banck_accounts(models.Model):
    
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey()
    id_banck_account = models.IntegerField()
    name_account = models.CharField( max_length=45)
    
        