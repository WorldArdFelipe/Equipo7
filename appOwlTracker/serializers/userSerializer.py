from dataclasses import fields
from rest_framework import serializers
from appOwlTracker.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","name","email","password"]
    
    def create(self,validated_data):
        userInstance =  User.objects.create(**validated_data)
        return userInstance
        
    def to_representation(self,obj):
        user =  User.objects.get(id = obj.id)
        return {
            'usuario':{
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'email' : user.email
            }
     }