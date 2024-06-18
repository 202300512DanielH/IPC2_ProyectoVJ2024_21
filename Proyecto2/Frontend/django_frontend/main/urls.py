from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('protected/', views.protected, name='protected'),
]
