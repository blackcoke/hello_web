from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def hello(request):
    return HttpResponse("<h1>Hello Django</h1><p>content...</p>")

def responsewithhtml(request):
    # data = {'first': 'Junhee', 'second': 'Cho'}
    data = {
        'first': request.GET['first'],
        'second': request.GET['second']
    }
    return render(request, 'home/responsewithhtml.html', context=data)

def organization(request):
    data = {
        'name': 'Junhee Cho',
        'Tel': '010-000-0000',
        'address': 'Seoul, Republic of korea'
    }
    return render(request, 'home/organization.html', context=data)

def form(request):
    return render(request, 'home/requestform.html')

def template(request):
    return render(request, 'home/template.html')
