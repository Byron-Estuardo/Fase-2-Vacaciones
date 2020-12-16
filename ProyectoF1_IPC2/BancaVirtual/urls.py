"""ProyectoF1_IPC2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Principal_view),
    path('Registro/', views.Registro_view),
    path('Inicio/', views.Inicio_view),
    path('Transacciones/EntreCuentas/', views.TCP_view),
    path('Transacciones/Terceros/', views.TCT_view),
    path('Pre-Autorizacion/', views.Pre_view),
    path('Pagos/Servicios/', views.PS_view),
    path('Pagos/PlantillasyProveedores/', views.PP_view),
    path('Solicitud-Prestamos/', views.SPresta_view),
    path('Usuario/', views.Usuario_view),
    path('Usuario/Suspender/', views.Suspender_view),
    path('Usuario/Reactivar/', views.Reactivar_view)
]
