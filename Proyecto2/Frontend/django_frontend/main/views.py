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
    return render(request, 'protected.html')

#vista para el catalogo de productos
def productos_view(request):
    response = requests.get('http://127.0.0.1:5000/get_products')
    products = response.json()#obtenemos los productos en formato json desde el servidor
    return render(request, 'catalogo.html', {'products': products})


