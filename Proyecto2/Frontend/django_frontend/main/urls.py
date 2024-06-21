from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('protected/', views.protected, name='protected'),
    
    path('productos/', views.productos_view, name='productos'),
    path('productos/<str:producto_id>/', views.producto_detalle_view, name='producto_detalle'),
    path('descarga_carrito/', views.descarga_carrito, name='descarga_carrito'),
    
    path('carga_usuarios/', views.carga_usuarios, name='carga_usuarios'),
    path('carga_productos/', views.carga_productos, name='carga_productos'),
    path('actividades/', views.actividades, name='carga_actividades'),
    path('carga_empleados/', views.carga_empleados, name='carga_empleados'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    
    path('reportes/', views.reportes, name='reportes'),
    
    path('productos_admin/', views.productos_view_admin, name='productos_admin'),
    path('productos_admin/<str:producto_id>/', views.producto_detalle_view_admin, name='producto_detalle_admin'),
    
    path('colaboradores/', views.colaboradores, name='colaboradores'),
    path('docu/', views.docu, name='docu')
]
