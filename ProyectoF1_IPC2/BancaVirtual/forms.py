import MySQLdb
from django import forms
from django.forms import PasswordInput, TextInput
from .models import *

host = 'localhost'
db_name = 'xd'
user = 'root'
contra = 'byron14112305'
puerto = 3306
idClienteIngresado = ''
# First view


db = MySQLdb.connect(host=host,
                     user=user,
                     password=contra,
                     db=db_name)

class InicioSesion1(forms.Form):
    codigoingreso = forms.CharField(max_length=100, required=True, label='Usuario')
    clavea = forms.CharField(max_length=100, label='Contraseña', widget=PasswordInput)
    class Meta:
        fields = ["codigoingreso","clavea"]
        labels = {
            'codigoingreso': 'Usuario Administrador',
            'clavea': 'Contraseña'
        }

class InicioSesion(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["codigoingreso", "clavea"]
        labels = {
            'codigoingreso': 'Usuario Administrador',
            'clavea': 'Contraseña'
        }
        widgets = {
            "clavea": PasswordInput()
        }


class InicioSesionA(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["codigoingreso", "clavea"]
        labels = {
            'codigoingreso': 'Usuario Administrador',
            'clavea': 'Contraseña'
        }
        widgets = {
            "clavea": PasswordInput()
        }
