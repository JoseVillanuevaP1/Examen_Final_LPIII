from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def personas(request):
    return render(request, 'personas.html',{
        'titulo': 'Listado de Personas'
    })