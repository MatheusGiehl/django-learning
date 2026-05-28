from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    frase = 'Olá Mundo!'
    return HttpResponse(frase)