from django.db import models


# Create your models here.
class Language(models.Model):
    languageCode = models.CharField(verbose_name="Skrótowy kod języka", max_length=10)
    languageName = models.CharField(verbose_name="Nazwa języka", max_length=100)

    def __str__(self):
        return "%s %s" % (self.language_name, self.language_code)


class Author(models.Model):
    name = models.CharField(verbose_name="Imię autora", max_length=255)
    surname = models.CharField(verbose_name="Nazwisko autora", max_length=255)
    description = models.TextField(verbose_name="Informacje o autorze")

    def __str__(self):
        return "%s %s" % (self.name, self.surname)


class Book(models.Model):
    name = models.CharField(verbose_name="Pełna nazwa książki", max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Autor książki")
    page = models.IntegerField(verbose_name="Ilość stron")
    publisher = models.CharField(verbose_name="Wydawwnictwo książki", max_length=255)
    isbn13 = models.CharField(verbose_name="Klucz identyfikacyjny ISBN", max_length=13,)
    releaseDate = models.DateTimeField(verbose_name="Data wydania książki")
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.name, self.author)


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.book, self.author)


class Customer(models.Model):
    name = models.CharField(verbose_name="Imię klienta", max_length=255)
    surname = models.CharField(verbose_name="Nazwisko klienta", max_length=255)
    phoneNumber = models.CharField(verbose_name="Numer telefonu klienta", max_length=9)
    street = models.CharField(verbose_name="Ulica", max_length=100)
    country = models.CharField(verbose_name="Kraj", max_length=255)

    def __str__(self):
        return "%s %s" % (self.name, self.surname)


class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rentalStart = models.DateTimeField(verbose_name="Data wypożyczenia książki")
    rentalEnd = models.DateTimeField(verbose_name="Data końca wypożyczenia")

    def __str__(self):
        return "Nazwa książki: %s\nWypożyczył: %s\nOd: %s\nDo: %s" % (self.book,
                                                                      self.customer, self.rentalStart, self.rentalEnd)
