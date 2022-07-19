from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Propietario, Departamento

# Agregar la clase EPropietario para administrar desde
# interfaz de administración
# admin.site.register(Propietario)

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Propietario
class PropietarioAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'apellido', 'edad','nacionalidad')
    search_fields = ('nombre', 'apellido')

admin.site.register(Propietario, PropietarioAdmin)

# Agregar la clase Departamento para administrar desde
# interfaz de administración
# admin.site.register(Departamento)

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# NDepartamento
class DepartamentoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('costo_departamento', 'num_cuartos', 'num_banos','valor','propietario')
    # se agrega el atributo 
    # raw_id_fields que permite acceder a una interfaz 
    # para buscar los ePropietarios y seleccionar el que 
    # se desee
    raw_id_fields = ('propietario',)

admin.site.register(Departamento, DepartamentoAdmin)
