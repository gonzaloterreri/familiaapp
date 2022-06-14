from django.db import models

class Familiar(models.Model):
    nombre = models.CharField("Nombre" , max_length=20)
    apellido = models.CharField("Apellido" , max_length=20)
    nacimiento = models.DateTimeField("Nacimiento")
    email = models.EmailField("Email")