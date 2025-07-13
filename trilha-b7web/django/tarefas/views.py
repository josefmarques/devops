from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    frase = "Hello World"
    return HttpResponse(frase)
    
