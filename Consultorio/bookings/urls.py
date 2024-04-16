from django.contrib import admin
from django.urls import path
from .views import (
    home_view, 
    list_view, 
    search_view, 
    detail_booking_view, 
    search_booking_with_form_view, 
    create_consulting_room_with_form_view, 
    create_booking_with_form_view, 
    detail_consulting_room_view, 
    consulting_room_list_view, 
    consulting_room_delete_view,
    delete_booking_view,
    consulting_room_update_view,
    consulting_room_search_view,
    ConsultorioListView,
    ConsultorioDetailView,
    ConsultorioCreateView,
    ConsultorioDeleteView,
    ConsultorioUpdateView
    )



urlpatterns = [
    path("", home_view),
    path("detail-booking/<booking_id>", detail_booking_view ),
    path("list/", list_view, name= "bookings-list"),
    path("buscar/<nombre_de_usuario>", search_view),
    path("buscar-reserva-con-formulario", search_booking_with_form_view, name="buscar-reserva-con-formulario"),
    path("crear-reserva-con-formulario", create_booking_with_form_view, name="crear-reserva-con-formulario"),
    path("crear-consultorio-con-formulario", create_consulting_room_with_form_view, name="crear-consultorio-con-formulario"),
    path("detail-consulting-room/<consulting_room_id>", detail_consulting_room_view, name="consultorio-detail" ),
    path("consultorio/list", consulting_room_list_view, name="consultorio-list"),
    path("consultorio/delete/<consulting_room_id>", consulting_room_delete_view, name="consultorio-delete"),
    path("delete/<booking_id>", delete_booking_view, name="booking-delete"),
    path("consultorio/update/<consulting_room_id>", consulting_room_update_view, name="consultorio-update"),
    path("buscar-consultorio-con-formulario", consulting_room_search_view, name="consultorio-buscar-con-formulario"),
    # Vistas basadas en clases
    path("consultorio/vbc/list", ConsultorioListView.as_view(), name="vbc-consultorio-list"),
    path("consultorio/vbc/<int:pk>/detail", ConsultorioDetailView.as_view(), name="vbc-consultorio-detail"),
    path("consultorio/vbc/create", ConsultorioCreateView.as_view(), name="vbc-consultorio-create"),
    path("consultorio/vbc/<int:pk>/delete", ConsultorioDeleteView.as_view(), name="vbc-consultorio-delete"),
    path("consultorio/vbc/<int:pk>/update", ConsultorioUpdateView.as_view(), name="vbc-consultorio-update")
]
