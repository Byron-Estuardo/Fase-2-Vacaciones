import random
import string
import MySQLdb
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.db import connection
from .forms import *
from .models import *
from django.db.models import Q



host = 'localhost'
db_name = 'xd'
user = 'root'
contra = 'byron14112305'
puerto = 3306
idClienteIngresado = ''
# Conexion base de datos
db = MySQLdb.connect(
    host=host,
    user=user,
    password=contra,
    db=db_name
              )
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
                consulta9 = "insert into Cliente(CodigoIngreso,ClaveA, tipo_usuario, IdClienteIn, Estado) values ('"+str(us)+"' , '"+str(con)+"', 'Individual' , "+ str(val) +", 'Activo')"
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
                consulta9 = "insert into Cliente(CodigoIngreso,ClaveA, tipo_usuario, IdClienteEm, Estado) values ('" + str(us) + "' , '" + str(con) + "', 'Empresarial' , " + str(val) + ", 'Activo')"
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


    form = CrearCuentaMo()
    # Obtener el idCliente General
    curId = db.cursor()
    consulta26 = "select idCliente from Cliente where tipo_usuario != 'Administrador'"
    curId.execute(consulta26)
    listId = []
    for i in curId:
        for k in i:
            listId.append(k)
    curId.close()
    print(listId)
    # Obtener el codigo de Ingreso
    curCI = db.cursor()
    consul = "select CodigoIngreso from Cliente where tipo_usuario != 'Administrador'"
    curCI.execute(consul)
    listCI = []
    for i in curCI:
        for k in i:
            listCI.append(k)
    curCI.close()
    variables = {
        "form": form,
        "listId": listId,
        "listCI": listCI
    }

    if request.method == "POST":



        form = CrearCuentaMo(data=request.POST)
        datos = form.data
        print(datos)
        cuentas = request.POST.get("cuenta")
        moneda = datos.get("moneda")
        Pre = datos.get("preauto")
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
        variables = {
                "form": form
                ,
                "listId": listId
        }
        return render(request, 'InicioAdmin.html', variables)


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

    form = CrearCuentaAho()
    variables = {
        "form": form
        ,
        "listId": listId
    }
    if request.method == "POST":
        form = CrearCuentaAho(data=request.POST)
        print(form.data)

        if form.is_valid():
            datos = form.cleaned_data
            cuentas = request.POST.get("cuenta")
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
            variables = {
                "form": form
                ,
                "listId": listId
            }
            return render(request, 'InicioAdmin.html', variables)
        else:
            variables = {
                "form": form
                ,
                "listId": listId
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

    form = CrearCuentaPF()
    variables = {
        "form": form
        ,
        "listId": listId
    }
    if request.method == "POST":
        form = CrearCuentaPF(data=request.POST)
        print(form.data)

        if form.is_valid():
            datos = form.cleaned_data
            cuentas = request.POST.get("cuenta")
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
            consulta2 = "insert into Cuenta(Saldo, Estado, TipoMoneda, TipoCuenta, idCliente, Interes, Tiempo, CodigoChe) values (0.00, 'Activo', '" + moneda + "', 'Plazo Fijo', " + cuentas + ", " + str(indec) + ", "+tiempo+", 0)"
            cur.execute(consulta2)
            db.commit()
            cur.close()
            form = CrearCuentaPF()
            variables = {
                "form": form
                ,
                "listId": listId
            }

            return render(request, 'InicioAdmin.html', variables)
        else:
            variables = {
                "form": form
                ,
                "listId": listId
            }

    return render(request, 'CuentaPlazo.html', variables)


def CrearChequera(request):
    # Obtener el idCliente General
    curId = db.cursor()
    consulta26 = "select CodigoCuenta from Cuenta where CodigoChe = 0 and Estado = 'Activo'"
    curId.execute(consulta26)
    listId = []
    for i in curId:
        for k in i:
            listId.append(k)
    curId.close()

    variables = {
        "listId": listId
    }
    if request.method == "POST":
            cuentas = request.POST.get("cuenta")
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
            curCI.close()
            #Actualizar Cuenta
            cur2 = db.cursor()
            consulta3 = "update Cuenta set CodigoChe = "+cuentas+" where CodigoCuenta = "+str(val)+""
            cur2.execute(consulta3)
            db.commit()
            cur2.close()
            form = Chequera()
            variables = {
                "listId": listId
            }
            return render(request, 'InicioAdmin.html', variables)

    return render(request, 'CrearCh.html', variables)


def Depositoss(request):
    # Obtener el idCliente General
    curId = db.cursor()
    consulta26 = "select CodigoCuenta from Cuenta where Estado = 'Activo'"
    curId.execute(consulta26)
    listId = []
    for i in curId:
        for k in i:
            listId.append(k)
    curId.close()

    form = Depositos()
    variables = {
        "form": form
        ,
        "listId": listId
    }
    if request.method == "POST":
        form = Depositos(data=request.POST)
        print(form.data)

        if form.is_valid():
            datos = form.cleaned_data
            monto = datos.get("monto")
            descrip = datos.get("Descripcion")
            cuentas = request.POST.get("cuenta")
            monedas = datos.get("moneda")
            dolaraquetzal = 7.60
            quetzaladolar = 7.87

            # Seleccionar Tipo de Moneda
            cursor = db.cursor()
            c = "select TipoMoneda from Cuenta where CodigoCuenta = " + cuentas + ""
            cursor.execute(c)
            row = cursor.fetchone()
            moneda = row[0]
            cursor.close()

            # Seleccionar saldo de cuenta
            cursor = db.cursor()
            c = "select TipoCuenta from Cuenta where CodigoCuenta = " + cuentas + ""
            cursor.execute(c)
            row = cursor.fetchone()
            tipo = row[0]
            cursor.close()
            if tipo == 'Monetaria':
                print(cuentas)
                # Primer insert
                cur = db.cursor()
                consulta2 = "insert into Deposito (monto, Descripcion, CodigoCuenta) values (" + str(monto) + ", '" + descrip + "' , " + cuentas + ")"
                cur.execute(consulta2)
                db.commit()
                cur.close()
                # Seleccionar saldo de cuenta
                curCI = db.cursor()
                consul = "select saldo from Cuenta where CodigoCuenta = " + cuentas + ""
                curCI.execute(consul)
                row = curCI.fetchone()
                val = row[0]
                if moneda == monedas:
                    agregarSaldo = float(val) + float(monto)
                    print('Q')
                elif monedas == 'Q' and moneda == '$':
                    conver = float(monto) * quetzaladolar
                    agregarSaldo = float(val) + conver
                    print('$')
                elif monedas == '$' and moneda == 'Q':
                    conver = float(monto) * dolaraquetzal
                    agregarSaldo = float(val) + conver
                    print('$')
                curCI.close()
                # Actualizar Cuenta
                cur2 = db.cursor()
                consulta3 = "update Cuenta set saldo = " + str(agregarSaldo) + " where CodigoCuenta = " + cuentas + ""
                cur2.execute(consulta3)
                db.commit()
                cur2.close()
                form = Depositos()
                variables = {
                    "form": form
                    ,
                    "listId": listId
                }
                return render(request, 'InicioAdmin.html', variables)
            elif tipo == 'Plazo Fijo':
                print(cuentas)
                #Primer Deposito
                # Primer insert
                cur = db.cursor()
                consulta2 = "insert into Deposito (monto, Descripcion, CodigoCuenta) values (" + str(monto) + ", '" + descrip + "' , " + cuentas + ")"
                cur.execute(consulta2)
                db.commit()
                cur.close()
                # Seleccionar saldo de cuenta
                curCI = db.cursor()
                consul = "select saldo from Cuenta where CodigoCuenta = " + cuentas + ""
                curCI.execute(consul)
                row = curCI.fetchone()
                val = row[0]
                conver = 0;
                if moneda == monedas:
                    agregarSaldo = float(val) + float(monto)
                    print('Q')
                elif monedas == 'Q' and moneda == '$':
                    conver = float(monto) * quetzaladolar
                    agregarSaldo = float(val) + conver
                    print('$')
                elif monedas == '$' and moneda == 'Q':
                    conver = float(monto) * dolaraquetzal
                    agregarSaldo = float(val) + conver
                    print('$')
                curCI.close()
                cur2 = db.cursor()
                # Actualizar Cuenta
                consulta3 = "update Cuenta set saldo = " + str(agregarSaldo) + " where CodigoCuenta = " + cuentas + ""
                cur2.execute(consulta3)
                db.commit()
                cur2.close()

                # Obtener Interes
                curCI = db.cursor()
                consul = "select Interes from Cuenta where CodigoCuenta = " + cuentas + ""
                curCI.execute(consul)
                row = curCI.fetchone()
                I = row[0]
                curCI.close()

                #Intereses
                # Primer insert
                interes = float(conver) * float(I)
                cur = db.cursor()
                consulta2 = "insert into Deposito (monto, Descripcion, CodigoCuenta) values (" + str(interes) + ", 'Intereses' , " + cuentas + ")"
                cur.execute(consulta2)
                db.commit()
                cur.close()
                # Seleccionar saldo de cuenta
                curCI = db.cursor()
                consul = "select saldo from Cuenta where CodigoCuenta = " + cuentas + ""
                curCI.execute(consul)
                row = curCI.fetchone()
                val = row[0]
                agregarSaldo = float(val) + float(interes)
                cur2 = db.cursor()
                # Actualizar Cuenta
                consulta3 = "update Cuenta set saldo = " + str(agregarSaldo) + " where CodigoCuenta = " + cuentas + ""
                cur2.execute(consulta3)
                db.commit()
                cur2.close()

                form = Depositos()
                variables = {
                    "form": form
                    ,
                    "listId": listId
                }
                return render(request, 'InicioAdmin.html', variables)
            elif tipo == 'Ahorro':
                print(cuentas)
                # Primer Deposito
                # Primer insert
                cur = db.cursor()
                consulta2 = "insert into Deposito (monto, Descripcion, CodigoCuenta) values (" + str(monto) + ", '" + descrip + "' , " + cuentas + ")"
                cur.execute(consulta2)
                db.commit()
                cur.close()
                # Seleccionar saldo de cuenta
                curCI = db.cursor()
                consul = "select saldo from Cuenta where CodigoCuenta = " + cuentas + ""
                curCI.execute(consul)
                row = curCI.fetchone()
                val = row[0]
                if moneda == monedas:
                    agregarSaldo = float(val) + float(monto)
                    print('Q')
                elif monedas == 'Q' and moneda == '$':
                    conver = float(monto) * quetzaladolar
                    agregarSaldo = float(val) + conver
                    print('$')
                elif monedas == '$' and moneda == 'Q':
                    conver = float(monto) * dolaraquetzal
                    agregarSaldo = float(val) + conver
                    print('$')
                curCI.close()
                cur2 = db.cursor()
                # Actualizar Cuenta
                consulta3 = "update Cuenta set saldo = " + str(agregarSaldo) + " where CodigoCuenta = " + cuentas + ""
                cur2.execute(consulta3)
                db.commit()
                cur2.close()

                # Obtener Interes
                curCI = db.cursor()
                consul = "select Interes from Cuenta where CodigoCuenta = " + cuentas + ""
                curCI.execute(consul)
                row = curCI.fetchone()
                I = row[0]
                curCI.close()

                # Intereses
                # Primer insert
                interes = float(conver) * float(I)
                cur = db.cursor()
                consulta2 = "insert into Deposito (monto, Descripcion, CodigoCuenta) values (" + str(interes) + ", 'Intereses' , " + cuentas + ")"
                cur.execute(consulta2)
                db.commit()
                cur.close()
                # Seleccionar saldo de cuenta
                curCI = db.cursor()
                consul = "select saldo from Cuenta where CodigoCuenta = " + cuentas + ""
                curCI.execute(consul)
                row = curCI.fetchone()
                val = row[0]
                agregarSaldo = float(val) + float(interes)
                cur2 = db.cursor()
                # Actualizar Cuenta
                consulta3 = "update Cuenta set saldo = " + str(agregarSaldo) + " where CodigoCuenta = " + cuentas + ""
                cur2.execute(consulta3)
                db.commit()
                cur2.close()

                form = Depositos()
                variables = {
                    "form": form
                    ,
                    "listId": listId
                }
                return render(request, 'InicioAdmin.html', variables)
        else:
            variables = {
                "form": form
                ,
                "listId": listId
            }
    return render(request, 'Depositos.html', variables)


def Desbloqueo(request):
    # Obtener el idCliente General
    curId = db.cursor()
    consulta26 = "select idCliente from Cliente where Estado = 'Bloqueado'"
    curId.execute(consulta26)
    listId = []
    for i in curId:
        for k in i:
            listId.append(k)
    curId.close()

    variables = {
        "listId": listId
    }
    if request.method == "POST":

            def gencon(chars=string.ascii_letters + string.digits + string.punctuation):
                return ''.join([random.choice(chars) for i in range(10)])
            nuevacon = gencon()
            cuentas = request.POST.get("cuenta")
            print(cuentas)
            # Primer Consulta
            cur = db.cursor()
            consulta2 = "update Cliente set ClaveA = '"+nuevacon+"', Estado = 'Activo' where idCliente = "+cuentas+""
            cur.execute(consulta2)
            db.commit()
            cur.close()
            variables = {
                "listId": listId
            }
            return render(request, 'InicioAdmin.html', variables)

    return render(request,"Desbloqueo.html", variables)


def Cobrar(request):

    variables = {

    }

    return render(request, 'CrearCh.html', variables)