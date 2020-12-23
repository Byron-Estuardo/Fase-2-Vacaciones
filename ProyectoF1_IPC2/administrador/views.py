import MySQLdb
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.db import connection
from .forms import *

host = 'localhost'
db_name = 'proyecto4'
user: str = 'root'
contra = 'byron14112305'
puerto = 3306
idClienteIngresado = ''

db = MySQLdb.connect(host=host,
                                 user=user,
                                 password=contra,
                                 db=db_name,
                                 connect_timeout = 5)
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
            db = MySQLdb.connect(host=host,
                                 user=user,
                                 password=contra,
                                 db=db_name)
            cur = db.cursor()
            consulta2 = "select idCliente, tipo_usuario from Cliente where CodigoIngreso = '" + usuario + "' and ClaveA = '" + clave + "'"
            cur.execute(consulta2)
            row = cur.fetchone()
            if row is not None:
                tipo = row[1]
                if tipo == 'Administrador':
                    idClienteIngresado = row[0]
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

    ins = 'Individual'
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
            val = 0
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
            print(type(user))
            print(type(con))
            print(datos)
            #Primer Consulta
            cur = db.cursor()
            consulta2 = "insert into ClienteIndividual(CUI, NIT, PNombre, SNombre, PApellido, SApellido, FNacimiento, CorreoE, NTelefonico, tipo_usuario)values(" + cui + ",'" + nit + "','" + pnombre + "','" + snombre + "','" + pallido + "','" + sallido + "','" + nacimiento + "','" + correoe + "'," + ntel + ", 'Individual')"
            cur.execute(consulta2)
            print(cur)
            db.commit()
            cur.close()
            #Segunda consulta
            cur5 = db.cursor()
            consulta3 = "select IdClienteIn from ClienteIndividual where CUI = " + cui + ""
            cur5.execute(consulta3)
            row = cur5.fetchone()
            val = row[0]
            print(val)
            print(type(val))
            cur5.close()
            #Tercer consulta
            cur1 = db.cursor()
            data = [us, con, 'Individual', val]
            print(type(us))
            print(us)
            print(type(con))
            print(type(val))
            print(type(ins))
            consulta9 = "insert into Cliente(CodigoIngreso,ClaveA, tipo_usuario, IdClienteIn) values ('"+us+"' , '"+con+"', 'Individual' , "+ str(val) +")"
            cur1.execute(consulta9)
            db.commit()
            # row = cur.fetchone()
            print(cur1)
            # print(row)
            cur1.close()
            form = ClienteIn()
            variables = {
                "form": form,
                "mensaje": nombre
            }
            return render(request, 'InicioAdmin.html', variables)
        else:
            form.clean()
            variables = {
                "form": form.full_clean()
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
            nombre = "Cliente Registrado"
            # form.save()
            form = ClienteEmpresarial()
            variables = {
                "form": form,
                "mensaje": nombre
            }
        else:
            form.clean()
            variables = {
                "form": form.full_clean()
            }

    return render(request, 'RegistroClientesEm.html', variables)

def CrearCuenta(Request):
    return render(Request, 'CrearCuentas.html')

def Depositos(Request):
    return render(Request, 'Depositos.html')

def Desbloqueo(Request):
    return render(Request,"Desbloqueo.html")