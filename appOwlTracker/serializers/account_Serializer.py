from dataclasses import fields
from rest_framework import serializers
from appOwlTracker.models.account import account
from appOwlTracker.models.user import User

class account_Serializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = ["id", "username","email","password"," id_bank_account"]
    
    def create(self,validated_data):
        accountInstance =  account.objects.create(**validated_data)
        return accountInstance
        
    def to_representation(self,obj):
        account = account.objects.get(id = obj.id)
        
        return {
            'account':{
                'username' : account.username,
                'email' :  account.email,
                'id_bank_account' : account.id_bank_account,
                'password' : account.password, 
            }
     }
        
        
  