"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views

from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),

]
