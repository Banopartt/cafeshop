from django.shortcuts import render, get_object_or_404
import requests
from .models import Coffee
# Create your views here.
def home(request):
    coffees = Coffee.objects.all()  # get all coffees from DB
    return render(request, 'cafe/home.html', {'coffees': coffees})

def details(request, id):
    coffee = get_object_or_404(Coffee, id=id)
    return render(request, "cafe/details.html", {"coffee": coffee})

def login_view(request):
    return render(request, 'cafe/login.html')

def register_view(request):
    return render(request, 'cafe/register.html')

def cafe_menu(request):
    coffees = Coffee.objects.all()  # get all coffees from DB
    return render(request, 'cafe/cafe.html', {'coffees': coffees})