from django.contrib import admin
from .models import Book,Language,Author,BookAuthor,Customer,Rental
# Register your models here.

admin.site.register(Book)
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(BookAuthor)
admin.site.register(Customer)
admin.site.register(Rental)
