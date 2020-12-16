from django.http import HttpResponse
from django.shortcuts import render

# First view

def Principal_view(Request):
    return render(Request,"Login.html")

def Registro_view(Request):
    return render(Request,"RegistroClientes.html")

def Inicio_view(Request):
    return render(Request,"Inicio.html")

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

def Suspender_view(Request):
    return render(Request,"Susp.html")

def Reactivar_view(Request):
    return render(Request,"Reactivar.html")