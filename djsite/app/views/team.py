
from app import models
from app.serializers import TeamSerializer
from rest_framework import viewsets

class TeamViewSet(viewsets.ModelViewSet):
    """ 用户API """
    queryset = models.Team.objects.all()
    serializer_class = TeamSerializer