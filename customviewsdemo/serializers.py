from .models import Book
from rest_framework import serializers

class BookSerilazer(serializers.ModelSerializer):
    genre_name=serializers.CharField(source='genre.name',read_only=True)

    class Meta:
        model=Book
        fields=['title','author']