from rest_framework import serializers
from .import models


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['name', 'salary', 'subject']   

class ClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Class
        fields = ['name', 'Teachers']

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['full_name', 'Class']        

     