from django.shortcuts import render
from django.http import JsonResponse
from .models import Cliente

# Create your views here.

def buscar_cliente(request, carnet):
    try:
        cliente = Cliente.objects.get(carnet_identidad=carnet)
        
        # Only return client data if it belongs to the authenticated user
        if cliente.user == request.user:
            return JsonResponse({
                'status': 'success',
                'cliente': {
                    'nombre': cliente.nombre,
                    'apellidos': cliente.apellidos,
                    'telefono': cliente.telefono
                }
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Este cliente fue registrado por otro gestor'
            }, status=403)
            
    except Cliente.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Cliente no encontrado'
        }, status=404)
