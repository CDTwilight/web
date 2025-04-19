from django.urls import path

from .views import Vregistro, cerrar_sesion, logear, administrar_usuarios, crear_usuario, editar_usuario, eliminar_usuario, historial_usuario, toggle_estado_usuario

urlpatterns = [
    
    path('', Vregistro.as_view(), name='Autenticacion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path('logear', logear, name='Logear'),
    path('administrar-usuarios/', administrar_usuarios, name='administrar_usuarios'),
    path('crear-usuario/', crear_usuario, name='crear_usuario'),
    path('editar/<int:user_id>/', editar_usuario, name='editar_usuario'),
    path('eliminar/<int:user_id>/', eliminar_usuario, name='eliminar_usuario'),
    path('toggle-estado/<int:user_id>/', toggle_estado_usuario, name='toggle_estado_usuario'),
    path('historial-usuario/<int:user_id>/', historial_usuario, name='historial_usuario'),
    

   
]
