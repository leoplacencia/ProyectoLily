from django.shortcuts import render,get_object_or_404
from .models import Letra , Opcion
from django.http import JsonResponse


# Create your views here.
def pasapalabra(request):
    letras = Letra.objects.all()
    letra_actual = Letra.objects.filter(opcion_id= 4).first()
    score =  len(Letra.objects.filter(opcion_id= 1))
    # get_object_or_404(Letra, opcion_id= 4).first()
    return render(request, 'letras/pasapalabra.html', {'letras': letras,'letra_actual':letra_actual,'score':score})

def buena(request, letra_id):
    letra = get_object_or_404(Letra, id= letra_id)
    letra.opcion_id = 1
    letra.save()
    return JsonResponse({'respuesta':1})
def mala(request, letra_id):
    letra = get_object_or_404(Letra, id= letra_id)
    letra.opcion_id = 2
    letra.save()
    return JsonResponse({'respuesta':1})
def pasa(request, letra_id):
    letra = get_object_or_404(Letra, id= letra_id)
    letra.opcion_id = 3
    letra.save()
    return JsonResponse({'respuesta':1})

def reiniciar(request):
    letras = Letra.objects.all()
    for letra in letras:
        letra.opcion_id = 4
        letra.save()

    return JsonResponse({'respuesta':1})
