import MySQLdb
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.db import connection
from .forms import *
import random
import string

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
# Create your views here.

def inicioAdmin(request):
    form = InicioSesion1()
    variables = {
        "form": form
    }
    if request.method == "POST":
        form = InicioSesion1(data=request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            usuario = datos.get("codigoingreso")
            clave = datos.get("clavea")
            cur = db.cursor()
            consulta2 = "select idCliente, tipo_usuario from Cliente where CodigoIngreso = '" + usuario + "' and ClaveA = '" + clave + "'"
            cur.execute(consulta2)
            row = cur.fetchone()
            if row is not None:
                tipo = row[1]
                if tipo == 'Administrador':

                    return render(request, "InicioAdmin.html", variables)
                else:
                    print('Wacho que no salio')
                    return render(request, "LoginAdmin.html", variables)
            else:
                print('no jalo')
                return render(request, "LoginAdmin.html", variables)
            db.close()
            form = InicioSesion()
            variables = {
                "form": form
            }
            return render(request, "InicioAdmin.html", variables)
        else:
            form.clean()
            variables = {
                "form": form.full_clean()
            }

    return render(request, "LoginAdmin.html", variables)

def RegIndividual(request):
    print(idClienteIngresado)
    form = ClienteIn()
    nombre = ''
    variables = {
        "mensaje": nombre,
        "form": form
    }
    if request.method == "POST":
        form = ClienteIn(data=request.POST)
        if form.is_valid():
            try:
                datos = form.cleaned_data
                cui = datos.get("cui")
                nit = datos.get("nit")
                pnombre = datos.get("pnombre")
                snombre = datos.get("snombre")
                pallido = datos.get("papellido")
                sallido = datos.get("sapellido")
                nacimiento = datos.get("fnacimiento")
                correoe =datos.get("correoe")
                ntel = datos.get("ntelefono")
                us = datos.get("codigoingreso")
                con = datos.get("clavea")

                #Primer Consulta
                cur = db.cursor()
                consulta2 = "insert into ClienteIndividual(CUI, NIT, PNombre, SNombre, PApellido, SApellido, FNacimiento, CorreoE, NTelefonico, tipo_usuario)values(" + cui + ",'" + nit + "','" + pnombre + "','" + snombre + "','" + pallido + "','" + sallido + "','" + nacimiento + "','" + correoe + "'," + ntel + ", 'Individual')"
                cur.execute(consulta2)
                db.commit()
                cur.close()
                #Segunda consulta
                cur5 = db.cursor()
                consulta3 = "select IdClienteIn from ClienteIndividual where CUI = " + cui + ""
                cur5.execute(consulta3)
                row = cur5.fetchone()
                val = row[0]
                cur5.close()
                #Tercer consulta
                cur1 = db.cursor()
                data = [us, con, 'Individual', val]
                consulta9 = "insert into Cliente(CodigoIngreso,ClaveA, tipo_usuario, IdClienteIn) values ('"+str(us)+"' , '"+str(con)+"', 'Individual' , "+ str(val) +")"
                cur1.execute(consulta9)
                db.commit()
                cur1.close()


                form = ClienteIn()

                variables = {
                    "form": form,
                    "mensaje": nombre
                }
                return render(request, 'InicioAdmin.html', variables)
            except:
                form = ClienteIn()
                variables = {
                    "form": form
                }
                return render(request, 'RegistroClientesIn.html', variables)
        else:
            form = ClienteIn()
            variables = {
                "form": form
            }

    return render(request, 'RegistroClientesIn.html', variables)

def RegEmpresarial(request):
    print(idClienteIngresado)
    form = ClienteEmpresarial()
    nombre = ''
    variables = {
        "mensaje" : nombre,
        "form": form
    }
    if request.method == "POST":
        form = ClienteEmpresarial(data=request.POST)
        if form.is_valid():
            try:
                datos = form.cleaned_data
                cui = datos.get("cui")
                nempresa = datos.get("nempresa")
                ncomercial = datos.get("ncomercial")
                pnombre = datos.get("pnombre")
                snombre = datos.get("snombre")
                pallido = datos.get("papellido")
                sallido = datos.get("sapellido")
                ubicacion = datos.get("ubicacion")
                ntel = datos.get("ntelefono")
                typempresa = datos.get("tipoempresa")

                us = datos.get("codigoingreso")
                con = datos.get("clavea")
                print(datos)
                cur = db.cursor()
                consulta2 = "INSERT INTO ClienteEmpresarial (CUIRL,NombreEmpresa,NombreComercial, PNombreRL, SNombreRL, PApellidoRL, SApellidoRL, Ubicacion, NTelefonico, tipo_usuario, Tipo_Empresa) values("+cui+",'"+nempresa+"','"+ncomercial+"','"+pnombre+"','"+snombre+"','"+pallido+"','"+sallido+"','"+ubicacion+"',"+ntel+", 'Empresarial','"+typempresa+"')"
                cur.execute(consulta2)
                db.commit()
                cur.close()
                # Segunda consulta
                cur5 = db.cursor()
                consulta3 = "select IdClienteEm from ClienteEmpresarial where CUIRL = " + cui + ""
                cur5.execute(consulta3)
                row = cur5.fetchone()
                val = row[0]
                print(val)
                print(type(val))
                cur5.close()
                # Tercer consulta
                cur1 = db.cursor()
                data = [us, con, 'Individual', val]
                print(type(us))
                print(us)
                print(type(con))
                print(type(val))
                consulta9 = "insert into Cliente(CodigoIngreso,ClaveA, tipo_usuario, IdClienteEm) values ('" + str(us) + "' , '" + str(con) + "', 'Empresarial' , " + str(val) + ")"
                cur1.execute(consulta9)
                db.commit()
                # row = cur.fetchone()
                print(cur1)
                # print(row)
                cur1.close()

                nombre = "Cliente Registrado"
                # form.save()
                form = ClienteEmpresarial()
                variables = {
                    "form": form,
                    "mensaje": nombre
                }
                return render(request, 'InicioAdmin.html', variables)
            except:
                form.clean()
                variables = {
                    "form": form.full_clean()
                }
                return render(request, 'RegistroClientesEm.html', variables)
        else:
            form.clean()
            variables = {
                "form": form.full_clean()
            }

    return render(request, 'RegistroClientesEm.html', variables)

def CuentaM(request):
    # Obtener el idCliente General
    curId = db.cursor()
    consulta26 = "select idCliente from Cliente where tipo_usuario != 'Administrador'"
    curId.execute(consulta26)
    listId = []
    for i in curId:
        for k in i:
            listId.append(k)
    curId.close()
    # Obtener el codigo de Ingreso
    curCI = db.cursor()
    consul = "select CodigoIngreso from Cliente where tipo_usuario != 'Administrador'"
    curCI.execute(consul)
    listCI = []
    for i in curCI:
        for k in i:
            listCI.append(k)
    curCI.close()

    d = dict(zip(listId, listCI))

    list2 = [(0, 'Seleccione una Opcion')]
    for a in d:
        list2.append((a, d[a]))
    print(list2)
    form = CrearCuentaMo()
    form.fields['cuentas'].choices = list2
    print(form.fields['cuentas'].choices)
    variables = {
        "form": form
    }
    if request.method == "POST":
        form = CrearCuentaMo(data=request.POST)
        print(form.data)

        if form.is_valid():
            datos = form.cleaned_data
            cuentas = datos.get("cuentas")
            moneda = datos.get("moneda")
            Pre = datos.get("Preauto")
            print(cuentas)
            print(moneda)
            print(Pre)
            # Primer Consulta
            cur = db.cursor()
            consulta2 = "insert into Cuenta(Saldo, Estado, TipoMoneda, TipoCuenta, PreAuto, idCliente, CodigoChe) values (0.00, 'Activo', '"+ moneda +"', 'Monetaria', '"+Pre+"', "+cuentas+", 0)"
            cur.execute(consulta2)
            db.commit()
            cur.close()
            form = CrearCuentaMo()
            form.fields['cuentas'].choices = list2
            variables = {
                "form": form
            }
            return render(request, 'InicioAdmin.html', variables)
        else:
            form.fields['cuentas'].choices = list2
            variables = {
                "form": form
            }

    return render(request, 'CuentaMonetaria.html', variables)

def CuentaA(request):
    # Obtener el idCliente General
    curId = db.cursor()
    consulta26 = "select idCliente from Cliente where tipo_usuario != 'Administrador'"
    curId.execute(consulta26)
    listId = []
    for i in curId:
        for k in i:
            listId.append(k)
    curId.close()
    # Obtener el codigo de Ingreso
    curCI = db.cursor()
    consul = "select CodigoIngreso from Cliente where tipo_usuario != 'Administrador'"
    curCI.execute(consul)
    listCI = []
    for i in curCI:
        for k in i:
            listCI.append(k)
    curCI.close()

    d = dict(zip(listId, listCI))

    list2 = [(0, 'Seleccione una Opcion')]
    for a in d:
        list2.append((a, d[a]))
    print(list2)
    form = CrearCuentaAho()
    form.fields['cuentas'].choices = list2
    print(form.fields['cuentas'].choices)
    variables = {
        "form": form
    }
    if request.method == "POST":
        form = CrearCuentaAho(data=request.POST)
        print(form.data)

        if form.is_valid():
            datos = form.cleaned_data
            cuentas = datos.get("cuentas")
            moneda = datos.get("moneda")
            Pre = datos.get("preauto")
            interes = datos.get("interes")
            print(cuentas)
            print(moneda)
            print(Pre)
            indec = int(interes)/100
            # Primer Consulta
            cur = db.cursor()
            consulta2 = "insert into Cuenta(Saldo, Estado, TipoMoneda, TipoCuenta, PreAuto, idCliente, Interes, CodigoChe) values (0.00, 'Activo', '" + moneda + "', 'Ahorro', '" + Pre + "', " + cuentas + ", "+str(indec)+", 0)"
            cur.execute(consulta2)
            db.commit()
            cur.close()
            form = CrearCuentaAho()
            form.fields['cuentas'].choices = list2
            variables = {
                "form": form
            }
            return render(request, 'InicioAdmin.html', variables)
        else:
            form.fields['cuentas'].choices = list2
            variables = {
                "form": form
            }

    return render(request, 'CuentaAhorro.html', variables)

def CuentaPF(request):
    # Obtener el idCliente General
    curId = db.cursor()
    consulta26 = "select idCliente from Cliente where tipo_usuario != 'Administrador'"
    curId.execute(consulta26)
    listId = []
    for i in curId:
        for k in i:
            listId.append(k)
    curId.close()
    # Obtener el codigo de Ingreso
    curCI = db.cursor()
    consul = "select CodigoIngreso from Cliente where tipo_usuario != 'Administrador'"
    curCI.execute(consul)
    listCI = []
    for i in curCI:
        for k in i:
            listCI.append(k)
    curCI.close()

    d = dict(zip(listId, listCI))

    list2 = [(0, 'Seleccione una Opcion')]
    for a in d:
        list2.append((a, d[a]))
    print(list2)
    form = CrearCuentaPF()
    form.fields['cuentas'].choices = list2
    print(form.fields['cuentas'].choices)
    variables = {
        "form": form
    }
    if request.method == "POST":
        form = CrearCuentaPF(data=request.POST)
        print(form.data)

        if form.is_valid():
            datos = form.cleaned_data
            cuentas = datos.get("cuentas")
            moneda = datos.get("moneda")
            Pre = datos.get("Preauto")
            interes = datos.get("interes")
            tiempo = datos.get("tiempo")
            print(cuentas)
            print(moneda)
            print(Pre)
            indec = int(interes) / 100
            # Primer Consulta
            cur = db.cursor()
            consulta2 = "insert into Cuenta(Saldo, Estado, TipoMoneda, TipoCuenta, idCliente, Interes, Tiempo, CodigoChe) values (0.00, 'Activo', '" + moneda + "', 'Plazo Fijo', " + cuentas + ", " + +str(indec) + ", "+tiempo+", 0)"
            cur.execute(consulta2)
            db.commit()
            cur.close()
            form = CrearCuentaPF()
            form.fields['cuentas'].choices = list2
            variables = {
                "form": form
            }
            return render(request, 'InicioAdmin.html', variables)
        else:
            form.fields['cuentas'].choices = list2
            variables = {
                "form": form
            }

    return render(request, 'CuentaPlazo.html', variables)

def CrearChequera(request):
    # Obtener el idCliente General
    curId = db.cursor()
    consulta26 = "select CodigoCuenta from Cuenta where CodigoChe = 0 and Estado = 'Activo';"
    curId.execute(consulta26)
    listId = []
    for i in curId:
        for k in i:
            listId.append(k)
    curId.close()
    # Obtener el codigo de Ingreso
    curCI = db.cursor()
    consul = "select CodigoCuenta from Cuenta where CodigoChe = 0 and Estado = 'Activo';"
    curCI.execute(consul)
    listCI = []
    for i in curCI:
        for k in i:
            listCI.append(k)
    curCI.close()

    d = dict(zip(listId, listCI))

    list2 = [(0, 'Seleccione una Opcion')]
    for a in d:
        list2.append((a, d[a]))
    print(list2)
    form = Chequera()
    form.fields['cuentas'].choices = list2
    print(form.fields['cuentas'].choices)
    variables = {
        "form": form
    }
    if request.method == "POST":
        form = Chequera(data=request.POST)
        print(form.data)

        if form.is_valid():
            datos = form.cleaned_data
            cuentas = datos.get("cuentas")
            print(cuentas)
            # Primer Consulta
            cur = db.cursor()
            consulta2 = "insert into Chequera (DispoCheque, CodigoCuenta) values(10, "+cuentas+")"
            cur.execute(consulta2)
            db.commit()
            cur.close()
            #Seleccionar numero de cuenta creada
            curCI = db.cursor()
            consul = "select CodigoChe from Chequera where CodigoCuenta = "+cuentas+""
            curCI.execute(consul)
            row = curCI.fetchone()
            val = row[0]
            #Actualizar Cuenta
            cur2 = db.cursor()
            consulta3 = "update Cuenta set CodigoChe = "+cuentas+" where CodigoCuenta = "+val+""
            cur2.execute(consulta3)
            db.commit()
            cur2.close()
            form = Chequera()
            form.fields['cuentas'].choices = list2
            variables = {
                "form": form
            }
            return render(request, 'InicioAdmin.html', variables)
        else:
            form.fields['cuentas'].choices = list2
            variables = {
                "form": form
            }

    return render(request, 'CrearCh.html', variables)





def Cobrar(request):
    variables = {

    }

    return render(request, 'CrearCh.html', variables)

def Depositos(request):

    variables = {

    }


    return render(request, 'Depositos.html', variables)

def Desbloqueo(Request):
    return render(Request,"Desbloqueo.html")