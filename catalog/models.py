from django.db import models

# Create your models here.

class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100, null=True, blank=True)
    img_url = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Desarrollador(models.Model):
    nombre = models.CharField(max_length=150)
    pais = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)
    fecha_lanzamiento = models.DateField(null=True, blank=True)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE)
    img_url = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo