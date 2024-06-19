from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('protected/', views.protected, name='protected'),
    path('carga_usuarios/', views.carga_usuarios, name='carga_usuarios'),
    path('carga_productos/', views.carga_productos, name='carga_productos'),
    path('actividades/', views.actividades, name='carga_actividades'),
    path('carga_empleados/', views.carga_empleados, name='carga_empleados'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    path('reportes_compras/', views.reportes_compras, name='reportes_compras'),
    path('reportes_actividades/', views.reportes_actividades, name='reportes_actividades'),
    path('colaboradores/', views.colaboradores, name='colaboradores'),
    path('docu/', views.docu, name='docu')
]
