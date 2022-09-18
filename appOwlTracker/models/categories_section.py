from importlib.metadata import requires
from typing_extensions import Required
from django.db import models

class categories_section(models.Model):
    
    id = models.AutoField(primary_key=True)
    name_categories = models.CharField(max_length=45)
    data_log = models.ForeignKey()
    