from django.contrib import admin
from .models import (Book,Author,BookAuthor,Language,Rental,Customer)
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookAuthor)
admin.site.register(Language)
admin.site.register(Rental)
admin.site.register(Customer)