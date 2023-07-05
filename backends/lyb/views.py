from django.shortcuts import render
from rest_framework import viewsets
from .models import Lyb
from .serializers import LybSerializer

# Create your views here.
class LybViewSet(viewsets.ModelViewSet):
    queryset = Lyb.objects.all().order_by('-posttime')
    serializer_class = LybSerializer