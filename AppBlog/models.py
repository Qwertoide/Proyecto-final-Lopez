from django.db import models
from django.contrib.auth.models import User



# Create your models here.





class Avatar(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to="avatares" , null=True , blank=True)
    
    def __str__(self):

        return f"User: {self.user}  -  Imagen: {self.imagen}"




class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} Camada: {self.camada}"


class Alumno(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    curso = models.CharField(max_length=20)

    def __str__(self):
        return f"Nombre: {self.nombre} Apelido: {self.apellido} Curso: {self.curso}"


class Profesor(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    profesion = models.CharField(max_length=30)
    foto = models.ImageField(upload_to="images" , null=True , blank=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Profesión: {self.profesion} - Foto: {self.foto}"
        




class Entregable(models.Model):

    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()

    def __str__(self):
        return f"Nombre: {self.nombre} Fecha de entrega: {self.fecha_de_entrega}"
    
    

    

