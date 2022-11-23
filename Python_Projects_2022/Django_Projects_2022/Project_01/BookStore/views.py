from django.shortcuts import render
from datetime import datetime as u_time
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from .models import AvailableBooks


# LoginRequiredMixin is optional for making restricted area to people who logged in
class TodayRestrictedView(LoginRequiredMixin, TemplateView):
    template_name = 'store_library/today_show_time.html'
    extra_context = {'today': u_time.today()}
    login_url = 'admin/'


# to access all model objects - context_object_name is the name for model.objects.all()
class AvailableBooksNamesView(ListView):
    model = AvailableBooks
    context_object_name = 'book_names_title'
    template_name = 'store_library/available_book_list.html'


# django is smart and it may find the template but it's better to define the template_name
class AvailableBookDetailsView(DetailView):
    model = AvailableBooks
    context_object_name = 'just_one_book'
    template_name = 'store_library/books_all_details.html'
