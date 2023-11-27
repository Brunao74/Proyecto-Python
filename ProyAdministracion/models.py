#Bruno Rossi

from django.db import models

# Punto A. 

class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    dni = models.IntegerField(primary_key=True)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

#Punto B
class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    banda_horaria = models.ForeignKey('BandaHoraria', on_delete=models.CASCADE)
    nota = models.IntegerField()

    def __str__(self):
        return self.nombre

#Punto C

class BandaHoraria(models.Model):
    nombre = models.CharField(max_length=255)
    horario_inicio = models.DateTimeField()
    horario_fin = models.DateTimeField()

    def __str__(self):
        return self.nombre
