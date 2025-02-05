from itertools import chain
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.test import Client
from .models import *
import random
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import vibe



# Create your views here.
def index(request):
    portada = Portada.objects.all()
    about = Sobre_Nosotros.objects.all()
    stats = Datos_Estadisticos.objects.all()
    services = Servicios.objects.all()
    clients = Publicidad.objects.all()
    testimonials = Testimonios.objects.all()
    articulos = Post.objects.all().order_by('-fecha')[0:4]
    metodologia = Metodologia.objects.all()
    equipo = Equipo.objects.all()
    cursillo_vibe = Cursillo_Vibe.objects.all().order_by('-id')
    contacto = Contacto.objects.all()

    context = {
        'portada': portada,
        'about': about,
        'stats': stats,
        'services': services,
        'clients': clients,
        'testimonials': testimonials,
        'articulos': articulos,
        'metodologia': metodologia,
        'equipo': equipo,
        'cursillo_vibe': cursillo_vibe,
        'contacto': contacto,

    }
    return render(request, 'index.html', context)

def raiz (request):
    return redirect('/inicio')

def detalles_porfolio(request):
    return render(request, 'portfolio-details.html')


def young_engcov(request):
    return render(request, 'youngengcov.html')

def libreria(request):
    libreria = Libreria.objects.all()
    contacto = Contacto.objects.all()
    context = {
        'libreria': libreria,
        'contacto': contacto,
    }
    return render(request, 'libreria.html', context)



def noticias(request):
    # Obtén todos los artículos (o tu queryset)
    articulos = Post.objects.all().order_by('-fecha')
    contacto = Contacto.objects.all()
    # Número de artículos por página
    paginator = Paginator(articulos, 6)  # por ejemplo, 5 artículos por página
    # Obtiene el número de página de la solicitud GET
    page = request.GET.get('page')
    try:
        articulos_paginados = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un entero, muestra la primera página
        articulos_paginados = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango (e.g., 9999), muestra la última página de resultados
        articulos_paginados = paginator.page(paginator.num_pages)

    return render(request, 'noticias.html', {'articulos': articulos_paginados, 'contacto': contacto})


def noticias_details(request, pk):
    articulo = get_object_or_404(Post, pk=pk)
    articulos = Post.objects.all().order_by('-fecha')[0:6]
    contacto = Contacto.objects.all()

    # Unimos todas las categorías en una sola lista
    categorias = list(chain(Categoria_1.objects.all(), Categoria_2.objects.all(), Categoria_3.objects.all()))

    contexto = {
        "articulo": articulo,
        "articulos": articulos,
        "categorias": categorias,
        'contacto': contacto
    }
    return render(request, 'noticias_details.html', contexto)



def cursillo_vibe(request):
    cursillo_vibe = Cursillo_Vibe.objects.all().order_by('-id')
    contacto = Contacto.objects.all()

    return render(request, 'cursillo_vibe.html', {'cursillo_vibe': cursillo_vibe, 'contacto': contacto })


def cursillo_vibe_details(request, pk):
    cursillo_vibe = get_object_or_404(Cursillo_Vibe, pk=pk)
    contacto = Contacto.objects.all()
    contexto = {
        "cursillo_vibe": cursillo_vibe,
        'contacto': contacto
    }
    return render(request, 'cursillo_vibe_form.html', contexto)

def cursillo_becas(request):
    cursillo_becas = Cursillo_Becas.objects.all().order_by('-id')
    contacto = Contacto.objects.all()

    return render(request, 'cursillo_becas.html', {'cursillo_becas': cursillo_becas, 'contacto': contacto})


def cursillo_becas_details(request, pk):
    cursillo_becas = get_object_or_404(Cursillo_Becas, pk=pk)
    contacto = Contacto.objects.all()
    contexto = {
        "cursillo_becas": cursillo_becas,
        'contacto': contacto
    }
    return render(request, 'cursillo_becas_form.html', contexto)


def clases_apoyo(request):
    clases_apoyo = Clases_Apoyo.objects.all().order_by('-id')
    contacto = Contacto.objects.all()

    return render(request, 'clases_apoyo.html', {'clases_apoyo': clases_apoyo, 'contacto': contacto})


def clases_apoyo_details(request, pk):
    clases_apoyo = get_object_or_404(Clases_Apoyo, pk=pk)
    contacto = Contacto.objects.all()
    contexto = {
        "clases_apoyo": clases_apoyo,
        'contacto': contacto
    }
    return render(request, 'clases_apoyo_form.html', contexto)


def residencia(request):
    residencia = Residencia.objects.all()
    preguntas = Preguntas_Frecuentes.objects.all()
    contacto = Contacto.objects.all()

    return render(request, 'residencia.html', {'residencia': residencia, 'preguntas': preguntas, 'contacto': contacto})


def residencia_details(request, pk):
    residencia = get_object_or_404(Residencia, pk=pk)
    contacto = Contacto.objects.all()
    contexto = {
        "residencia": residencia,
        'contacto': contacto
    }
    return render(request, 'residencia_details.html', contexto)


def preguntas_frecuentes(request):
    preguntas = Preguntas_Frecuentes.objects.all()
    contacto = Contacto.objects.all()

    return render(request, 'preguntas_frecuentes.html', {'preguntas': preguntas, 'contacto': contacto})