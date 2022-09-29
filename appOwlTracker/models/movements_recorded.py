from importlib.metadata import requires
from django.db import models
from .user import User
from .bank_accounts import Bank_Accounts

class Movements_Recorded(models.Model):
    
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User,related_name="id_user",on_delete=models.CASCADE)
    name_item = models.CharField(max_length=40)
    type_movimiento = models.SmallIntegerField()
    value_amount = models.BigIntegerField("13")
    id_categories = models.IntegerField()
    data_time = models.DateTimeField()
    id_bank_account = models.ForeignKey(Bank_Accounts,related_name="id_bank_account_movements",on_delete=models.CASCADE)
    
    
    
    