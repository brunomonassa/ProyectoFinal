from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Venta(models.Model):

    ubicacion = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    precio = models.IntegerField()
    habitaciones = models.IntegerField()

    def __str__(self):
        return f"Ubicacion: {self.ubicacion} - Direccion: {self.direccion} - Precio: {self.precio} - Habitaciones: {self.habitaciones}"

class Alquiler(models.Model):

    ubicacion = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    precio = models.IntegerField()
    habitaciones = models.IntegerField()

    def __str__(self):
        return f"Ubicacion: {self.ubicacion} - Direccion: {self.direccion} - Precio: {self.precio} - Habitaciones: {self.habitaciones}"

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
