from importlib.metadata import requires
from django.db import models
from .user import User

class Bank_Accounts(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User,related_name="id_user_bank",on_delete=models.CASCADE)
    id_bank_account = models.IntegerField()
    name_account = models.CharField(max_length=46)