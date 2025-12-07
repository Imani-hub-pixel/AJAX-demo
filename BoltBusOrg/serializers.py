from .models import Purchase,ItemForSale
from rest_framework import serializers

class PurchaseSerializer(serializers.ModelSerializer):
    item_name=serializers.CharField(source='item.name',read_only=True)

    class Meta():
        model=Purchase
        fields=['__all__']