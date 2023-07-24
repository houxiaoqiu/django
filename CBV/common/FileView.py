import os
from django.http import FileResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from CBV.settings import MEDIA_ROOT,MEDIA_URL

class ImageView(APIView):
    def get(self,request,name):
        path = MEDIA_ROOT / name
        if os.path.isfile(path):
            return FileResponse(open(path,'rb'))
        return Response({'error': "没有找到该文件！"},status=status.HTTP_404_NOT_FOUND)