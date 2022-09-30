from django.conf import settings
from appOwlTracker.models.movements_recorded import Movements_Recorded
from appOwlTracker.serializers.userSerializer import UserSerializer
from rest_framework import status, views, generics
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from appOwlTracker.serializers.movements_recordedSerializer import MovementsSerializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

class MovementsRecordedView(generics.ListAPIView):

    def get(self,request,*args, **kwargs):
        movements = Movements_Recorded.objects.get(id = kwargs['id_user'])
        movements_serializer = MovementsSerializer(movements)
        return Response(movements_serializer.data,status=status.HTTP_200_OK) 

    
    def post(self,request,*args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tockendBackend = TokenBackend(algorithm = settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tockendBackend.decode(token,verify=False)        

        movements_recorded = request.data.pop('movements_recorded')
        movements_recorded["id_user"] = valid_data["id"]
        
        serializer_movements = MovementsSerializer(data = movements_recorded)
        serializer_movements.is_valid(raise_exception=True)
        movements = serializer_movements.save()
        
        return_data = {"movements": MovementsSerializer(movements).data}
        
        return Response(return_data, status=status.HTTP_201_CREATED)
    
    def put(self,request,*args, **kwargs):
        movements =  Movements_Recorded.objects.get(id = kwargs['id'])
        serializer_movements = MovementsSerializer(movements,data=request.data)
        serializer_movements.is_valid(raise_exception = True)
        serializer_movements.save()
        
        return Response(MovementsSerializer(movements).data, status=status.HTTP_201_CREATED)

    def delete(self,request,*args, **kwargs):
        movements =  Movements_Recorded.objects.filter(id = kwargs['id']).first()
        movements.delete()
        
        stringResponde =  {'detail':'Registro eliminado correctamente'}
        
        return Response(stringResponde,status=status.HTTP_200_OK)
    