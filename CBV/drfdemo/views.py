
import re
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from rest_framework.views import APIView
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin, \
    # RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# from rest_framework.viewsets import ViewSetMixin
from rest_framework.viewsets import ModelViewSet

from .models import Student,Book,Publish,Author,\
    NaturalPerson,LegalPerson,Employee,User,Department
from .serial import StudentModelSerializer,BookModelSerializer,PublishModelSerializer

# 用户登录
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError,InvalidToken
from rest_framework.response import Response
class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        result = serializer.validated_data
        result['id'] = serializer.user.id
        result['mobile'] = serializer.user.mobile
        result['email'] = serializer.user.email
        result['username'] = serializer.user.username
        result['token'] = result.pop('access')
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

""" 用户注册"""
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        password_confirmation = request.data.get('password_confirmation')
        # 校验参数是否为空
        if not all([username,email,password,password_confirmation]):
            return Response(
                {'error': "所有参数均不能为空"},
                status = status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        # 校验用户是否已注册
        if User.objects.filter(username=username).exists(): 
            return Response(
                { "errors": "用户已注册"},
                status = status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        # 校验密码是否一致
        if password != password_confirmation:
            return Response(
                { "errors": "密码与确认密码不一致"},
                status = status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        # 校验密码长度
        if not ( 6 <= len(password) <= 18 ):
            return Response(
                { "errors": "密码长度不满足6~18位"},
                status = status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        # 校验邮箱
        if User.objects.filter(email=email).exists(): 
            return Response(
                { "errors": "该邮箱已被其他注册用户使用"},
                status = status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$',email):
            return Response(
                { "errors": "邮箱格式不正确"},
                status = status.HTTP_422_UNPROCESSABLE_ENTITY                
            )
        # 创建用户
        obj = User.objects.create_user(username=username,email=email,password=password)
        # 返回用户信息
        res = {
                "id": obj.id, 
                "username": obj.username,                            
                "email": obj.email,
            }
        return Response(res,status=status.HTTP_201_CREATED)
        
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
class AuthorModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

""" 集成视图 Author """
class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

""" 序列化 Publish """
class PublishModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publish
        fields = "__all__"
        
    # 反序列化校验字段
    def validate_name(self,value):
        if value.endswith("出版社"):
            return value
        else:
            raise serializers.ValidationError('出版商名称须以“出版社”结尾')

""" 集成视图 Publish """
class PublishView(ModelViewSet):
    queryset = Publish.objects.all()
    serializer_class = PublishModelSerializer

""" 自然人 NaturalPerson """
class NaturalPersonModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NaturalPerson
        fields = "__all__"

class NaturalPersonView(ModelViewSet):
    queryset = NaturalPerson.objects.all()
    serializer_class = NaturalPersonModelSerializer
          
""" 法人 LegalPerson """
class LegalPersonModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LegalPerson
        fields = "__all__"

class LegalPersonView(ModelViewSet):
    queryset = LegalPerson.objects.all()
    serializer_class = LegalPersonModelSerializer

""" 雇员 Employee """
class EmployeeModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class EmployeeView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer

""" 用户 User """
class UserModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

""" 部门 Department """
class DepartmentModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer