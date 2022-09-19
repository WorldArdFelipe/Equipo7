from importlib.metadata import requires
from typing_extensions import Required
from django.db import models

class data_log(models.Model):
    
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey()
    name_item = models.CharField(max_length=40)
    type_movimiento = models.SmallIntegerField()
    value_amount = models.BigIntegerField("13")
    id_categories = models.IntegerField()
    data_time = models.DateTimeField()
    id_bank_account = models.ForeignKey()
    
    
    
    