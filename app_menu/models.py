from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.nombre}"

class Producto(models.Model):
    tipo = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="productos", null=True, blank=True)
    modificacion = models.DateField()

    def __str__(self):
        return f"{self.nombre}: ${self.precio}"


# Hice esta clase de Contacto, para poder tener un formulario tipo Form.
class Contacto (models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} { self.apellido}"