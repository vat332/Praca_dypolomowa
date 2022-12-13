from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Category, Customer, Language, Author, Book, BookAuthor, Rental 
import datetime

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    isbn13 = serializers.CharField(required=True)
    pages = serializers.IntegerField(required=True)
    publisher = serializers.CharField(required=True)
    language = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.isbn13 = validated_data.get('isbn13',instance.isbn13)
        instance.pages = validated_data.get('pages',instance.pages)
        instance.publisher = validated_data.get('publisher',instance.publisher)
        instance.language = validated_data.get('language',instance.language)
        instance.category = validated_data.get('category',instance.category)
        instance.save()
        return instance

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    name2 = serializers.CharField(required=False)
    name3 = serializers.CharField(required=False)
    surname = serializers.CharField(required=True)
    description = serializers.CharField(required=False)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.name2 = validated_data.get('name2',instance.name2)
        instance.name3 = validated_data.get('name3',instance.name3)
        instance.surname = validated_data.get('surname',instance.surname)
        instance.description = validated_data.get('description',instance.description)
        instance.save()
        return instance


class BookAuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    def create(self, validated_data):
        return BookAuthor.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.book_id = validated_data.get('book_id',instance.book_id)
        instance.author_id = validated_data.get('author_id',instance.author_id)
        instance.save()
        return instance

class RentalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    start_time = serializers.DateTimeField(required=True)
    end_time = serializers.DateTimeField(required=True)

    def create(self, validated_data):
        return Rental.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.book = validated_data.get('book',instance.book)
        instance.customer = validated_data.get('customer',instance.customer)
        instance.start_time = validated_data.get('start_time',instance.start_time)
        instance.end_time = validated_data.get('end_time',instance.end_time)
        instance.save()
        return instance

class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    street = serializers.CharField(required=True)
    country = serializers.CharField(required=True)

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.surname = validated_data.get('surname',instance.surname)
        instance.phone_number = validated_data.get('phone_number',instance.phone_number)
        instance.street = validated_data.get('street',instance.street)
        instance.country = validated_data.get('country',instance.country)
        instance.save()
        return instance

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.save()
        return instance

class LanguageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    language_code = serializers.CharField(required=True)
    language_name = serializers.CharField(required=True)

    def create(self, validated_data):
        return Language.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.language_code = validated_data.get('language_code',instance.language_code)
        instance.language_name = validated_data.get('language_name',instance.language_name)
        instance.save()
        return instance
