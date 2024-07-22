# Create your models here.
from django.db import models

class Villanueva_Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    SEXO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    ]
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    fecha_de_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

