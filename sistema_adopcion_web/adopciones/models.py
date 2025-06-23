from django.db import models

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    tamaño = models.CharField(max_length=20, choices=[('pequeño', 'Pequeño'), ('mediano', 'Mediano'), ('grande', 'Grande')])
    peso = models.FloatField()
    estado_salud = models.CharField(max_length=100)
    vacunado = models.BooleanField(default=False)
    estado = models.CharField(max_length=20, choices=[('disponible', 'Disponible'), ('reservado', 'Reservado'), ('adoptado', 'Adoptado')])
    temperamento = models.CharField(max_length=50, choices=[('tranquilo','Tranquilo'), ('jugueton','Juguetón'), ('protector','Protector'), ('sociable','Sociable')])

class UsuarioAdoptante(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    preferencias_raza = models.CharField(max_length=50, null=True, blank=True)
    preferencias_edad = models.IntegerField(null=True, blank=True)
    preferencias_tamaño = models.CharField(max_length=20, null=True, blank=True)