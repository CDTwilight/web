from django.urls import path

from . import views

app_name = 'pedidos'

urlpatterns = [
    path('prosesar_pedido/', views.prosesar_pedido, name='prosesar_pedido'),
    path('lista/', views.lista_pedidos, name='lista_pedidos'),
    path('detalle/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('eliminar/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('editar/<int:pedido_id>/', views.editar_pedido, name='editar_pedido'),
    path('editar_detalle/<int:pedido_id>/', views.editar_detalle, name='editar_detalle'),
    path('efectuar/<int:pedido_id>/', views.efectuar_pedido, name='efectuar_pedido'),
    path('factura/<int:pedido_id>/', views.generar_factura, name='generar_factura'),
    path('oferta/<int:pedido_id>/', views.generar_oferta, name='generar_oferta'),
    path('cancelar/<int:pedido_id>/', views.cancelar_pedido, name='cancelar_pedido'),
    path('reactivar/<int:pedido_id>/', views.reactivar_pedido, name='reactivar_pedido'),
    path('configuracion/', views.configurar_eliminacion, name='configurar_eliminacion'),
    path('estadisticas/', views.estadisticas_usuario, name='estadisticas_usuario'),
    path('get-clientes-by-gestor/', views.get_clientes_by_gestor, name='get_clientes_by_gestor'),

]
