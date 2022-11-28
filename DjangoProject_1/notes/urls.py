from django.urls import path

from . import views

urlpatterns = [
    path('notes-titles', views.list_titles, name='noteslistall.all'),
    path('notes-titles/<int:pk>', views.list_eachNote, name='notes.eachone'),
]
