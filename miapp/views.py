from django.shortcuts import render, HttpResponse, redirect
from miapp.forms import FormPersona
from miapp.models import Villanueva_Persona
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def personas(request):
    personas = Villanueva_Persona.objects.all()
    
    return render(request, 'personas.html', {
        'personas': personas,
        'titulo': 'Listado de Personas'
    })

def create_persona(request):
    if request.method == 'POST':
        formulario = FormPersona(request.POST)
        if formulario.is_valid():
            # Guardar los datos del formulario en una nueva instancia de Villanueva_Persona
            nueva_persona = formulario.save()

            # Mensaje flash para mostrar que se agregó correctamente la persona
            messages.success(request, f'Se agregó correctamente a {nueva_persona.nombre} {nueva_persona.apellidos}')

            return redirect('personas')  # Redirigir a la página de listar personas (ajusta según tu URL)

    else:
        formulario = FormPersona()  # Formulario vacío para mostrar al usuario

    return render(request, 'create_persona.html', {
        'form': formulario
    })


def eliminar_persona(request, id):
    persona = Villanueva_Persona.objects.get(pk=id)
    persona.delete()
    return redirect('personas')
