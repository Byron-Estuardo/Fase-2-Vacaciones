from django import forms
from .models import *

class Cliente(forms.ModelForm):
    codigoingreso = models.IntegerField(db_column='CodigoIngreso')  # Field name made lowercase.
    clavea = models.CharField(db_column='ClaveA', max_length=50)  # Field name made lowercase.
    tipo_usuario = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'cliente'
        unique_together = (('idcliente', 'codigoingreso'),)


class InicioSesion(forms.Form):
    idproducto = forms.IntegerField(required = True, help_text='Campo numerico, ingrese solo digitos')
    nombre = forms.CharField(max_length=50, help_text='Nombre del producto',required = True)
    class Meta:
        fields = ("idproducto","nombre")
