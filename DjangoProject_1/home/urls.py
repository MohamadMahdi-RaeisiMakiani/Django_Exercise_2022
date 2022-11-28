from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='app.mainpage'),
    path('author', views.author),
]
