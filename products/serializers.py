# form

from rest_framework import serializers
from .models import Product , Brand , Review , ProductImages


class ProductListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'



class ProductDetailSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['id'.'name']

class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


