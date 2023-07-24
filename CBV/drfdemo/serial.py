from rest_framework import serializers

from .models import Addr, Student,Book,Publish,User

""" 序列化 Student """
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

""" 序列化 Student """
class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

""" 序列化 Publish """
class PublishModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = "__all__"

""" 序列化 User """
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','last_name','email','mobile','avatar']
        # read_only_fields = ('id')   # 不参与反序列化（只读）
        # extra_kwargs = {            # 更改字段校验规则
        #     'mobile':{
        #         'min_length': 11,
        #         'max_length': 14,
        #         'required': True,
        #     },
        # }

""" 序列化 Addr """
class AddrModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addr
        fields = '__all__'