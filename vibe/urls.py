"""vibe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from empresavibe import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.raiz),
    path('inicio/', views.index),
    path('casos_de_exito/', views.detalles_porfolio),
    path('cursillo_vibe/', views.cursillo_vibe),
    path('cursillo_vibe/<int:pk>/', views.cursillo_vibe_details, name='cursillo_vibe_details'),
    path('young_engineers_cov/', views.young_engcov),
    path('cursillo_becas/', views.cursillo_becas),
    path('cursillo_becas/<int:pk>/', views.cursillo_becas_details, name='cursillo_becas_details'),
    path('clases_de_apoyo/', views.clases_apoyo),
    path('clases_de_apoyo/<int:pk>/', views.clases_apoyo_details, name='clases_apoyo_details'),
    path('residencia/', views.residencia),
    path('residencia/<int:pk>/', views.residencia_details, name='residencia_details'),
    path('noticias/' , views.noticias),
    path('noticias/<int:pk>/', views.noticias_details, name='noticias_details'),
    path('libreria/', views.libreria),
    path('preguntas_frecuentes/', views.preguntas_frecuentes),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
