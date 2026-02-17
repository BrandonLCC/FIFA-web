from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, 'index.html')


def jugadores(request):
    return render(request, 'jugadores.html')

def equipos(request):
    return render(request, 'equipos.html')