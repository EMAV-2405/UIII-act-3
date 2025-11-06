# app_Ford/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ==========================================
    # URLS PRINCIPALES
    # ==========================================
    path('', views.inicio_ford, name='inicio'),

    # ==========================================
    # URLS CRUD DE VEHÍCULO
    # ==========================================
    
    # Create (Agregar)
    path('vehiculos/agregar/', views.agregar_vehiculo, name='agregar_vehiculo'),
    
    # Read (Ver)
    path('vehiculos/ver/', views.ver_vehiculos, name='ver_vehiculos'),
    
    # Update (Actualizar)
    # Paso 1: Mostrar el formulario de actualización (GET)
    path('vehiculos/actualizar/<int:id>/', views.actualizar_vehiculo, name='actualizar_vehiculo'),
    # Paso 2: Procesar la actualización (POST)
    path('vehiculos/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_vehiculo, name='realizar_actualizacion_vehiculo'),

    # Delete (Borrar)
    path('vehiculos/borrar/<int:id>/', views.borrar_vehiculo, name='borrar_vehiculo'),
]