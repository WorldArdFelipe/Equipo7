from dataclasses import fields
from rest_framework import serializers
from appOwlTracker.models.data_log import data_log
from appOwlTracker.models. user import User


class account_Serializer(serializers.ModelSerializer):
    class Meta:
        model = data_log
        fields = ["id_user", "name_item", "type_movimiento","value_amount", "id_categories", "data_time", "id_bank_account"]
    
    def create(self,validated_data):
        data_logInstance =  data_log.objects.create(**validated_data)
        return data_logInstance
        
    def to_representation(self,obj):
        data_log = data_log.objects.get(id = obj.id)
        
        return {
            'data_log':{
                'id':data_log.id,
                'id_user' : data_log.id_user,
                ' name_item' : data_log.name_item,
                'type_movimiento' : data_log.type_movimiento,
                'value_amount' : data_log.value_amount,
                'id_categories' : data_log.id_categories,
                'data_time' : data_log.data_time,
                'id_bank_account' : data_log.id_bank_account,
            }
     }
        
