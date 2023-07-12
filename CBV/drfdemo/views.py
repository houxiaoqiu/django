from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
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


# """ 序列化 Student """
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     gender = serializers.BooleanField()
#     age = serializers.IntegerField()
#     class_number = serializers.CharField()

# """ 查询 Student """
# class StudentView(APIView):
#     # 查询全部记录
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(instance=students,many=True)
#         return Response(serializer.data)
#     # 新增记录
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         try:
#             serializer.is_valid(raise_exception=True)
#             # 新增记录
#             stu = Student.objects.create(**serializer.validated_data)
#             ser = StudentSerializer(instance=stu, many=False)
#             return Response(ser.data)
#         except Exception as e:
#             return Response(serializer.errors)

# """ 详细 Student """    
# class StudentDetailView(APIView):
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
            # 更新记录
            Student.objects.filter(pk=id).update(**serializer.validated_data)
            stu = Student.objects.get(id=id)
            ser = StudentSerializer(instance=stu, many=False)
            return Response(ser.data)
        except Exception as e:
            return Response(serializer.errors)
