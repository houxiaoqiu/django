from rest_framework import serializers
from app.views import team

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = team
        fields = "__all__"
    
        
    
        