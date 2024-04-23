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
    ConsultorioUpdateView,
    therapist_list_view,
    update_booking_view,
    create_therapist_with_form_view,
    detail_therapist_view,
    update_therapist_view,
    MasajistaDeleteView,
    therapist_search_view,
    user_login_view,
    user_logout_view,
    user_creation_view,
    UserUpdateView
    )



urlpatterns = [
    path("", home_view, name="home"),
    path("detail-booking/<booking_id>", detail_booking_view, name="booking-detail"),
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
    path("masajista/list", therapist_list_view, name="masajista-list"),
    path("update-booking/<booking_id>", update_booking_view, name="booking-update"),
    path("masajista/create", create_therapist_with_form_view, name="masajista-create"),
    # Vistas basadas en clases
    path("consultorio/vbc/list", ConsultorioListView.as_view(), name="vbc-consultorio-list"),
    path("consultorio/vbc/<int:pk>/detail", ConsultorioDetailView.as_view(), name="vbc-consultorio-detail"),
    path("consultorio/vbc/create", ConsultorioCreateView.as_view(), name="vbc-consultorio-create"),
    path("consultorio/vbc/<int:pk>/delete", ConsultorioDeleteView.as_view(), name="vbc-consultorio-delete"),
    path("consultorio/vbc/<int:pk>/update", ConsultorioUpdateView.as_view(), name="vbc-consultorio-update"),
    # Fin Vistas basadas en clases
    path("masajista/detail/<therapist_id>", detail_therapist_view, name="masajista-detail"),
    path("masajista/update/<therapist_id>", update_therapist_view, name="masajista-update"),
    path("masajista/<int:pk>/delete", MasajistaDeleteView.as_view(), name="masajista-delete"),
    path("buscar-masajista-con-formulario", therapist_search_view, name="masajista-search"),
    path("login", user_login_view, name="login"),
    path("logout", user_logout_view, name="logout"),
    path("user-create", user_creation_view, name="crear-usuario"),
    path("edit-profile", UserUpdateView.as_view(), name="edit-profile")
]
