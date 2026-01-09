from django.urls import path, include

urlpatterns = [
    path("api/usuarios/", include("usuarios.api")),
]