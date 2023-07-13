
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from rest_framework.views import APIView
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import CreateModelMixin, ListModelMixin,\
#     RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .models import Student,Book,Publish,Author
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


# """ 序列化 Student """
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    gender = serializers.BooleanField()
    age = serializers.IntegerField()
    class_number = serializers.CharField()

# """ 查询 Student """
class StudentView(APIView):
    # 查询全部记录
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students,many=True)
        return Response(serializer.data)
    # 新增记录
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            stu = Student.objects.create(**serializer.validated_data)
            ser = StudentSerializer(instance=stu, many=False)
            return Response(ser.data)
        except Exception as e:
            return Response(serializer.errors)

# """ 详细 Student """    
class StudentDetailView(APIView):
    # 查询指定记录
    def get(self, request, id):
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(instance=student,many=False)
        return Response(serializer.data)
    # 删除指定记录
    def delete(self, request, id):
        student = Student.objects.get(pk=id).delete()
        return Response()
    # 更新指定记录
    def put(self, request, id):
        serializer = StudentSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            Student.objects.filter(pk=id).update(**serializer.validated_data)
            stu = Student.objects.get(id=id)
            ser = StudentSerializer(instance=stu, many=False)
            return Response(ser.data)
        except Exception as e:
            return Response(serializer.errors)

# """ 序列化 Author """
class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32)
    age = serializers.IntegerField()

    def create(self, validated_data):
        author_obj = Author.objects.create(**validated_data)
        return author_obj
    
    def update(self, instance, validated_data):
        Author.objects.filter(pk=instance.pk).update(**validated_data)
        author_obj = Author.objects.filter(pk=instance.pk).first()
        return author_obj

""" 查询 Author """
class AuthorView(APIView):
    # 查询全部记录
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(instance=authors,many=True)
        return Response(serializer.data)
    # 新增记录
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response(serializer.errors)

""" 详细 Author """
class AuthorDetailView(APIView):
    # 查询全部记录
    def get(self, request, id):
        author = Author.objects.get(pk=id)
        serializer = AuthorSerializer(instance=author,many=False)
        return Response(serializer.data)
    # 更新记录
    def put(self, request, id):
        author = Author.objects.get(pk=id)
        serializer = AuthorSerializer(instance=author,data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response(serializer.errors)
    # 删除记录    
    def delete(self, request, id):    
        author = Author.objects.get(pk=id).delete()
        return Response()
    
""" 序列化 Publish """
class PublishModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = "__all__"

class PublishView(ListCreateAPIView):
    queryset = Publish.objects
    serializer_class = PublishModelSerializer

class PublishDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Publish.objects
    serializer_class = PublishModelSerializer
