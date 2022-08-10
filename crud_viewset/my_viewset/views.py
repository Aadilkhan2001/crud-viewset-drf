from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework import viewsets
from .models import ProductModels

# Create your views here.
class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModels.objects.all()

    def update(self, request, *args, **kwargs):
        return super().update(request,partial=True, *args, **kwargs)





