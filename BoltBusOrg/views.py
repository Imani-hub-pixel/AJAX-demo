from django.shortcuts import render
from django.urls import re_path
from .models import Purchase
from .serializers import PurchaseSerializer
from rest_framework import generics

# Create your views here.

class PurchaseList(generics.ListAPIView):
    serializer_class=PurchaseSerializer

    def get_queryset(self):
        user=self.request.user
        return Purchase.objects.filter(purchaser=user)

re_path('^purchase/(?<username>.+)/$',PurchaseList.as_view())

