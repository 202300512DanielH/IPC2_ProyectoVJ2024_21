from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),  # Redirige la URL raíz a la vista de inicio de sesión
    path('', include('main.urls')),  # Incluye todas las URLs de la aplicación 'main'
]
