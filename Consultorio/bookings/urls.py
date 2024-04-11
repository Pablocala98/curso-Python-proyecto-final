from django.contrib import admin
from django.urls import path
from .views import home_view, list_view, search_view, detail_view, search_booking_with_form_view



urlpatterns = [
    path("", home_view),
    path("detail/<booking_id>", detail_view ),
    path("list/", list_view, name= "bookings-list"),
    path("buscar/<nombre_de_usuario>", search_view),
    path("buscar-reserva-con-formulario", search_booking_with_form_view, name="buscar-reserva-con-formulario")
]
