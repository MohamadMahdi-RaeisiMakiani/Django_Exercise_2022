from django.urls import path

from . import views

urlpatterns = [
    path('notes-titles', views.list_titles),
    path('notes-titles/<int:pk>', views.list_eachNote),
]
