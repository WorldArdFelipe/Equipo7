from importlib.metadata import requires
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self,username,password=None):
        if not username:
            raise ValueError("User must have an username")
        user = self.model(username = username)
        user.set_password(password)
        user.save(using = self._db)
        return user
    

class User(AbstractBaseUser,PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)    
    is_staff   = models.BooleanField(default=False)
    admin   = models.BooleanField(default=False)
    
    def save(self, **kwargs):
        some_alt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password,some_alt)
        super().save(**kwargs)
    
    objects =  UserManager()
    USERNAME_FIELD = 'username'
    
    
    
    