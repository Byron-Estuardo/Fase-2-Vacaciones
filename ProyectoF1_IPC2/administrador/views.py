from django.shortcuts import render

# Create your views here.

def Registro_view(Request):
    return render(Request,"RegistroClientes.html")