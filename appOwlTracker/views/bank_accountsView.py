from turtle import back
from django.conf import settings
from appOwlTracker.models.bank_accounts import Bank_Accounts
from appOwlTracker.serializers.userSerializer import UserSerializer
from rest_framework import status, views, generics
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from appOwlTracker.serializers.bank_accountSerializer import BankAccountSerializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
class BankAccountView(generics.ListAPIView):

    def get(self,request,*args, **kwargs):
        bank = Bank_Accounts.objects.get(id = kwargs['id_user'])
        bank_serializer = BankAccountSerializer(bank)
        return Response(bank_serializer.data,status=status.HTTP_200_OK) 

    def post(self,request,*args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tockendBackend = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tockendBackend.decode(token,verify=False)        

        bank_account = request.data.pop('banks_account')
        bank_account["id_user"] = valid_data["id"]
        
        serializer_bank = BankAccountSerializer(data = bank_account)
        serializer_bank.is_valid(raise_exception=True)
        bank = serializer_bank.save()
        
        return_data = {"bank": BankAccountSerializer(bank).data}
        
        return Response(return_data, status=status.HTTP_201_CREATED)
    
    
    ################################################################
    
    
    def put(self,request,*args, **kwargs):
        
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tockendBackend = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tockendBackend.decode(token,verify=False)  
        
        back_account = back_account.objects.get(id = valid_data['id'])
        back_accountslz = back_accountslz(back_account,data=request.data)
        back_accountslz.is_valid(raise_exception = True)
        back_accountslz.save()
         
        
        return Response(BankAccountSerializer(back_account).data, status=status.HTTP_201_CREATED)
    
    
    def delete(self,request,*args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tockendBackend = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tockendBackend.decode(token,verify=False)  
        Bank_Accounts = Bank_Accounts.objects.filter(id = valid_data['id']).first()
        Bank_Accounts.delete()
        
        stringResponde =  {'detail':'Registro eliminado correctamente'}
        
         
        return Response(stringResponde, status=status.HTTP_200_OK)
    
    
    