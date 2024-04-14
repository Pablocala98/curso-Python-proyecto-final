from django.contrib import admin
from django.urls import path
from .views import home_view, list_view, search_view, detail_booking_view, search_booking_with_form_view, create_consulting_room_with_form_view, create_booking_with_form_view, detail_consulting_room_view



urlpatterns = [
    path("", home_view),
    path("detail-booking/<booking_id>", detail_booking_view ),
    path("list/", list_view, name= "bookings-list"),
    path("buscar/<nombre_de_usuario>", search_view),
    path("buscar-reserva-con-formulario", search_booking_with_form_view, name="buscar-reserva-con-formulario"),
    path("crear-reserva-con-formulario", create_booking_with_form_view, name="crear-reserva-con-formulario"),
    path("crear-consultorio-con-formulario", create_consulting_room_with_form_view, name="crear-consultorio-con-formulario"),
    path("detail-consulting-room/<consulting_room_id>", detail_consulting_room_view ),

]
