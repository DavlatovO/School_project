from django.shortcuts import render
from .import models
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import StudentSerializers, TeacherSerializers, ClassSerializers
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action

class TeacherViewset(mixins.RetrieveModelMixin, 
                      mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = TeacherSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def custom_status(self, request):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
    
class ClassViewset(viewsets.ModelViewSet):
    queryset = models.Class.objects.all()
    serializer_class = ClassSerializers
    
class StudentViewset(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializers