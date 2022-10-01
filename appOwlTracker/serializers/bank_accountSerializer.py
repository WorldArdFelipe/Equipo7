from dataclasses import fields
from rest_framework import serializers
from appOwlTracker.models.bank_accounts import Bank_Accounts
from appOwlTracker.models.user import User


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank_Accounts
        fields = ["id_user","id_bank_account","name_account"]
    
    def create(self,validated_data):
        banksAccountInstance =  Bank_Accounts.objects.create(**validated_data)
        return banksAccountInstance
        
    def to_representation(self,obj):
        banks = Bank_Accounts.objects.get(id = obj.id)
        
        return {
            'banks_account':{
                'id_bank_account' : banks.id_bank_account,
                'name_account' :  banks.name_account,
            }
     }
