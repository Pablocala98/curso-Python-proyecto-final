from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva
from .forms import ReservaSearchForm


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

def detail_view(request, booking_id):
    reserva = Reserva.objects.get(id=booking_id)
    contexto_dict = {"reserva" : reserva}
    return render(request, "bookings/detail.html", contexto_dict)

def search_booking_with_form_view(request):
    if request.method == "GET":
        form = ReservaSearchForm()
        return render(request,"bookings/form-search-booking.html", context = {"search_form":form})
    elif request.method == "POST":
        form = ReservaSearchForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
            reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario = nombre_de_usuario).all()
            contexto_dict = {'reservas': reservas_del_usuario}
            return render(request, "bookings/list.html", contexto_dict)
