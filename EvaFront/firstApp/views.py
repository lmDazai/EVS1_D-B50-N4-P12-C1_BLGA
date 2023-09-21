from django.shortcuts import render
from django.https import HttpResponse

# Create your views here.

def display(request):
    return HttpResponse("<h1> hola </h1>")