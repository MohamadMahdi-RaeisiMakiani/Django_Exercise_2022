from django.contrib import admin
from . import models


class LibraryBooksAdmin(admin.ModelAdmin):
    list_display = ('book_code', 'book_name', 'book_availability')


admin.site.register(models.AvailableBooks, LibraryBooksAdmin)
