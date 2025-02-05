from django.db import models

# Create your models here.
class Portada(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    imagen = models.ImageField()
    link_video = models.URLField()

    def __str__(self):
        return self.titulo

class Sobre_Nosotros(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    imagen = models.ImageField()
    texto_1 = models.TextField()
    mision = models.TextField()
    vision = models.TextField()
    texto_2 = models.TextField()
    texto_3 = models.TextField()
    imagen_2 = models.ImageField()
    enlace = models.URLField()

    def __str__(self):
        return self.titulo

class Datos_Estadisticos(models.Model):
    numero_de_ingresantes = models.CharField(max_length=100)
    numero_examenes_de_ingreso = models.CharField(max_length=100)
    numero_horas_de_clase = models.CharField(max_length=100)
    numero_miembros_de_equipo = models.CharField(max_length=100)

    def __str__(self):
        return self.numero_de_ingresantes


class Servicios(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField()
    enlace = models.URLField()


    def __str__(self):
        return self.titulo


class Publicidad(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField()
    enlace = models.URLField()


    def __str__(self):
        return self.nombre


class Testimonios(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField()
    puesto = models.CharField(max_length=100)
    testimonio = models.TextField()


    def __str__(self):
        return self.nombre


class Casos_de_exito(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField()
    descripcion = models.TextField()
    enlace = models.URLField()


    def __str__(self):
        return self.titulo

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField()
    cargo = models.CharField(max_length=100)
    enlace = models.URLField()
    enlace_1 = models.URLField()
    enlace_2 = models.URLField()
    enlace_3 = models.URLField()


    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField()
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()


    def __str__(self):
        return self.direccion








