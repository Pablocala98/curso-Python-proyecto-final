from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reserva, Consultorio
from .forms import ConsultorioCreateForm, ReservaSearchForm, ReservaCreateForm, ConsultorioSearchForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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
    if request.method == "GET":
        form = ReservaCreateForm()
        contexto = {"create_booking_form":form}
        return render(request,"bookings/form-create-booking.html", contexto)
    elif request.method == "POST":
        form = ReservaCreateForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
            consultorio = form.cleaned_data['consultorio']
            fecha = form.cleaned_data['fecha']
            hora = form.cleaned_data['hora']
            duracion = form.cleaned_data['duracion']
            descripcion = form.cleaned_data['descripcion']
            nueva_reserva = Reserva(nombre_de_usuario = nombre_de_usuario, consultorio = consultorio, fecha = fecha, hora = hora, duracion = duracion, descripcion = descripcion)
            nueva_reserva.save()
            return detail_booking_view(request,nueva_reserva.id)

def consulting_room_list_view(request):
    consultorio = Consultorio.objects.all() #con este Reserva.objects.all() nos trae todos los objetos reserva de la base de datos
    contexto_dict = {'consultorios': consultorio}
    return render(request, "bookings/consulting_rooms_list.html", contexto_dict)

def consulting_room_delete_view(request, consulting_room_id):
    consultorio_a_borrar = Consultorio.objects.filter(id=consulting_room_id).first()
    consultorio_a_borrar.delete()
    return redirect("consultorio-list")

def delete_booking_view(request, booking_id):
    reserva_a_borrar = Reserva.objects.filter(id=booking_id).first()
    reserva_a_borrar.delete()
    return redirect("bookings-list")

def consulting_room_update_view(request, consulting_room_id):

    consultorio_a_editar = Consultorio.objects.filter(id=consulting_room_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "nombre": consultorio_a_editar.nombre,              #argument error, no me aparece en azul
            "disponible": consultorio_a_editar.disponible,
            "capacidad": consultorio_a_editar.capacidad,
            "descripcion": consultorio_a_editar.descripcion
            }
        formulario = ConsultorioCreateForm(initial=valores_iniciales)
        contexto_dict = {
            "form_update" : formulario,
            "OBJETO": consultorio_a_editar  
            }
        return render(request, "bookings/form-update.html", contexto_dict)
    elif request.method == "POST":
        form = ConsultorioCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            disponible = form.cleaned_data['disponible']
            capacidad = form.cleaned_data['capacidad']
            descripcion = form.cleaned_data['descripcion']
            consultorio_a_editar.nombre = nombre
            consultorio_a_editar.disponible = disponible
            consultorio_a_editar.capacidad = capacidad
            consultorio_a_editar.descripcion = descripcion
            consultorio_a_editar.save()
            return redirect("consultorio-detail", consultorio_a_editar.id)
        
def consulting_room_search_view(request):
    if request.method == "GET":
        form = ConsultorioSearchForm()
        return render(request,"bookings/form-search-consulting-room.html", context = {"search_form":form})
    elif request.method == "POST":
        form = ConsultorioSearchForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            consultorio = Consultorio.objects.filter(nombre = nombre).all()
            contexto_dict = {'consultorios': consultorio}
            return render(request, "bookings/consulting_rooms_list.html", contexto_dict)
        
class ConsultorioListView(ListView):
    model = Consultorio
    template_name = "bookings/VBC/vbc-consultorio-list.html"
    context_object_name = "consultorios"

class ConsultorioDetailView(DetailView):
    model = Consultorio
    template_name = "bookings/VBC/vbc-consultorio-detail.html"
    context_object_name = "consultorio"

class ConsultorioCreateView(CreateView):
    model = Consultorio
    template_name = "bookings/VBC/vbc-consultorio-create.html"
    fields = ['nombre', 'disponible', 'capacidad', 'descripcion']
    success_url = reverse_lazy("vbc-consultorio-list")

class ConsultorioDeleteView(DeleteView):
    model = Consultorio
    template_name = "bookings/VBC/vbc-consultorio-delete.html"
    success_url = reverse_lazy("vbc-consultorio-list")

class ConsultorioUpdateView(UpdateView):
    model = Consultorio
    template_name = "bookings/VBC/vbc-consultorio-update.html"
    fields = ['nombre', 'disponible', 'capacidad', 'descripcion']
    success_url = reverse_lazy("vbc-consultorio-list")
    