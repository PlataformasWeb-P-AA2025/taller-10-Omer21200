from django.contrib import admin
from .models import Parroquia, Barrio

@admin.register(Parroquia)
class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    list_filter = ('ubicacion', 'tipo')
    search_fields = ('nombre',)
    ordering = ('nombre',)
    

@admin.register(Barrio)
class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios_residenciales', 'parroquia')
    list_filter = ('numero_parques', 'parroquia')
    search_fields = ('nombre',)
    ordering = ('nombre',)
