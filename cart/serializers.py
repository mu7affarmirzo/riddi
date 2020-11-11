from rest_framework import serializers
from .cart import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['title', ' body', 'image', 'date_updated']