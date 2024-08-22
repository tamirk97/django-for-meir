from rest_framework import viewsets
from .models import Student, Car
from .serializers import StudentSerializer, CarSerializer
from rest_framework.permissions import AllowAny

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny] 

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [AllowAny]     