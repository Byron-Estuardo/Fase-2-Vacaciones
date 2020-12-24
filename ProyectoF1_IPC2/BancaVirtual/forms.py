import MySQLdb
from django import forms
from django.forms import PasswordInput, TextInput
from .models import *

host = 'localhost'
db_name = 'xd'
user = 'root'
contra = 'byron14112305'
puerto = 3306
# First view


db = MySQLdb.connect(host=host,
                     user=user,
                     password=contra,
                     db=db_name)

class InicioSesion1(forms.Form):
    codigoingreso = forms.CharField(max_length=100, required=True, label='Usuario',
                                    widget=forms.TextInput)
    clavea = forms.CharField(max_length=100, label='Contraseña', widget=PasswordInput)