from django.shortcuts import render, redirect
import requests

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        response = requests.post('http://127.0.0.1:5000/login', data={'username': username, 'password': password})
        if response.status_code == 200 :
            request.session['logged_in'] = True
            if username == "AdminIPC2": 
                return redirect('protected')
            else: 
                return redirect('productos')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

def protected(request):
    if not request.session.get('logged_in'):
        return redirect('login')
    return render(request, 'admin.html')


from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import requests


def carga_usuarios(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            # Prepara los archivos para la solicitud
            files = {'file': (file.name, file)}
            response = requests.post('http://127.0.0.1:5000/carga_masiva_usuarios', files=files)

            if response.status_code == 200:
                return render(request, 'pestaña_CM_Usuarios.html', {'success': 'Usuarios cargados correctamente'})
            else:
                # Podemos mejorar la gestión de errores mostrando los errores específicos desde Flask si es necesario
                error_message = response.json().get('error', 'Algun error al cargar usuarios')
                return render(request, 'pestaña_CM_Usuarios.html', {'error': error_message})
        else:
            return render(request, 'pestaña_CM_Usuarios.html', {'error': 'No se seleccionó ningún archivo'})
    return render(request, 'pestaña_CM_Usuarios.html')



#vista para el catalogo de productos
def productos_view(request):
    response = requests.get('http://127.0.0.1:5000/get_products')
    products = response.json()#obtenemos los productos en formato json desde el servidor
    return render(request, 'catalogo.html', {'products': products})

def productos_view_admin(request):
    response = requests.get('http://127.0.0.1:5000/get_products')
    products = response.json()#obtenemos los productos en formato json desde el servidor
    return render(request, 'catalogo_admin.html', {'products': products})

#vista para los detalles de un producto
def producto_detalle_view(request, producto_id):
    response = requests.get('http://127.0.0.1:5000/get_products')
    producto_encontrado = None
    for producto in response.json():
        if producto['id'] == producto_id:
            producto_encontrado = producto
            break
    if request.method == 'POST':
        nombre_producto = producto_encontrado['nombre']
        cantidad = request.POST['cantidad']
        action = request.POST['action']
        
        if action == "add_cart": 
            response = requests.post('http://127.0.0.1:5000/add_cart', data={'nombre_producto': nombre_producto, 'cantidad': cantidad})
            if response.status_code == 200:
                # Podrías añadir un mensaje de éxito si lo deseas
                return render(request, 'producto.html', {'producto': producto_encontrado, 'success': 'Producto agregado al carrito exitosamente.'})
            else:
                # Mostrar mensaje de error
                return render(request, 'producto.html', {'producto': producto_encontrado, 'error': 'No se pudo agregar el producto al carrito'})
        elif action == "add_buy": 
            response = requests.post('http://127.0.0.1:5000/comprar')
            if response.status_code == 200:
                # Podrías añadir un mensaje de éxito si lo deseas
                return render(request, 'producto.html', {'producto': producto_encontrado, 'success': 'Compra realizada exitosamente.'})
            elif response.status_code == 400:
                # Mostrar mensaje de error
                return render(request, 'producto.html', {'producto': producto_encontrado, 'error': 'Carrito vacío, no se pudo realizar la compra'})
            else:
                return render(request, 'producto.html', {'producto': producto_encontrado, 'error': 'No se pudo realizar la compra'})
    
    return render(request, 'producto.html', {'producto': producto_encontrado})

#vista de detalle del producto desde el admin
def producto_detalle_view_admin(request, producto_id):
    response = requests.get('http://127.0.0.1:5000/get_products')
    producto_encontrado = None
    for producto in response.json():
        if producto['id'] == producto_id:
            producto_encontrado = producto
            break
    return render(request, 'detalles_admin.html', {'producto': producto_encontrado})

#vista para descargar el carrito de compras
def descarga_carrito(request):
    flask_download_url = 'http://localhost:5000/descarga_carrito'
    return redirect(flask_download_url)

#vista para descargar las compras realizadas
def descarga_compras(request):
    flask_download_url = 'http://localhost:5000/descarga_compras'
    return redirect(flask_download_url)

def carga_productos(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            # Prepara los archivos para la solicitud
            files = {'file': (file.name, file)}
            response = requests.post('http://127.0.0.1:5000/carga_masiva_productos', files=files)

            if response.status_code == 200:
                return render(request, 'pestaña_CM_Productos.html', {'success': 'Productos cargados correctamente'})
            else:
                # Mejora en el manejo de errores para obtener un mensaje más específico del servidor
                error_message = response.json().get('error', 'Algun error al cargar productos')
                return render(request, 'pestaña_CM_Productos.html', {'error': error_message})
        else:
            return render(request, 'pestaña_CM_Productos.html', {'error': 'No se seleccionó ningún archivo'})
    return render(request, 'pestaña_CM_Productos.html')


def actividades(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            # Prepara los archivos para la solicitud
            files = {'file': (file.name, file)}
            response = requests.post('http://127.0.0.1:5000/carga_masiva_actividades', files=files)

            if response.status_code == 200:
                return render(request, 'pestaña_CM_Actividades.html', {'success': 'Actividades cargadas correctamente'})
            else:
                error_message = response.json().get('error', 'Algun error al cargar actividades')
                return render(request, 'pestaña_CM_Actividades.html', {'error': error_message})
        else:
            return render(request, 'pestaña_CM_Actividades.html', {'error': 'No se seleccionó ningún archivo'})
    return render(request, 'pestaña_CM_Actividades.html')


def carga_empleados(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            # Prepara los archivos para la solicitud
            files = {'file': (file.name, file)}
            response = requests.post('http://127.0.0.1:5000/carga_masiva_empleados', files=files)

            if response.status_code == 200:
                return render(request, 'pestaña_CM_Empleados.html', {'success': 'Empleados cargados correctamente'})
            else:
                error_message = response.json().get('error', 'Algun error al cargar empleados')
                return render(request, 'pestaña_CM_Empleados.html', {'error': error_message})
        else:
            return render(request, 'pestaña_CM_Empleados.html', {'error': 'No se seleccionó ningún archivo'})
    return render(request, 'pestaña_CM_Empleados.html')


def estadisticas(request):
    return render(request, 'estadisticas.html')

def reportes(request):
    if request.method == 'POST':
        action = request.POST['action']
        if action == "compras":
            flask_download_url = 'http://localhost:5000/descarga_compras'
            return redirect(flask_download_url)
        elif action == "actividades": 
            flask_download_url = 'http://localhost:5000/descarga_actividades_hoy'
            return redirect(flask_download_url)
    return render(request, 'reportes.html')

def colaboradores(request):
    return render(request, 'colaboradores.html')

def docu(request):
    return render(request, 'docu.html')

