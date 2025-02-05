from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.test import Client

from .models import *
import random
from django.core.paginator import Paginator

import vibe


# Create your views here.
def index(request):
    portada = Portada.objects.all()
    about = Sobre_Nosotros.objects.all()
    stats = Datos_Estadisticos.objects.all()
    services = Servicios.objects.all()
    clients = Publicidad.objects.all()
    testimonials = Testimonios.objects.all()

    context = {
        'portada': portada,
        'about': about,
        'stats': stats,
        'services': services,
        'clients': clients,
        'testimonials': testimonials,
    }
    return render(request, 'index.html', context)

def raiz (request):
    return redirect('/inicio')

def detalles_porfolio(request):
    return render(request, 'portfolio-details.html')

def service_details(request):
    return render(request, 'service-details.html')
