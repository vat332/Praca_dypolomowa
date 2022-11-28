from rest_framework import serializers
from .models import Book, Language, Customer, Rental, Author


class BookSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    page = serializers.IntegerField()
    isbn13 = serializers.CharField(max_length=13)
    releaseDate = serializers.DateTimeField()
    language = serializers.CharField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.page = validated_data.get('paga', instance.page)
        instance.isbn13 = validated_data.get('isbn13', instance.isbn13)
        instance.language = validated_data.get('language', instance.language)
        instance.releaseDate = validated_data.get('releaseDate', instance.releaseDate)
        instance.save()
        return instance


class LanguageSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    languageCode = serializers.CharField(max_length="10")
    languageName = serializers.CharField(max_length="100")

    def create(self, validated_data):
        return Language.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.languageCode = validated_data.get('languageCode', instance.languageCode)
        instance.languageName = validated_data.get('languageName', instance.languageName)
        instance.save()
        return instance


class CustomerSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    surname = serializers.CharField(max_length=255)
    phoneNumber = serializers.CharField(max_length=9)
    street = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
        instance.street = validated_data.get('street', instance.street)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance


class RentalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rentalStart = serializers.DateTimeField()
    rentalEnd = serializers.DateTimeField()
    def create(self, validated_data):
        return Rental.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.rentalStart = validated_data.get('rentalStart', instance.rentalStart)
        instance.rentalEnd = validated_data.get('rentalEnd', instance.rentalEnd)
        instance.save()
        return instance


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    surname = serializers.CharField(max_length=255)
    description = serializers.CharField()

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance