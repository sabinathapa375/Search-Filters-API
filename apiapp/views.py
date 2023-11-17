from django.shortcuts import render
from rest_framework.filters import SearchFilter
from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView

# Create your views here.
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [SearchFilter]
    search_fields = ['name', 'passby']
    