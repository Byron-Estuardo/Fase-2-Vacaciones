from .forms import *
from django.shortcuts import render
from .forms import *
from django.db import connection
import MySQLdb

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

def Principal_view(request):
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
            print(usuario)
            print(clave)
            cur = db.cursor()
            consulta2 = "select idCliente from Cliente where CodigoIngreso = '" + usuario + "' and ClaveA = '" + clave + "'"
            cur.execute(consulta2)
            row = cur.fetchone()
            if row is not None:
                idClienteIngresado = row[0]
                print(idClienteIngresado)
                return render(request, "Inicio.html", variables)
            else:
                print('no jalo')
                return render(request, "Login.html", variables)
            db.close()
            form = InicioSesion()
            variables = {
                "form": form
            }
            return render(request, "Inicio.html", variables)
        else:
            form.clean()
            variables = {
                "form": form.full_clean()
            }
    return render(request, "Login.html", variables)




def Inicio_view(request):
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
                if tipo != 'Administrador':

                    return render(request, "Inicio.html", variables)
                else:
                    print('Wacho que no salio')
                    return render(request, "Login.html", variables)
            else:
                print('no jalo')
                return render(request, "Login.html", variables)
            db.close()
            form = InicioSesion()
            variables = {
                "form": form
            }
            return render(request, "Inicio.html", variables)
        else:
            form.clean()
            variables = {
                "form": form.full_clean()
            }
    return render(request, "Login.html", variables)

def TCP_view(Request):
    return render(Request,"TCP.html")

def TCT_view(Request):
    return render(Request,"TCT.html")

def Pre_view(Request):
    return render(Request,"Pre-Cheques.html")

def PS_view(Request):
    return render(Request,"PS.html")

def PP_view(Request):
    return render(Request,"PP.html")

def SPresta_view(Request):
    return render(Request,"SPresta.html")

def Usuario_view(Request):
    return render(Request,"Usuario.html")

def Suspender_view(request):
    # Obtener el idCliente General
    curId = db.cursor()
    consulta26 = "select Cuenta from Cliente where id = 'Bloqueado'"
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
        consulta2 = "update Cliente set ClaveA = '" + nuevacon + "', Estado = 'Activo' where idCliente = " + cuentas + ""
        cur.execute(consulta2)
        db.commit()
        cur.close()
        variables = {
            "listId": listId
        }
        return render(request, 'InicioAdmin.html', variables)

    return render(request, "Desbloqueo.html", variables)
    return render(request,"Susp.html", variables)

def Reactivar_view(request):
    return render(request,"Reactivar.html")