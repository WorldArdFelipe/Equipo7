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
        return

    def put(self,request,*args, **kwargs):
        return
    
    def delete(self,request,*args, **kwargs):
        return
    