from django.conf import settings
from appOwlTracker.models.user import User
from rest_framework import status, views, generics
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from appOwlTracker.serializers.userSerializer import UserSerializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

class UserView(generics.ListAPIView):

    #CONSULTAR DEPENDIENDO EL kwargs
    
    
    def get(self,request,*args, **kwargs):
        usuario =  User.objects.get(id = kwargs['id'])
        usuario_serializer = UserSerializer(usuario)
        return Response(usuario_serializer.data,status=status.HTTP_200_OK) 
    
    #CREACION O ENVIAR DATOS
    def post(self,request,*args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        tokenData = {"username":request.data["username"],"password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

    def put(self,request,*args, **kwargs):
        usuario =  User.objects.get(id = kwargs['id'])
        usuario_serializer = UserSerializer(usuario,data=request.data)
        usuario_serializer.is_valid(raise_exception = True)
        usuario_serializer.save()
        
        return Response(UserSerializer(usuario).data, status=status.HTTP_201_CREATED)

    def delete(self,request,*args, **kwargs):
        usuario =  User.objects.filter(id = kwargs['id']).first()
        usuario.delete()
        
        stringResponde =  {'detail':'Registro eliminado correctamente'}
        
        return Response(stringResponde,status=status.HTTP_200_OK)


# Trae todos los usuarios
class AllUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        usuario_serializer = UserSerializer(queryset,many=True)
        return Response(usuario_serializer.data, status=status.HTTP_201_CREATED)    

        
        
        