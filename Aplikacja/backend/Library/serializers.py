from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    author = serializers.CharField(max_length=255)
    page = serializers.IntegerField()
    publisher = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.author = validated_data.get('author', instance.author)
        instance.page = validated_data.get('paga', instance.page)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.save()
        return instance