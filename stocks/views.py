from django.shortcuts import render
from rest_framework import viewsets

from .serializers import SupplierSerializer
from .models import Supplier

# Create your views here.
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('name')
    serializer_class = SupplierSerializer
