import uuid

from django.db import models
from .validators import validar_ci, validar_texto

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=100, validators=[validar_texto])
    apellido = models.CharField(max_length=100, validators=[validar_texto])
    ci = models.CharField(max_length=10, unique=True, validators=[validar_ci])
    email = models.EmailField(unique=True)
    fecha_ingreso = models.DateField(auto_now_add=True)
    estado = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"        
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    gestion = models.CharField(max_length=5)

    class Meta:
        unique_together = ('alumno', 'materia')

    def __str__(self):
        return f"{self.alumno} inscrito en {self.materia}"

class Nota(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Nota del Alumno {self.inscripcion.alumno} en {self.inscripcion.materia} es de: {self.nota}"