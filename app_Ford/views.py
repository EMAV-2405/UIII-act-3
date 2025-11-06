# app_Ford/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo
# Importaremos los otros modelos cuando los necesitemos
# from .models import Empleado, Venta 

# ==========================================
# VISTAS PRINCIPALES
# ==========================================

def inicio_ford(request):
    """
    Renderiza la página de inicio.
    """
    return render(request, 'inicio.html')

# ==========================================
# VISTAS CRUD DE VEHÍCULO
# ==========================================

def agregar_vehiculo(request):
    """
    Vista para agregar un nuevo vehículo.
    Maneja GET (mostrar formulario) y POST (guardar datos).
    """
    if request.method == "POST":
        # Recoger datos del formulario (sin validación, como se solicitó)
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        anio = request.POST.get('anio')
        color = request.POST.get('color')
        numero_serie = request.POST.get('numero_serie')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad_disponible')

        # Crear y guardar el nuevo objeto Vehiculo
        Vehiculo.objects.create(
            marca=marca,
            modelo=modelo,
            anio=anio,
            color=color,
            numero_serie=numero_serie,
            precio=precio,
            cantidad_disponible=cantidad
        )
        # Redirigir a la lista de vehículos después de guardar
        return redirect('ver_vehiculos')
    
    # Si es GET, solo muestra el formulario
    return render(request, 'vehiculos/agregar_vehiculo.html')


def ver_vehiculos(request):
    """
    Muestra una lista de todos los vehículos en la base de datos.
    """
    # Obtener todos los objetos Vehiculo
    todos_los_vehiculos = Vehiculo.objects.all()
    # Preparar el contexto para la plantilla
    contexto = {
        'vehiculos': todos_los_vehiculos
    }
    return render(request, 'vehiculos/ver_vehiculos.html', contexto)


def actualizar_vehiculo(request, id):
    """
    Muestra el formulario con los datos actuales del vehículo 
    para que el usuario pueda editarlos. (Maneja GET)
    """
    # Buscar el vehículo por su ID o mostrar error 404 si no existe
    vehiculo_a_actualizar = get_object_or_404(Vehiculo, id=id)
    
    contexto = {
        'vehiculo': vehiculo_a_actualizar
    }
    return render(request, 'vehiculos/actualizar_vehiculo.html', contexto)


def realizar_actualizacion_vehiculo(request, id):
    """
    Procesa los datos enviados desde el formulario de actualización. 
    (Maneja POST)
    """
    # Buscar el vehículo que vamos a actualizar
    vehiculo_a_actualizar = get_object_or_404(Vehiculo, id=id)
    
    if request.method == "POST":
        # Actualizar los campos del objeto con los datos del POST
        vehiculo_a_actualizar.marca = request.POST.get('marca')
        vehiculo_a_actualizar.modelo = request.POST.get('modelo')
        vehiculo_a_actualizar.anio = request.POST.get('anio')
        vehiculo_a_actualizar.color = request.POST.get('color')
        vehiculo_a_actualizar.numero_serie = request.POST.get('numero_serie')
        vehiculo_a_actualizar.precio = request.POST.get('precio')
        vehiculo_a_actualizar.cantidad_disponible = request.POST.get('cantidad_disponible')
        
        # Guardar los cambios en la base de datos
        vehiculo_a_actualizar.save()
        
        # Redirigir a la lista de vehículos
        return redirect('ver_vehiculos')
    
    # Si alguien intenta acceder a esta URL por GET, lo redirigimos
    return redirect('ver_vehiculos')


def borrar_vehiculo(request, id):
    """
    Elimina un vehículo de la base de datos.
    """
    # Buscar el vehículo a eliminar
    vehiculo_a_borrar = get_object_or_404(Vehiculo, id=id)
    
    # Eliminar el objeto
    vehiculo_a_borrar.delete()
    
    # Redirigir a la lista de vehículos
    return redirect('ver_vehiculos')