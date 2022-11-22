from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required


def home(request):
    # return HttpResponse("Hello my neighbour!")
    return render(request, 'pages/welcome.html', {'today': datetime.today()})


@login_required(login_url='admin/')
def author(request):
    return render(request, 'pages/restricted.html', {})
