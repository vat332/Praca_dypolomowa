from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="Nazwa kategorii",blank=False,max_length=50)
    description = models.TextField(verbose_name="Opis kateorii",blank=True)

class Customer(models.Model):
    name = models.CharField(verbose_name="Imię klienta", max_length=255)
    surname = models.CharField(verbose_name="Nazwisko klienta", max_length=255)
    phone_number = models.CharField(verbose_name="Numer telefonu klienta", max_length=9)
    street = models.CharField(verbose_name="Ulica", max_length=100)
    country = models.CharField(verbose_name="Kraj", max_length=255)

    def __str__(self):
        return "%s %s" % (self.name, self.surname)

class Language(models.Model):
    language_code = models.CharField(verbose_name="Skrótowy kod języka", max_length=10,default="ENG")
    language_name = models.CharField(verbose_name="Nazwa języka", max_length=100,default="English")

    def __str__(self):
        return "%s %s" % (self.language_name, self.language_code)

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Imię autora",blank=False)
    name2 = models.CharField(max_length=100,verbose_name="Drugie imię autora (Opcjonalnie)",blank=True)
    name3 = models.CharField(max_length=100,verbose_name="Trzecie imię autora (Opcjonalnie)",blank=True)
    surname = models.CharField(max_length=200,verbose_name="Nazwisko autora",blank=False)
    description = models.TextField(blank=True,verbose_name="Opis autora")

    def __str__(self):
        return "%s %s" % (self.name, self.surname)

class Book(models.Model):
    title = models.CharField(max_length=200,verbose_name="Pełna nazwa książki")
    isbn13 = models.CharField(max_length=13,verbose_name="Numer ISBN, 13 znakowy")
    pages = models.IntegerField(verbose_name="Ilość stron")
    release_date = models.DateField(auto_now=True,verbose_name="Data premiery książki")
    publisher = models.CharField(verbose_name="Wydawnictwo książki", max_length=255)
    language = models.ForeignKey(Language, on_delete=models.CASCADE,blank=True,verbose_name="Język")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Gatunek książki",blank=False)

    def __str__(self):
        return "%s, %s" % (self.title, self.release_date)

class BookAuthor(models.Model):
    book_id = models.ForeignKey(Book, null=False, on_delete=models.CASCADE, blank=False,verbose_name="Książka")
    author_id = models.ForeignKey(Author, null=False,on_delete=models.CASCADE, blank=False,verbose_name="Autor")

    def __str__(self):
        return "%s, %s" % (self.book_id, self.author_id)


class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,verbose_name="Nazwa książki")
    start_time = models.DateTimeField(auto_now=True, verbose_name="Początek wypożyczenia")
    end_time = models.DateTimeField(auto_now=True, verbose_name="Koniec wypożyczenia")
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE,blank=False,verbose_name="Osoba która wypożycza")
    
    def __str__(self):
        return "%s, %s" % (self.book, self.customer)