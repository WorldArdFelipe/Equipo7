from dataclasses import fields
from shutil import move
from rest_framework import serializers
from appOwlTracker.models.movements_recorded import Movements_Recorded
from appOwlTracker.models.user import User


class MovementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movements_Recorded
        fields = ["id","id_user","name_item","password"]
    
    def create(self,validated_data):
        movementsIntance =  Movements_Recorded.objects.create(**validated_data)
        return movementsIntance
        
    def to_representation(self,obj):
        movements_recorded = Movements_Recorded.objects.get(id=obj.id)
        user = User.objects.get(id = movements_recorded.id_user)
         
        return {        
            'movement':
            {
                'id': movements_recorded.id,
                'id_user': movements_recorded.id_user,
                'name_item': movements_recorded.name_item,
                'type_movimiento': movements_recorded.type_movimiento,
                'value_amount' : movements_recorded.value_amount,
                'id_categories' : movements_recorded.id_categories,
                'data_time' : movements_recorded.data_time,
                'id_bank_account' : movements_recorded.id_bank_account,
            }
        }