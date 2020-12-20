# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agregada(models.Model):
    codigocuenta = models.ForeignKey('Cuenta', models.DO_NOTHING, db_column='CodigoCuenta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agregada'


class Cambioc(models.Model):
    codigocambio = models.AutoField(db_column='CodigoCambio', primary_key=True)  # Field name made lowercase.
    fechacambio = models.DateField(db_column='FechaCambio')  # Field name made lowercase.
    correlativo = models.ForeignKey('Cheque', models.DO_NOTHING, db_column='Correlativo', blank=True, null=True)  # Field name made lowercase.
    codigoauto = models.ForeignKey('Preauto', models.DO_NOTHING, db_column='CodigoAuto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cambioc'


class Cheque(models.Model):
    correlativo = models.IntegerField(db_column='Correlativo', primary_key=True)  # Field name made lowercase.
    cuentadestino = models.BigIntegerField(db_column='CuentaDestino')  # Field name made lowercase.
    pnombre = models.CharField(db_column='PNombre', max_length=100)  # Field name made lowercase.
    snombre = models.CharField(db_column='SNombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    papellido = models.CharField(db_column='PApellido', max_length=100)  # Field name made lowercase.
    sapellido = models.CharField(db_column='SApellido', max_length=100, blank=True, null=True)  # Field name made lowercase.
    monto = models.FloatField(db_column='Monto')  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=100)  # Field name made lowercase.
    codigoche = models.ForeignKey('Chequera', models.DO_NOTHING, db_column='CodigoChe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cheque'


class Chequera(models.Model):
    codigoche = models.AutoField(db_column='CodigoChe', primary_key=True)  # Field name made lowercase.
    dispocheque = models.IntegerField(db_column='DispoCheque')  # Field name made lowercase.
    codigocuenta = models.ForeignKey('Cuenta', models.DO_NOTHING, db_column='CodigoCuenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chequera'


class Cliente(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    codigoingreso = models.IntegerField(db_column='CodigoIngreso')  # Field name made lowercase.
    clavea = models.CharField(db_column='ClaveA', max_length=50)  # Field name made lowercase.
    tipo_usuario = models.CharField(max_length=20)
    idclientein = models.ForeignKey('Clienteindividual', models.DO_NOTHING, db_column='IdClienteIn', blank=True, null=True)  # Field name made lowercase.
    idclienteem = models.ForeignKey('Clienteempresarial', models.DO_NOTHING, db_column='IdClienteEm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'
        unique_together = (('idcliente', 'codigoingreso'),)


class Clienteempresarial(models.Model):
    idclienteem = models.AutoField(db_column='IdClienteEm', primary_key=True)  # Field name made lowercase.
    cuirl = models.BigIntegerField(db_column='CUIRL')  # Field name made lowercase.
    nombreempresa = models.CharField(db_column='NombreEmpresa', max_length=50)  # Field name made lowercase.
    nombrecomercial = models.CharField(db_column='NombreComercial', max_length=50)  # Field name made lowercase.
    pnombrerl = models.CharField(db_column='PNombreRL', max_length=50)  # Field name made lowercase.
    snombrerl = models.CharField(db_column='SNombreRL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    papellidorl = models.CharField(db_column='PApellidoRL', max_length=50)  # Field name made lowercase.
    sapellidorl = models.CharField(db_column='SApellidoRL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ubicacion = models.CharField(db_column='Ubicacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ntelefonico = models.IntegerField(db_column='NTelefonico', blank=True, null=True)  # Field name made lowercase.
    tipo_usuario = models.CharField(max_length=12, blank=True, null=True)
    tipo_empresa = models.CharField(db_column='Tipo_Empresa', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clienteempresarial'


class Clienteindividual(models.Model):
    idclientein = models.AutoField(db_column='IdClienteIn', primary_key=True)  # Field name made lowercase.
    cui = models.BigIntegerField(db_column='CUI')  # Field name made lowercase.
    nit = models.BigIntegerField(db_column='NIT')  # Field name made lowercase.
    pnombre = models.CharField(db_column='PNombre', max_length=100)  # Field name made lowercase.
    snombre = models.CharField(db_column='SNombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    papellido = models.CharField(db_column='PApellido', max_length=100)  # Field name made lowercase.
    sapellido = models.CharField(db_column='SApellido', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fnacimiento = models.DateField(db_column='FNacimiento')  # Field name made lowercase.
    correoe = models.CharField(db_column='CorreoE', max_length=100)  # Field name made lowercase.
    ntelefonico = models.IntegerField(db_column='NTelefonico', blank=True, null=True)  # Field name made lowercase.
    tipo_usuario = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'clienteindividual'


class Cuenta(models.Model):
    codigocuenta = models.BigIntegerField(db_column='CodigoCuenta', primary_key=True)  # Field name made lowercase.
    saldo = models.IntegerField(db_column='Saldo')  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=30)  # Field name made lowercase.
    tipomoneda = models.CharField(db_column='TipoMoneda', max_length=50)  # Field name made lowercase.
    tipocuenta = models.CharField(db_column='TipoCuenta', max_length=100)  # Field name made lowercase.
    preauto = models.IntegerField(db_column='PreAuto', blank=True, null=True)  # Field name made lowercase.
    interes = models.CharField(db_column='Interes', max_length=50)  # Field name made lowercase.
    tiempo = models.IntegerField(db_column='Tiempo')  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente')  # Field name made lowercase.
    codigoche = models.IntegerField(db_column='CodigoChe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuenta'


class Deposito(models.Model):
    nodeposito = models.AutoField(db_column='NoDeposito', primary_key=True)  # Field name made lowercase.
    cuentadestino = models.BigIntegerField(db_column='CuentaDestino')  # Field name made lowercase.
    monto = models.BigIntegerField()
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    codigocuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='CodigoCuenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deposito'


class Preauto(models.Model):
    codigoauto = models.AutoField(db_column='CodigoAuto', primary_key=True)  # Field name made lowercase.
    correlativo = models.IntegerField(db_column='Correlativo')  # Field name made lowercase.
    cuentadestino = models.BigIntegerField(db_column='CuentaDestino')  # Field name made lowercase.
    pnombre = models.CharField(db_column='PNombre', max_length=100)  # Field name made lowercase.
    snombre = models.CharField(db_column='SNombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    papellido = models.CharField(db_column='PApellido', max_length=100)  # Field name made lowercase.
    sapellido = models.CharField(db_column='SApellido', max_length=100, blank=True, null=True)  # Field name made lowercase.
    monto = models.FloatField(db_column='Monto')  # Field name made lowercase.
    codigoche = models.ForeignKey(Chequera, models.DO_NOTHING, db_column='CodigoChe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'preauto'


class Trans(models.Model):
    codigotransaccion = models.AutoField(db_column='CodigoTransaccion', primary_key=True)  # Field name made lowercase.
    cuentad = models.BigIntegerField(db_column='CuentaD')  # Field name made lowercase.
    monto = models.FloatField(db_column='Monto')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    codigocuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='CodigoCuenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trans'
