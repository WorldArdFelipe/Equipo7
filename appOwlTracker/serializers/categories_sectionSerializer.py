from dataclasses import fields
from rest_framework import serializers
from appOwlTracker.models.categories_section import Categories_Section
from appOwlTracker.models.user import User



class account_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Categories_Section
        fields = ["id", "username","name_categories"]
    
    def create(self,validated_data):
        categories_sectionInstance =  Categories_Section.objects.create(**validated_data)
        return categories_sectionInstance
        
    def to_representation(self,obj):
        account = Categories_Section.objects.get(id = obj.id)
        
        return {
            'categories_section':{
                'id' : Categories_Section.id,
                'name_categories' : Categories_Section.name_categories,
                
            }
     }
      

