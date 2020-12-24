from django import forms
from django.forms import PasswordInput, TextInput
from administrador.models import *
import MySQLdb

host = 'localhost'
db_name = 'proyecto5'
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
    codigoingreso = forms.CharField(max_length=100, required=True, label='Usuario Administrador',
                                    widget=forms.TextInput)
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
    codigoingreso = forms.CharField(max_length=100, label='Nombre de Usuario', widget=forms.TextInput)
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


class CrearCuentaMo(forms.Form):
    quet = 'Q'
    dol = '$'
    elecciones = ((quet, 'Q'),
                  (dol, '$'))

    si = 'Si'
    no = 'No'
    elecciones1 = ((si, 'Si'),
                   (no, 'No'))
    moneda = forms.CharField(widget=forms.Select(choices=elecciones), label='Tipo de Moneda')
    preauto = forms.CharField(widget=forms.Select(choices=elecciones1), label='Pre-Autorizacion')

class CrearCuentaAho(forms.Form):
    quet = 'Q'
    dol = '$'
    elecciones = ((quet, 'Q'),
                  (dol, '$'))

    si = 'Si'
    no = 'No'
    elecciones1 = ((si, 'Si'),
                   (no, 'No'))
    moneda = forms.CharField(widget=forms.Select(choices=elecciones), label='Tipo de Moneda')
    preauto = forms.CharField(widget=forms.Select(choices=elecciones1), label='Pre-Autorizacion')
    interes = forms.CharField(max_length=100, label='Interes', widget=forms.TextInput)


class CrearCuentaPF(forms.Form):
    quet = 'Q'
    dol = '$'
    elecciones = ((quet, 'Q'),
                  (dol, '$'))

    si = 'Si'
    no = 'No'
    elecciones1 = ((si, 'Si'),
                   (no, 'No'))

    tres = 3
    seis = 6
    doce = 12
    dc = 24
    ts = 36
    elecciones2 = ((tres, 3),
    (seis , 6),
    (doce , 12),
    (dc , 24),
    (ts , 36))
    moneda = forms.CharField(widget=forms.Select(choices=elecciones), label='Tipo de Moneda')
    preauto = forms.CharField(widget=forms.Select(choices=elecciones1), label='Pre-Autorizacion')
    interes = forms.CharField(max_length=100, label='Interes (Porcentaje)', widget=forms.TextInput)
    tiempo = forms.CharField(widget=forms.Select(choices=elecciones2), label='Tiempo Definido (Meses)')


class Depositos(forms.Form):
    quet = 'Q'
    dol = '$'
    elecciones = ((quet, 'Q'),
                  (dol, '$'))

    moneda = forms.CharField(widget=forms.Select(choices=elecciones), label='Tipo de Moneda')
    monto = forms.FloatField(max_value=10000, label='Monto a Depositar')
    Descripcion = forms.CharField(widget=forms.TextInput, label='Descripcion')


class Desbloqueos(forms.Form):
    cuentas = forms.ChoiceField(widget=forms.Select(), choices=[], label='Cuentas Bloqueadas')