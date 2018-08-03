from django.shortcuts import render,get_object_or_404
from .models import Letra , Opcion

# Create your views here.
def pasapalabra(request):
    letras = Letra.objects.all()
    return render(request, 'letras/pasapalabra.html', {'letras': letras})