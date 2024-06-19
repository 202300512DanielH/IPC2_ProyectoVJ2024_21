from django.shortcuts import render, redirect
import requests

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        response = requests.post('http://127.0.0.1:5000/login', data={'username': username, 'password': password})
        if response.status_code == 200:
            request.session['logged_in'] = True
            return redirect('protected')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

def protected(request):
    if not request.session.get('logged_in'):
        return redirect('login')
    return render(request, 'admin.html')

def carga_usuarios(request):
    return render(request, 'pestaña_CM_Usuarios.html')

def carga_productos(request):
    return render(request, 'pestaña_CM_Productos.html')

def actividades(request):
    return render(request, 'pestaña_CM_Actividades.html')

def carga_empleados(request):
    return render(request, 'pestaña_CM_Empleados.html')

def estadisticas(request):
    return render(request, 'estadisticas.html')

def reportes_compras(request):
    return render(request, 'reportes_compras.html')

def reportes_actividades(request):
    return render(request, 'reportes_actividades.html')

def colaboradores(request):
    return render(request, 'colaboradores.html')

def docu(request):
    return render(request, 'docu.html')