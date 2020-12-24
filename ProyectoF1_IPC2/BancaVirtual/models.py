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
    idcliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='idCliente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agregada'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cambioc(models.Model):
    codigocambio = models.AutoField(db_column='CodigoCambio', primary_key=True)  # Field name made lowercase.
    fechacambio = models.DateField(db_column='FechaCambio')  # Field name made lowercase.
    correlativo = models.ForeignKey('Cheque', models.DO_NOTHING, db_column='Correlativo')  # Field name made lowercase.
    codigoauto = models.ForeignKey('Preauto', models.DO_NOTHING, db_column='CodigoAuto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cambioc'


class Cheque(models.Model):
    correlativo = models.IntegerField(db_column='Correlativo', primary_key=True)  # Field name made lowercase.
    pnombre = models.CharField(db_column='PNombre', max_length=100)  # Field name made lowercase.
    snombre = models.CharField(db_column='SNombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    papellido = models.CharField(db_column='PApellido', max_length=100)  # Field name made lowercase.
    sapellido = models.CharField(db_column='SApellido', max_length=100, blank=True, null=True)  # Field name made lowercase.
    monto = models.FloatField(db_column='Monto')  # Field name made lowercase.
    estadocobro = models.CharField(db_column='EstadoCobro', max_length=100)  # Field name made lowercase.
    estadoauto = models.CharField(db_column='EstadoAuto', max_length=100)  # Field name made lowercase.
    codigoche = models.ForeignKey('Chequera', models.DO_NOTHING, db_column='CodigoChe', blank=True, null=True)  # Field name made lowercase.
    codigocuenta = models.ForeignKey('Cuenta', models.DO_NOTHING, db_column='CodigoCuenta', blank=True, null=True)  # Field name made lowercase.

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
    codigoingreso = models.CharField(db_column='CodigoIngreso', unique=True, max_length=100)  # Field name made lowercase.
    clavea = models.CharField(db_column='ClaveA', max_length=50)  # Field name made lowercase.
    tipo_usuario = models.CharField(max_length=20)
    idclientein = models.OneToOneField('Clienteindividual', models.DO_NOTHING, db_column='IdClienteIn', blank=True, null=True)  # Field name made lowercase.
    idclienteem = models.OneToOneField('Clienteempresarial', models.DO_NOTHING, db_column='IdClienteEm', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'
        unique_together = (('idcliente', 'codigoingreso'),)


class Clienteempresarial(models.Model):
    idclienteem = models.AutoField(db_column='IdClienteEm', primary_key=True)  # Field name made lowercase.
    cuirl = models.BigIntegerField(db_column='CUIRL', unique=True)  # Field name made lowercase.
    nombreempresa = models.CharField(db_column='NombreEmpresa', max_length=50)  # Field name made lowercase.
    nombrecomercial = models.CharField(db_column='NombreComercial', max_length=50)  # Field name made lowercase.
    pnombrerl = models.CharField(db_column='PNombreRL', max_length=50)  # Field name made lowercase.
    snombrerl = models.CharField(db_column='SNombreRL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    papellidorl = models.CharField(db_column='PApellidoRL', max_length=50)  # Field name made lowercase.
    sapellidorl = models.CharField(db_column='SApellidoRL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ubicacion = models.CharField(db_column='Ubicacion', max_length=300, blank=True, null=True)  # Field name made lowercase.
    ntelefonico = models.IntegerField(db_column='NTelefonico', blank=True, null=True)  # Field name made lowercase.
    tipo_usuario = models.CharField(max_length=12, blank=True, null=True)
    tipo_empresa = models.CharField(db_column='Tipo_Empresa', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clienteempresarial'


class Clienteindividual(models.Model):
    idclientein = models.AutoField(db_column='IdClienteIn', primary_key=True)  # Field name made lowercase.
    cui = models.BigIntegerField(db_column='CUI', unique=True)  # Field name made lowercase.
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
    codigocuenta = models.BigAutoField(db_column='CodigoCuenta', primary_key=True)  # Field name made lowercase.
    saldo = models.FloatField(db_column='Saldo')  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=30)  # Field name made lowercase.
    tipomoneda = models.CharField(db_column='TipoMoneda', max_length=50)  # Field name made lowercase.
    tipocuenta = models.CharField(db_column='TipoCuenta', max_length=100)  # Field name made lowercase.
    preauto = models.CharField(db_column='PreAuto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    interes = models.CharField(db_column='Interes', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tiempo = models.IntegerField(db_column='Tiempo', blank=True, null=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idCliente')  # Field name made lowercase.
    codigoche = models.IntegerField(db_column='CodigoChe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuenta'


class Deposito(models.Model):
    nodeposito = models.AutoField(db_column='NoDeposito', primary_key=True)  # Field name made lowercase.
    monto = models.BigIntegerField()
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    codigocuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='CodigoCuenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deposito'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    cuenta = models.BigIntegerField(db_column='Cuenta')  # Field name made lowercase.
    monto = models.FloatField(db_column='Monto')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    codigocuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='CodigoCuenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trans'
