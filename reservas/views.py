from django.shortcuts import render
from .models import Quarto

def home(request):
    quartos = Quarto.objects.all()

    return render(request, 'home.html', {
        'quartos': quartos
    })