from importlib.metadata import requires
from django.db import models

class Categories_Section(models.Model):
    
    id = models.AutoField(primary_key=True)
    name_categories = models.CharField(max_length=45)
    #data_log = models.ForeignKey()
    
    