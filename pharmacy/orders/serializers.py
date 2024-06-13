from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    username =  serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ("id", "username", "drug_id", "quantity", "status")
    
    def get_username(self,obj):
        return obj.username.username

class OrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "username", "drug_id", "quantity", "status")