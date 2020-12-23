from django import forms
from django.forms import PasswordInput, TextInput
from administrador.models import *


class InicioSesion1(forms.Form):
    codigoingreso = forms.CharField(max_length=100, required=True, label='Usuario Administrador', widget=forms.TextInput)
    clavea = forms.CharField(max_length=100, label='Contraseña', widget=PasswordInput)

class ClienteEmpresarial(forms.Form):
    cui = forms.CharField(max_length=100, required=True, label='CUI', widget=forms.NumberInput)
    nempresa = forms.CharField(max_length=100, label='Nombre de la Empresa')
    ncomercial = forms.CharField(max_length=100, label='Nombre Comercial')
    pnombre = forms.CharField(max_length=100, label='Primer Nombre Representante Legal')
    snombre = forms.CharField(max_length=100, label='Segundo Nombre Representante Legal')
    papellido = forms.CharField(max_length=100, label='Primer Apellido Representante Legal')
    sapellido = forms.CharField(max_length=100, label='Segundo Apellido Representante Legal')
    ubicacion = forms.CharField(max_length=100, label='Ubicacion')
    ntelefono = forms.CharField(max_length=100, label='Numero Telefonico', widget=forms.NumberInput)
    tipoempresa = forms.CharField(max_length=100, label='Tipo de Empresa')
    codigoingreo = forms.CharField(max_length=100, label='Nombre de Usuario', widget=forms.TextInput)
    clavea = forms.CharField(max_length=100, label='Contraseña', widget=PasswordInput)

class ClienteIn(forms.Form):
    cui = forms.CharField(max_length=100, required=True, label='CUI', widget=forms.NumberInput)
    nit = forms.CharField(max_length=100, label='NIT', widget=forms.NumberInput)
    pnombre = forms.CharField(max_length=100, label='Primer Nombre')
    snombre = forms.CharField(max_length=100, label='Segundo Nombre')
    papellido = forms.CharField(max_length=100, label='Primer Apellido')
    sapellido = forms.CharField(max_length=100, label='Segundo Apellido')
    fnacimiento = forms.CharField(max_length=100, label='Fecha de Nacimiento', widget=forms.DateInput)
    correoe = forms.CharField(max_length=100, label='Correo Electronico', widget=forms.EmailInput)
    ntelefono = forms.CharField(max_length=100, label='Numero Telefonico', widget=forms.NumberInput)
    codigoingreso = forms.CharField(max_length=100, label='Nombre de Usuario', widget=forms.TextInput)
    clavea = forms.CharField(max_length=100, label='Contraseña', widget=PasswordInput)

