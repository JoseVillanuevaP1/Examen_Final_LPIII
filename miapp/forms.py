from django import forms
from django.core import validators
from .models import Villanueva_Persona

class FormPersona(forms.ModelForm):
    class Meta:
        model = Villanueva_Persona
        fields = ['nombre', 'apellidos', 'sexo']
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'sexo': 'Sexo'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre'}),
            'apellidos': forms.TextInput(attrs={'placeholder': 'Ingrese los apellidos'}),
            'sexo': forms.Select(choices=Villanueva_Persona.SEXO_CHOICES)
        }

    nombre = forms.CharField(
        validators=[
            validators.MinLengthValidator(2, 'El nombre es muy corto'),
            validators.MaxLengthValidator(50, 'El nombre es muy largo'),
        ]
    )

    apellidos = forms.CharField(
        validators=[
            validators.MinLengthValidator(2, 'Los apellidos son muy cortos'),
            validators.MaxLengthValidator(50, 'Los apellidos son muy largos'),
        ]
    )

    sexo = forms.TypedChoiceField(
        label='Sexo',
        choices=Villanueva_Persona.SEXO_CHOICES,
        coerce=str
    )
