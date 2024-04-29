from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reserva, Consultorio, Masajista, Avatar
from .forms import ConsultorioCreateForm, ReservaSearchForm, ReservaCreateForm, ConsultorioSearchForm, MasajistaCreateForm, MasajistaSearchForm, AvatarCreateForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import UserEditForm

# Create your views here.

def home_view(request):
    return render(request, "bookings/home.html")

@login_required
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
            reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario__icontains = nombre_de_usuario).all()
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

@login_required
def consulting_room_list_view(request):
    consultorio = Consultorio.objects.all() #con este Reserva.objects.all() nos trae todos los objetos reserva de la base de datos
    contexto_dict = {'consultorios': consultorio}
    return render(request, "bookings/consulting-rooms-list.html", contexto_dict)

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
            "nombre": consultorio_a_editar.nombre,
            "disponible": consultorio_a_editar.disponible,
            "capacidad": consultorio_a_editar.capacidad,
            "descripcion": consultorio_a_editar.descripcion
            }
        formulario = ConsultorioCreateForm(initial=valores_iniciales)
        contexto_dict = {
            "form_update" : formulario,
            "OBJETO": consultorio_a_editar  
            }
        return render(request, "bookings/form-update-consulting-room.html", contexto_dict)
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
            descartar_no_disponibles = form.cleaned_data['disponible']
            if descartar_no_disponibles:
                consultorio = Consultorio.objects.filter(nombre__icontains = nombre, disponible = True).all()
            else:
                consultorio = Consultorio.objects.filter(nombre__icontains = nombre).all()
            contexto_dict = {'consultorios': consultorio}
            return render(request, "bookings/consulting-rooms-list.html", contexto_dict)
class ConsultorioListView(LoginRequiredMixin,ListView):
    model = Consultorio
    template_name = "bookings/VBC/vbc-consultorio-list.html"
    context_object_name = "consultorios"
class ConsultorioDetailView(LoginRequiredMixin,DetailView):
    model = Consultorio
    template_name = "bookings/VBC/vbc-consultorio-detail.html"
    context_object_name = "consultorio"

class ConsultorioCreateView(LoginRequiredMixin, CreateView):
    model = Consultorio
    template_name = "bookings/VBC/vbc-consultorio-create.html"
    fields = ['nombre', 'disponible', 'capacidad', 'descripcion']
    success_url = reverse_lazy("vbc-consultorio-list")

class ConsultorioDeleteView(LoginRequiredMixin, DeleteView):
    model = Consultorio
    template_name = "bookings/VBC/vbc-consultorio-delete.html"
    success_url = reverse_lazy("vbc-consultorio-list")

class ConsultorioUpdateView(LoginRequiredMixin, UpdateView):
    model = Consultorio
    template_name = "bookings/VBC/vbc-consultorio-update.html"
    fields = ['nombre', 'disponible', 'capacidad', 'descripcion']
    success_url = reverse_lazy("vbc-consultorio-list")

def therapist_list_view(request):
    masajista = Masajista.objects.all()
    contexto = {'masajistas': masajista}
    return render(request, "bookings/therapist-list.html", contexto)

def update_booking_view(request, booking_id):
    reserva_a_editar = Reserva.objects.filter(id=booking_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "nombre_de_usuario": reserva_a_editar.nombre_de_usuario,              #argument error, no me aparece en azul
            "consultorio": reserva_a_editar.consultorio,
            "fecha": reserva_a_editar.fecha,
            "hora": reserva_a_editar.hora,
            "duracion": reserva_a_editar.duracion,
            "descripcion": reserva_a_editar.descripcion
            }
        formulario = ReservaCreateForm(initial=valores_iniciales)
        contexto_dict = {
            "form_update" : formulario,
            "OBJETO": reserva_a_editar  
            }
        return render(request, "bookings/form-update-booking.html", contexto_dict)
    elif request.method == "POST":
        form = ReservaCreateForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
            consultorio = form.cleaned_data['consultorio']
            fecha = form.cleaned_data['fecha']
            hora = form.cleaned_data['hora']
            duracion = form.cleaned_data['duracion']
            descripcion = form.cleaned_data['descripcion']
            reserva_a_editar.nombre_de_usuario = nombre_de_usuario
            reserva_a_editar.consultorio = consultorio
            reserva_a_editar.fecha = fecha
            reserva_a_editar.hora = hora
            reserva_a_editar.duracion = duracion
            reserva_a_editar.descripcion = descripcion
            reserva_a_editar.save()
            return redirect("booking-detail", reserva_a_editar.id)

def create_therapist_with_form_view(request):
    if request.method == "GET":
        form = MasajistaCreateForm()
        contexto = {"masajista_create_form":form}
        return render(request,"bookings/form-create-therapist.html", contexto)
    elif request.method == "POST":
        form = MasajistaCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            documento = form.cleaned_data['documento']
            telefono = form.cleaned_data['telefono']
            nuevo_masajista = Masajista(nombre = nombre, apellido = apellido, documento = documento, telefono = telefono)
            nuevo_masajista.save()
            return detail_therapist_view(request,nuevo_masajista.id) #corregir el detail_consulting_room_view
        
def detail_therapist_view(request, therapist_id):
    masajista = Masajista.objects.get(id=therapist_id)
    contexto_dict = {"masajista" : masajista}
    return render(request, "bookings/detail-therapist.html", contexto_dict)

def update_therapist_view(request,therapist_id):
    masajista_a_editar = Masajista.objects.filter(id=therapist_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "nombre": masajista_a_editar.nombre,              
            "apellido": masajista_a_editar.apellido,
            "documento": masajista_a_editar.documento,
            "telefono": masajista_a_editar.telefono
            }
        formulario = MasajistaCreateForm(initial=valores_iniciales)
        contexto_dict = {
            "form_update" : formulario,
            "OBJETO": masajista_a_editar  
            }
        return render(request, "bookings/form-update-therapist.html", contexto_dict)
    elif request.method == "POST":
        form = MasajistaCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            documento = form.cleaned_data['documento']
            telefono = form.cleaned_data['telefono']
            masajista_a_editar.nombre = nombre
            masajista_a_editar.apellido = apellido
            masajista_a_editar.documento = documento
            masajista_a_editar.telefono = telefono
            masajista_a_editar.save()
            return redirect("masajista-detail", masajista_a_editar.id)

class MasajistaDeleteView(LoginRequiredMixin, DeleteView):
    model = Masajista
    template_name = "bookings/therapist-delete.html"
    success_url = reverse_lazy("masajista-list")

def therapist_search_view(request):
    if request.method == "GET":
        form = MasajistaSearchForm()
        return render(request,"bookings/form-search-therapist.html", context = {"search_form":form})
    elif request.method == "POST":
        form = MasajistaSearchForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            masajista = Masajista.objects.filter(nombre = nombre).all()
            contexto_dict = {'masajistas': masajista}
            return render(request, "bookings/therapist-list.html", contexto_dict)
        

def user_logout_view(request):
    logout(request)
    return redirect('login')

def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request,user)
                return redirect('home')

    return render(request, 'bookings/login.html', {'form':form})

def user_creation_view(request):
    if request.method == "GET":
        form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    return render(request, "bookings/create-user.html", {"form": form})
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = "bookings/form-edit-profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user


def avatar_view(request):
    if request.method == "GET":
        contexto = {"form" : AvatarCreateForm()}
    else:
        form = AvatarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            avatar_existente = Avatar.objects.filter(user = request.user)
            avatar_existente.delete()
            nuevo_avatar = Avatar(image=image, user = request.user)
            nuevo_avatar.save()
            return redirect("home")
        else:
            contexto = {"form": form}
    
    return render(request, "bookings/avatar-create.html", context= contexto)

def about_me_view(request):
    return render(request, "bookings/about-me.html")