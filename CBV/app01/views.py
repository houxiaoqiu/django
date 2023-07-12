from rest_framework.viewsets import ModelViewSet

from .models import Student,Book,Publish
from .serial import StudentModelSerializer,BookModelSerializer,PublishModelSerializer


# Create your views here.

""" Student """
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

""" Book """
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

""" Publish """
class PublishViewSet(ModelViewSet):
    queryset = Publish.objects.all()
    serializer_class = PublishModelSerializer

