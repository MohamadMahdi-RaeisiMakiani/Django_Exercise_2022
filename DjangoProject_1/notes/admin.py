from django.contrib import admin
from . import models


class MyNotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')


admin.site.register(models.MyNotes, MyNotesAdmin)
