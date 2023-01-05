from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, HttpResponse
from .models import Book, Customer, Author, Rental ,Language, Category, BookAuthor
from .serializers import BookSerializer, CustomerSerializer, AuthorSerializer, RentalSerializer, LanguageSerializer, CategorySerializer, BookAuthorSerializer

class book_list(APIView):
    name = "Lista książek"
    def get(self, requset, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

class book_detail(APIView):
    name = 'Informacje o książce'
    def get_object(self,pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

class book_post(APIView):
    name = 'Dodaj książke'
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class book_put(APIView):
    name = 'Edycja książki'
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class book_delete(APIView):
    name = 'Usuń książkę'
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class customer_list(APIView):
    name = "Lista klientów"
    def get(self, requset, format=None):
        customeres = Customer.objects.all()
        serializer = CustomerSerializer(customeres, many=True)
        return Response(serializer.data)

class customer_detail(APIView):
    name = 'Informacje o kliencie'
    def get_object(self,pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

class customer_post(APIView):
    name = 'Dodaj kilenta'
    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class customer_put(APIView):
    name = 'Edycja klienta'
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class customer_delete(APIView):
    name = 'Usuń klienta'
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class author_list(APIView):
    name = "Lista autorów"
    def get(self, requset, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

class author_detail(APIView):
    name = 'Informacje o autorze'
    def get_object(self,pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

class author_post(APIView):
    name = 'Dodaj autora'
    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class author_put(APIView):
    name = 'Edycja autora'
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class author_delete(APIView):
    name = 'Usuń autora'
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class language_list(APIView):
    name = "Lista języków"
    def get(self, requset, format=None):
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)

class language_detail(APIView):
    name = 'Informacje o języku'
    def get_object(self,pk):
        try:
            return Language.objects.get(pk=pk)
        except Language.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        language = self.get_object(pk)
        serializer = LanguageSerializer(language)
        return Response(serializer.data, status=status.HTTP_200_OK)

class language_post(APIView):
    name = 'Dodaj język'
    def post(self, request, format=None):
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class language_put(APIView):
    name = 'Edycja języka'
    def get_object(self, pk):
        try:
            return Language.objects.get(pk=pk)
        except Language.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        language = self.get_object(pk)
        serializer = LanguageSerializer(language)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        language = self.get_object(pk)
        serializer = LanguageSerializer(language, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class language_delete(APIView):
    name = 'Usuń język'
    def get_object(self, pk):
        try:
            return Language.objects.get(pk=pk)
        except Language.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        language = self.get_object(pk)
        serializer = LanguageSerializer(language)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        language = self.get_object(pk)
        language.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class category_list(APIView):
    name = "Lista kategorii"
    def get(self, requset, format=None):
        categoryies = Category.objects.all()
        serializer = CategorySerializer(categoryies, many=True)
        return Response(serializer.data)

class category_detail(APIView):
    name = 'Informacje o kategorii'
    def get_object(self,pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

class category_post(APIView):
    name = 'Dodaj kategorie'
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class category_put(APIView):
    name = 'Edycja kategorii'
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class category_delete(APIView):
    name = 'Usuń kategorie'
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class rental_list(APIView):
    name = "Lista wypożyczeń"
    def get(self, requset, format=None):
        rentals = Rental.objects.all()
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)

class rental_detail(APIView):
    name = 'Informacje o wpożyczeniu'
    def get_object(self,pk):
        try:
            return Rental.objects.get(pk=pk)
        except Rental.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        rental = self.get_object(pk)
        serializer = RentalSerializer(rental)
        return Response(serializer.data, status=status.HTTP_200_OK)

class rental_post(APIView):
    name = 'Dodaj wypożyczenie'
    def post(self, request, format=None):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class rental_put(APIView):
    name = 'Edycja wypożyczenia'
    def get_object(self, pk):
        try:
            return Rental.objects.get(pk=pk)
        except Rental.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        rental = self.get_object(pk)
        serializer = RentalSerializer(rental)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        rental = self.get_object(pk)
        serializer = RentalSerializer(rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class rental_delete(APIView):
    name = 'Usuń wypożyczenie'
    def get_object(self, pk):
        try:
            return Rental.objects.get(pk=pk)
        except Rental.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        rental = self.get_object(pk)
        serializer = RentalSerializer(rental)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        rental = self.get_object(pk)
        rental.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class book_author_list(APIView):
    name = "Lista przypisań książek do autorów"
    def get(self, requset, format=None):
        bookauthors = BookAuthor.objects.all()
        serializer = BookAuthorSerializer(bookauthors, many=True)
        return Response(serializer.data)

class book_author_detail(APIView):
    name = 'Informacje o przypisaniu ksiązek do autora'
    def get_object(self,pk):
        try:
            return BookAuthor.objects.get(pk=pk)
        except BookAuthor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book_author = self.get_object(pk)
        serializer = BookAuthorSerializer(book_author)
        return Response(serializer.data, status=status.HTTP_200_OK)

class book_author_post(APIView):
    name = 'Dodaj book_author'
    def post(self, request, format=None):
        serializer = BookAuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class book_author_put(APIView):
    name = 'Edycja book_author'
    def get_object(self, pk):
        try:
            return BookAuthor.objects.get(pk=pk)
        except BookAuthor.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        book_author = self.get_object(pk)
        serializer = BookAuthorSerializer(book_author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        book_author = self.get_object(pk)
        serializer = BookAuthorSerializer(book_author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class book_author_delete(APIView):
    name = 'Usuń book_author'
    def get_object(self, pk):
        try:
            return BookAuthor.objects.get(pk=pk)
        except BookAuthor.DoesNotExist:
                raise Http404

    def get(self, request, pk, format=None):
        book_author = self.get_object(pk)
        serializer = BookAuthorSerializer(book_author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        book_author = self.get_object(pk)
        book_author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)