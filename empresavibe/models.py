

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
import re



# Create your models here.
class Portada(models.Model):
    titulo = models.TextField()
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


    def __str__(self):
        return self.nombre


class Metodologia(models.Model):
    item_1 = models.CharField(max_length=100)
    item_2 = models.CharField(max_length=100)
    item_3 = models.CharField(max_length=100)
    item_4 = models.CharField(max_length=100)
    item_5 = models.CharField(max_length=100)
    item_6 = models.CharField(max_length=100)
    item_7 = models.CharField(max_length=100)
    item_8 = models.CharField(max_length=100)

    def __str__(self):
        return self.item_1





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
    whatsapp = models.URLField(blank=True)
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()


    def __str__(self):
        return self.direccion


class Categoria_1 (models.Model):
    nombre = models.CharField(null= False, blank= True, max_length=100)

    def __str__(self):
        return self.nombre


class Categoria_2 (models.Model):
    nombre = models.CharField(null= False, blank= True, max_length=100)

    def __str__(self):
        return self.nombre

class Categoria_3 (models.Model):
    nombre = models.CharField(null= False, blank= True, max_length=100)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    imagen = models.ImageField(null=True, blank=True)
    titulo = models.CharField(max_length=250)
    texto = models.TextField()
    categoria_1 = models.ForeignKey('Categoria_1', on_delete=models.CASCADE,null=True, blank=True)
    categoria_2 = models.ForeignKey ('Categoria_2', on_delete=models.CASCADE, null=True, blank=True)
    categoria_3 = models.ForeignKey('Categoria_3', on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateTimeField(blank=True, null=True)


    def get_absolute_url(self):
        return reverse('blog_details', kwargs={'pk': self.pk})


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo


class Cursillo_Vibe(models.Model):
    titulo = models.CharField(max_length=250)
    precio = models.CharField(max_length=100)
    tipo_de_pago = models.CharField(max_length=300)
    beneficio_1 = models.CharField(max_length=300)
    beneficio_2 = models.CharField(max_length=300)
    beneficio_3 = models.CharField(max_length=300)
    materias = models.CharField(max_length=300)
    fecha_de_inicio = models.DateField(blank=True, null=True)
    enlace_formulario = models.CharField(max_length=150, blank=True, null=True)
    enlace_programa = models.CharField(max_length=150, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.enlace_formulario:
            self.enlace_formulario = self.enlace_formulario.split("/")[-1]

        if self.enlace_programa:
            match = re.search(r'\/d\/([a-zA-Z0-9_-]+)', self.enlace_programa)
            if match:
                self.enlace_programa = match.group(1)

        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('cursillo_vibe_details', kwargs={'pk': self.pk})


    def __str__(self):
        return self.titulo


class Cursillo_Becas(models.Model):
    titulo = models.CharField(max_length=250)
    precio = models.CharField(max_length=100)
    tipo_de_pago = models.CharField(max_length=300)
    beneficio_1 = models.CharField(max_length=300)
    beneficio_2 = models.CharField(max_length=300)
    beneficio_3 = models.CharField(max_length=300)
    materias = models.CharField(max_length=300)
    fecha_de_inicio = models.DateField(blank=True, null=True)
    enlace_formulario_beca = models.CharField(max_length=150, blank=True, null=True)
    enlace_programa_beca = models.CharField(max_length=150, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.enlace_formulario_beca:
            self.enlace_formulario_beca = self.enlace_formulario_beca.split("/")[-1]

        if self.enlace_programa_beca:
            match = re.search(r'\/d\/([a-zA-Z0-9_-]+)', self.enlace_programa_beca)
            if match:
                self.enlace_programa_beca = match.group(1)

        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('cursillo_becas_details', kwargs={'pk': self.pk})


    def __str__(self):
        return self.titulo



class Clases_Apoyo(models.Model):
    titulo = models.CharField(max_length=250)
    precio = models.CharField(max_length=100)
    tipo_de_pago = models.CharField(max_length=300)
    beneficio_1 = models.CharField(max_length=300)
    beneficio_2 = models.CharField(max_length=300)
    beneficio_3 = models.CharField(max_length=300)
    materias = models.CharField(max_length=300)
    fecha_de_inicio = models.DateField(blank=True, null=True)
    enlace_formulario_c_apoyo = models.CharField(max_length=150, blank=True, null=True)
    enlace_programa_c_apoyo = models.CharField(max_length=150, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.enlace_formulario_c_apoyo:
            self.enlace_formulario_c_apoyo = self.enlace_formulario_c_apoyo.split("/")[-1]

        if self.enlace_programa_c_apoyo:
            match = re.search(r'\/d\/([a-zA-Z0-9_-]+)', self.enlace_programa_c_apoyo)
            if match:
                self.enlace_programa_c_apoyo = match.group(1)

        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('clases_apoyo_details', kwargs={'pk': self.pk})


    def __str__(self):
        return self.titulo



class Residencia(models.Model):
    nombre_habitacion = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=350)
    precio = models.CharField(max_length=100)
    tipo_de_pago = models.CharField(max_length=50, blank=True, null=True)
    cantidad_de_personas = models.CharField(max_length=50)
    imagen_1 = models.ImageField( blank=True, null=True)
    imagen_2 = models.ImageField( blank=True, null=True)
    imagen_3 = models.ImageField( blank=True, null=True)
    imagen_4 = models.ImageField( blank=True, null=True)
    imagen_5 = models.ImageField( blank=True, null=True)
    imagen_6 = models.ImageField( blank=True, null=True)
    enlace_whatsapp = models.CharField(max_length=350)


    def get_absolute_url(self):
        return reverse('residencia_details', kwargs={'pk': self.pk})


    def __str__(self):
        return self.nombre_habitacion


class Libreria(models.Model):
    nombre_producto = models.CharField(max_length=250)
    precio = models.CharField(max_length=100)
    imagen = models.ImageField( blank=True, null=True)
    enlace_whatsapp = models.CharField(max_length=350)

    def __str__(self):
        return self.nombre_producto



class Preguntas_Frecuentes(models.Model):
    pregunta = models.CharField(max_length=350)
    respuesta = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.pregunta



