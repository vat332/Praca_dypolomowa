from django.db import models


# Create your models here.
class Language(models.Model):
    language_code = models.CharField(verbose_name="Skrótowy kod języka", max_length=10)
    language_name = models.CharField(verbose_name="Nazwa języka", max_length=100)

    def __str__(self):
        return "%s %s" % (self.language_name, self.language_code)


class Book(models.Model):
    name = models.CharField(verbose_name="Pełna nazwa książki", max_length=255)
    author = models.CharField(verbose_name="Author książki", max_length=255)
    page = models.IntegerField(verbose_name="Ilość stron")
    publisher = models.CharField(verbose_name="Wydawwnictwo książki", max_length=255)
    isbn13 = models.PositiveIntegerField(verbose_name="Klucz identyfikacyjny ISBN", max_length=13)
    realaseDate = models.DateTimeField(verbose_name="Data wydania książki")
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.name, self.author)


class Author(models.Model):
    name = models.CharField(verbose_name="Imię autora", max_length=255)
    surname = models.CharField(verbose_name="Nazwisko autora", max_length=255)
    description = models.TextField(verbose_name="Informacje o autorze")

    def __str__(self):
        return "%s %s" % (self.name, self.surname)


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Customer(models.Model):
    name = models.CharField(verbose_name="Imię klienta", max_length=255)
    surname = models.CharField(verbose_name="Nazwisko klienta", max_length=255)
    phoneNumber = models.CharField(verbose_name="Numer telefonu klienta", max_length=9)
    street = models.CharField(verbose_name="Ulica", max_length=100)
    country = models.CharField(verbose_name="Kraj", max_length=255)

    def __str__(self):
        return "%s %s" % (self.name, self.surname)


class BookRental(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rentalDate = models.DateTimeField(verbose_name="Data wypożyczenia książki")


class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    bookRental = models.ForeignKey(BookRental, on_delete=models.CASCADE)