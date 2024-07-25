from rest_framework import viewsets
from .models import Student, Subject
from .serializers import subject_serializer, student_serializer

# Create your views here.
class student_view_set(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = student_serializer

class subject_view_set(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = subject_serializer
    
