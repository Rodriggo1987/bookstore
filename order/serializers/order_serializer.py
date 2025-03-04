from rest_framework import seriallizers

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(seriallizers.ModelSerializer):  # trabalhar em conjunto com os nossos modelos
    Product = ProductSerializer(required=True, many=True)
    total = seriallizers.SerializerMethodField()
    
    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        
    class Meta: 
        model = Product
        field = ['product', 'total'] 
        
           