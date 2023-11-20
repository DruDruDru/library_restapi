from django.contrib import admin

from .models import Book, Author, Cover


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Cover)
