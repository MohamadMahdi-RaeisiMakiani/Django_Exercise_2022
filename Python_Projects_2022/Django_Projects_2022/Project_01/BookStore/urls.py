from django.urls import path
from . import views

urlpatterns = [
    path('time-res', views.TodayRestrictedView.as_view()),
    path('store-library-a-books', views.AvailableBooksNamesView.as_view()),
    path('store-library-a-books/<int:pk>',
         views.AvailableBookDetailsView.as_view()),
]
