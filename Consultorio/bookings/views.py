from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva


# Create your views here.

def home_view(request):
    return HttpResponse("<h3>Bienvenidos a la home de reservas 'Bookings'</h3>")

def list_view(request):
    reservas = Reserva.objects.all()
    contexto_dict = {'reservas': reservas}
    return render(request, "list.html", contexto_dict)

def search_view(request, nombre_de_usuario):

    return HttpResponse(f"Has pedido buscar las reservas de {nombre_de_usuario}")


def create_view(request, nombre_de_usuario, consultorio):

#   reserva = Reserva("",nombre_de_usuario, consultorio) -- esta forma no se utiliza en django, se utiliza la de abajo
    reserva = Reserva.objects.create(nombre_de_usuario = nombre_de_usuario,consultorio = consultorio)
    return HttpResponse(f"He creado {reserva}")