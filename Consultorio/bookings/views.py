from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva


# Create your views here.

def home_view(request):
    return render(request, "bookings/home.html")

def list_view(request):
    reservas = Reserva.objects.all() #con este Reserva.objects.all() nos trae todos los objetos reserva de la base de datos
    contexto_dict = {'reservas': reservas}
    return render(request, "bookings/list.html", contexto_dict)

def search_view(request, nombre_de_usuario):
    reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario = nombre_de_usuario).all() #con este Reserva.objects.filter() nos filtra todos los objetos reserva de la base de datos por lo que hay dentro del parentesis
    contexto_dict = {'reservas': reservas_del_usuario}
    return render(request, "bookings/list.html", contexto_dict)

def create_view(request, nombre_de_usuario, consultorio):
#   reserva = Reserva("",nombre_de_usuario, consultorio) -- esta forma no se utiliza en django, se utiliza la de abajo
    reserva = Reserva.objects.create(nombre_de_usuario = nombre_de_usuario,consultorio = consultorio)
    return HttpResponse(f"He creado {reserva}")

def detail_view(request, booking_id):
    reserva = Reserva.objects.get(id=booking_id)
    contexto_dict = {"reserva" : reserva}
    return render(request, "bookings/detail.html", contexto_dict)
