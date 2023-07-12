from rest_framework import serializers

from .models import Student,Book,Publish

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
