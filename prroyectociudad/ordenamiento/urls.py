from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('parroquias/', views.parroquias_y_barrios, name='parroquias_y_barrios'),
    path('barrios/', views.lista_barrios, name='lista_barrios'),
    path('crear_parroquia/', views.crear_parroquia, name='crear_parroquia'),
    path('crear_barrio/', views.crear_barrio, name='crear_barrio'),
]
