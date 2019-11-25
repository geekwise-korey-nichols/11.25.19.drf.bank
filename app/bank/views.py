from .models import Branch, Customer
from rest_framework import viewsets
from .serializers import Branch_Serializer, Customer_Serializer

class Branch_Viewset(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = Branch_Serializer

class Customer_Viewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = Customer_Serializer