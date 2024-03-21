from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse("<h3>Bienvenidos a la aplicacion de reservas!!!!</h3>")

urlpatterns = [
    path("", mi_vista)
]
