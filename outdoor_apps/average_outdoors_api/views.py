from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts  import get_object_or_404
from .models import page
from .serializers import PageSerializer
# Create your views here.
class ConservationArea(APIView):
    def get(self,request,*args,**kwargs):
        return Response(data={'ok':'ok'}, status=status.HTTP_200_OK)

class ActivityPages(APIView):
    def get(self,request,*args,**kwargs):
        #need to review how indexing works for fkey fields when we arnt using the pk
        page_obj = get_object_or_404(page, state_reltn__state_name = request.query_params['state'].lower(),activity_reltn__activity_name = request.query_params['activity'].lower())
        serializer = PageSerializer(page_obj)
        return Response(data={'obj':serializer.data}, status=status.HTTP_200_OK)