from django.db import models

# Create your models here.

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
    release_date = models.DateField(auto_now=False,verbose_name="Data premiery książki")
    publisher = models.CharField(verbose_name="Wydawnictwo książki", max_length=255)
    language = models.ForeignKey(Language, on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return "%s, %s" % (self.title, self.release_date)

class BookAuthor(models.Model):
    book_id = models.ForeignKey(Book, null=False, on_delete=models.CASCADE, blank=False)
    author_id = models.ForeignKey(Author, null=False,on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return "%s, %s" % (self.book_id, self.author_id)

class BookRental(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(auto_now=True, verbose_name="Data wypożyczenia książki")
    
    def __str__(self):
        return "%s, %s" % (self.customer, self.rental_date)

class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_rental = models.ForeignKey(BookRental, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s, %s" % (self.book, self.book_rental)