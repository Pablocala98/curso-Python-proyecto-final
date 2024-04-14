from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva, Consultorio
from .forms import ConsultorioCreateForm, ReservaSearchForm, ReservaCreateForm


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

def detail_booking_view(request, booking_id):
    reserva = Reserva.objects.get(id=booking_id)
    contexto_dict = {"reserva" : reserva}
    return render(request, "bookings/detail-booking.html", contexto_dict)

def detail_consulting_room_view(request, consulting_room_id):
    consultorio = Consultorio.objects.get(id=consulting_room_id)
    contexto_dict = {"consultorio" : consultorio}
    return render(request, "bookings/detail-consulting-room.html", contexto_dict)

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
        
def create_consulting_room_with_form_view(request):
    if request.method == "GET":
        form = ConsultorioCreateForm()
        contexto = {"create_consulting_room_form":form}
        return render(request,"bookings/form-create-consulting-room.html", contexto)
    elif request.method == "POST":
        form = ConsultorioCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            disponible = form.cleaned_data['disponible']
            capacidad = form.cleaned_data['capacidad']
            descripcion = form.cleaned_data['descripcion']
            nuevo_consultorio = Consultorio(nombre = nombre, disponible = disponible, capacidad = capacidad, descripcion = descripcion)
            nuevo_consultorio.save()
            return detail_consulting_room_view(request,nuevo_consultorio.id)
        
def create_booking_with_form_view(request):
    form = ReservaCreateForm()
    contexto = {"create_booking_form":form}
    return render(request,"bookings/form-create-booking.html", contexto)
