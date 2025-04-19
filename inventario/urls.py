from django.urls import path

from . import views

urlpatterns = [
    path('', views.inventario, name='inventario'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('editar-inventario/', views.editar_inventario, name='editar_inventario'),
    path('editar-material/<int:material_id>/', views.editar_material, name='editar_material'),
    path('eliminar-imagen/<int:imagen_id>/', views.eliminar_imagen, name='eliminar_imagen'),
    path('crear-material/', views.crear_material, name='crear_material'),
    path('eliminar-material/<int:material_id>/', views.eliminar_material, name='eliminar_material'),
    path('pedidos-pendientes/<int:material_id>/', views.pedidos_pendientes, name='pedidos_pendientes'),
    path('toggle-destacado/<int:material_id>/', views.toggle_destacado, name='toggle_destacado'),
    path('material/<int:material_id>/imagenes/', views.material_imagenes, name='material_imagenes'),
    path('toggle-activo/<int:material_id>/', views.toggle_activo, name='toggle_activo'),
    path('crear-categoria/', views.crear_categoria, name='crear_categoria'),
    path('toggle-oferta/<int:material_id>/', views.toggle_oferta, name='toggle_oferta'),
]
