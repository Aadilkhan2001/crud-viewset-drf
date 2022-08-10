from dataclasses import field
from rest_framework import serializers
from .models import ProductModels


class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model=ProductModels
        fields=['id','name','price']
        read_only_fields=(['id'])
