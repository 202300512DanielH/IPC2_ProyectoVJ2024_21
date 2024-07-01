from flask import Flask, request, jsonify, Response, send_file
from flask_cors import CORS 
from models.user import Usuario
from models.product import Producto
from models.employee import Empleado
from models.activity import Actividad
from models.purchase import Compra
from models.cart import Carrito
import xml.etree.ElementTree as ET
import os
import datetime
import re
from collections import Counter

app = Flask(__name__)
CORS(app)

# Inicializa el archivo xml donde se almacenan los archivos si no existe
DATA_DIR = 'data/uploads'
USERS_FILE = os.path.join(DATA_DIR, 'users.xml')
PRODUCTS_FILE = os.path.join(DATA_DIR, 'products.xml')
EMPLOYEES_FILE = os.path.join(DATA_DIR, 'employees.xml')
ACTIVITIES_FILE = os.path.join(DATA_DIR, 'activities.xml')
CART_FILE = os.path.join(DATA_DIR, 'cart.xml')
PURCHASES_FILE = os.path.join(DATA_DIR, 'purchases.xml')
ACTIVITIES_TODAY_FILE = os.path.join(DATA_DIR, 'activities_today.xml')

# Asegura que el directorio exista
os.makedirs(DATA_DIR, exist_ok=True)

# Crea archivos XML vacíos si no existen
for file in [USERS_FILE, PRODUCTS_FILE, EMPLOYEES_FILE, ACTIVITIES_FILE, CART_FILE, PURCHASES_FILE, ACTIVITIES_TODAY_FILE]:
    if not os.path.exists(file):
        root = ET.Element(os.path.splitext(os.path.basename(file))[0])
        tree = ET.ElementTree(root)
        tree.write(file)


# Usuarios estáticos para login (no me dejaron usar pandas pipipi)
users = {}
username = " "
carrito = Carrito()
compras = []

# Función para obtener los usuarios actualmente cargados en el sistema 
def load_users():
    global users
    try:
        tree = ET.parse(USERS_FILE)
        root = tree.getroot()
        # Limpiar el diccionario de usuarios
        users = {}
        # Quemando el admin
        users["3"] = "3" #usuario rapido para pruebas
        users["AdminIPC2"] = "IPC2VJ2024"
        # Cargar los usuarios del archivo XML
        for elemento_usuario in root.findall('usuario'):
            id = elemento_usuario.get('id')
            password = elemento_usuario.get('password')
            users[id] = password
        print("Usuarios cargados correctamente", users)
    except Exception as e:
        print(str(e))

# Cargar los usuarios al iniciar la aplicación
load_users()

# Endpoint para login
@app.route('/login', methods=['POST'])
def login():
    global username, users, carrito
    carrito.vaciar_carrito()
    load_users()
    username = request.form.get('username')
    password = request.form.get('password')
    
    #limpiando el carrito de compras
    tree_carrito = ET.parse(CART_FILE)
    root_carrito = tree_carrito.getroot()
    root_carrito.clear()
    tree_carrito.write(CART_FILE)
    
    if username in users and users[username] == password:
        return jsonify({"msg": "Login Exitoso"}), 200
    else:
        return jsonify({"msg": "Usuario o contraseña incorrecta"}), 401

# Endpoint para cargar masivamente usuarios al archivo xml de usuarios
@app.route('/carga_masiva_usuarios', methods=['POST'])
def carga_masiva_usuarios():
    if 'file' not in request.files:
        return jsonify({'error': 'No hay archivo para cargar'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 401

    try:
        tree = ET.parse(file)
        root = tree.getroot()
        existing_tree = ET.parse(USERS_FILE)
        existing_root = existing_tree.getroot()

        existing_ids = {usuario.get('id') for usuario in existing_root.findall('usuario')}
        errors = []
        usuarios_agregados = 0

        for usuario in root.findall('usuario'):
            id_usuario = usuario.get('id')
            email = usuario.find('email').text if usuario.find('email') is not None else ""
            telefono = usuario.find('telefono').text if usuario.find('telefono') is not None else ""
            password = usuario.get('password')
            nombre = usuario.find('nombre').text if usuario.find('nombre') is not None else ""
            edad = usuario.find('edad').text if usuario.find('edad') is not None else ""

            user = Usuario(id_usuario, password, nombre, edad, email, telefono)

            if id_usuario in existing_ids:
                errors.append(f"ID repetido: {id_usuario}")
                continue
            elif email and not user.validar_email(email):
                errors.append(f"Email inválido: {email} en usuario ID: {id_usuario}")
                continue
            elif telefono and not user.validar_telefono(telefono):
                errors.append(f"Teléfono inválido: {telefono} en usuario ID: {id_usuario}")
                continue
            
            existing_root.append(usuario)
            existing_ids.add(id_usuario)
            usuarios_agregados += 1

            print(f"Usuario agregado: {id_usuario}")
        #indentar el xml
        indentar(existing_root)
        # Guardar los cambios en el archivo XML
        existing_tree.write(USERS_FILE, encoding="utf-8", xml_declaration=True)
        print("XML actualizado guardado")

        if errors:
            return jsonify({"success": f"Se cargaron correctamente {usuarios_agregados} usuarios.", "errors": errors}), 207
        return jsonify({"success": f"Todos los usuarios ({usuarios_agregados}) cargados correctamente"}), 200
    except ET.ParseError:
        return jsonify({'error': 'Error en el parseo del xml'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Modificación en el endpoint para obtener los usuarios del xml de usuarios con validación
@app.route('/get_users', methods=['GET'])
def get_users():
    try:
        tree = ET.parse(USERS_FILE)
        root = tree.getroot()
        usuarios = []
        for elemento_usuario in root.findall('usuario'):
            id = elemento_usuario.get('id')
            nombre = elemento_usuario.find('nombre').text if elemento_usuario.find('nombre') is not None else ""
            edad = elemento_usuario.find('edad').text if elemento_usuario.find('edad') is not None else ""
            email = elemento_usuario.find('email').text if elemento_usuario.find('email') is not None else ""
            telefono = elemento_usuario.find('telefono').text if elemento_usuario.find('telefono') is not None else ""
            password = elemento_usuario.get('password', "")
            user = Usuario(id, password, nombre, edad, email, telefono)
            usuarios.append(user.to_json())
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para cargar masivamente productos al archivo xml de productos
@app.route('/carga_masiva_productos', methods=['POST'])
def carga_masiva_productos():
    if 'file' not in request.files:
        return jsonify({'error': 'No hay archivo para cargar'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 400
    # Parsear el archivo XML cargado
    try:
        tree = ET.parse(file)
        root = tree.getroot()
        existing_tree = ET.parse(PRODUCTS_FILE)
        existing_root = existing_tree.getroot()

        # Verificar unicidad del ID
        existing_ids = {producto.get('id') for producto in existing_root.findall('producto')}
        errors = []  # Lista para acumular errores
        productos_cargados = 0
        for producto in root.findall('producto'):
            id_producto = producto.get('id')
            precio = producto.find('precio').text if producto.find('precio') is not None else ""
            cantidad = producto.find('cantidad').text if producto.find('cantidad') is not None else ""
            descripcion = producto.find('descripcion').text if producto.find('descripcion') is not None else ""
            categoria = producto.find('categoria').text if producto.find('categoria') is not None else ""
            imagen = producto.find('imagen').text if producto.find('imagen') is not None else ""
            nombre = producto.find('nombre').text if producto.find('nombre') is not None else ""

            product = Producto(id_producto, nombre, precio, descripcion, categoria, cantidad, imagen)
            
            # Validar ID, precio y cantidad
            if id_producto in existing_ids:
                errors.append(f"ID repetido en producto: {id_producto}")
                continue 
            if not product.validar_precio(precio):
                errors.append(f"Precio inválido: {precio} en producto ID: {id_producto}")
                continue
            if not product.validar_cantidad(cantidad):
                errors.append(f"Cantidad inválida: {cantidad} en producto ID: {id_producto}")
                continue

            existing_root.append(producto)
            existing_ids.add(id_producto)
            productos_cargados += 1

        indentar(existing_root)
        existing_tree.write(PRODUCTS_FILE, encoding="utf-8", xml_declaration=True)

        if errors:
            return jsonify({"success": f"se cargaron {productos_cargados} productos", "errors": errors}), 207
        return jsonify({"success": "Todos los productos cargados correctamente"}), 200

    except ET.ParseError:
        return jsonify({'error': 'Error en el parseo del xml'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Endpoint para obtener los productos del xml de productos
@app.route('/get_products', methods=['GET'])
def get_products():
    try:
        tree = ET.parse(PRODUCTS_FILE)
        root = tree.getroot()
        productos = []
        for elemento_producto in root.findall('producto'):
            id_producto = elemento_producto.get('id')
            nombre = elemento_producto.find('nombre').text if elemento_producto.find('nombre') is not None else ""
            precio = elemento_producto.find('precio').text if elemento_producto.find('precio') is not None else ""
            descripcion = elemento_producto.find('descripcion').text if elemento_producto.find('descripcion') is not None else ""
            categoria = elemento_producto.find('categoria').text if elemento_producto.find('categoria') is not None else ""
            cantidad = elemento_producto.find('cantidad').text if elemento_producto.find('cantidad') is not None else ""
            imagen = elemento_producto.find('imagen').text if elemento_producto.find('imagen') is not None else ""

            new_product = Producto(id_producto, nombre, precio, descripcion, categoria, cantidad, imagen)
            productos.append(new_product.to_json())
            
        return jsonify(productos), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para cargar masivamente empleados al archivo xml de empleados
@app.route('/carga_masiva_empleados', methods=['POST'])
def carga_masiva_empleados():
    if 'file' not in request.files:
        return jsonify({'error': 'No hay archivo para cargar'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No se selecciono ningun archivo'}), 400

    try:
        tree = ET.parse(file)
        root = tree.getroot()
        existing_tree = ET.parse(EMPLOYEES_FILE)
        existing_root = existing_tree.getroot()

        # Verificar unicidad del código
        existing_codigos = {empleado.get('codigo') for empleado in existing_root.findall('empleado')}
        errors = []  # Lista para acumular errores
        empleados_cargados = 0
        for empleado in root.findall('empleado'):
            codigo_empleado = empleado.get('codigo')
            nombre = empleado.find('nombre').text if empleado.find('nombre') is not None else ""
            puesto = empleado.find('puesto').text if empleado.find('puesto') is not None else ""

            # Validar código
            if codigo_empleado in existing_codigos:
                errors.append(f"Código repetido en empleado: {codigo_empleado}")
                continue  # Saltar al siguiente empleado sin añadir este

            existing_root.append(empleado)
            existing_codigos.add(codigo_empleado)
            empleados_cargados += 1

        existing_tree.write(EMPLOYEES_FILE, encoding="utf-8", xml_declaration=True)

        if errors:
            return jsonify({"success": f"Se cargaron {empleados_cargados} empleados", "errors": errors}), 207
        return jsonify({"success": "Todos los empleados cargados correctamente"}), 200

    except ET.ParseError:
        return jsonify({'error': 'Error en el parseo del xml'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Endpoint para obtener las actividades del xml de actividades
@app.route('/get_employees', methods=['GET'])
def get_employees():
    try:
        tree = ET.parse(EMPLOYEES_FILE)
        root = tree.getroot()
        empleados = []
        for elemento_empleado in root.findall('empleado'):
            codigo = elemento_empleado.get('codigo')
            nombre = elemento_empleado.find('nombre').text if elemento_empleado.find('nombre') is not None else ""
            puesto = elemento_empleado.find('puesto').text if elemento_empleado.find('puesto') is not None else ""
            new_employee = Empleado(codigo, nombre, puesto)
            empleados.append(new_employee.to_json())
        return jsonify(empleados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para cargar masivamente actividades al archivo xml de actividades
@app.route('/carga_masiva_actividades', methods=['POST'])
def carga_masiva_actividades():
    if 'file' not in request.files:
        return jsonify({'error': 'No hay archivo para cargar'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 400

    try:
        tree = ET.parse(file)
        root = tree.getroot()
        existing_tree = ET.parse(ACTIVITIES_FILE)
        existing_root = existing_tree.getroot()

        existing_ids = {actividad.get('id') for actividad in existing_root.findall('actividad')}
        errors = []  # Lista para acumular errores
        actividades_cargadas = 0
        for actividad in root.findall('actividad'):
            id_actividad = actividad.get('id')

            # Validar ID
            if id_actividad in existing_ids:
                errors.append(f"ID repetido en actividad: {id_actividad}")
                continue  # Saltar al siguiente actividad sin añadir esta

            existing_root.append(actividad)
            existing_ids.add(id_actividad)
            actividades_cargadas += 1
        existing_tree.write(ACTIVITIES_FILE, encoding="utf-8", xml_declaration=True)

        if errors:
            return jsonify({"success": f"Se han cargado {actividades_cargadas} actividades", "errors": errors}), 207
        return jsonify({"success": "Todas las actividades cargadas correctamente"}), 200

    except ET.ParseError:
        return jsonify({'error': 'Error en el parseo del xml'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Endpoint para obtener las actividades del xml de actividades
@app.route('/get_activities', methods=['GET'])
def get_activities():
    try:
        tree = ET.parse(ACTIVITIES_FILE)
        root = tree.getroot()
        actividades = []
        for elemento_actividad in root.findall('actividad'):
            id_actividad = elemento_actividad.get('id')
            nombre = elemento_actividad.find('nombre').text if elemento_actividad.find('nombre') is not None else ""
            descripcion = elemento_actividad.find('descripcion').text if elemento_actividad.find('descripcion') is not None else ""
            empleado = elemento_actividad.find('empleado').text if elemento_actividad.find('empleado') is not None else ""
            dia = elemento_actividad.find('dia').text if elemento_actividad.find('dia') is not None else ""
            hora = elemento_actividad.get('hora', "")
            new_activity = Actividad(id_actividad, nombre, descripcion, empleado, dia, hora)
            actividades.append(new_activity.to_json())
        return jsonify(actividades), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Función para añadir indentación al XML
def indentar(elemento_identar, level=0):
    i = "\n" + level * "  "
    if len(elemento_identar):
        # Si el elemento tiene hijos, añadir indentación
        if not elemento_identar.text or not elemento_identar.text.strip():
            elemento_identar.text = i + "   "
        # Si el elemento tiene hijos, añadir indentación
        if not elemento_identar.tail or not elem.tail.strip():
            elemento_identar.tail = i
        # Llamar recursivamente a los hijos del elemento para indentarlos
        for elemento_identar in elemento_identar:
            indent(elemento_identar, level + 1)
        # Si el último hijo no tiene tail, añadir indentación (tail: texto después del último hijo)
        if not elemento_identar.tail or not elemento_identar.tail.strip():
            elemento_identar.tail = i
    else:
        # Si el elemento no tiene hijos, añadir indentación al texto
        if level and (not elemento_identar.tail or not elemento_identar.tail.strip()):
            elemento_identar.tail = i

# Endpoint para agregar productos al archivo xml que representa el carrito de compras
@app.route('/add_cart', methods=['POST'])
def add_cart():
    global carrito
    try:
        data = request.form
        nombre_producto = data.get('nombre_producto')
        cantidad_solicitada = int(data.get('cantidad'))

        if not nombre_producto or cantidad_solicitada is None:
            return jsonify({"error": "Faltan datos obligatorios (nombre_producto o cantidad)"}), 400

        # Buscando el producto y verificando el stock disponible
        tree = ET.parse(PRODUCTS_FILE)
        root = tree.getroot()
        id_producto = ""
        cantidad_disponible = 0
        for producto in root.findall('producto'):
            if producto.find('nombre').text == nombre_producto:
                id_producto = producto.get('id')
                cantidad_disponible = int(producto.find('cantidad').text)
                break

        if cantidad_solicitada > cantidad_disponible:
            return jsonify({"error": "Cantidad solicitada supera el stock disponible"}), 400

        carrito.agregar_producto(id_producto, nombre_producto, str(cantidad_solicitada))

        return jsonify({"success": f"Producto '{nombre_producto}' añadido al carrito correctamente"}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

    
# Endpoint para obtener los productos del carrito de compras
@app.route('/get_cart', methods=['GET'])
def get_cart():
    global carrito
    return jsonify(carrito.productos), 200

# Endpoint para obtener los productos del carrito de compras
@app.route('/descarga_carrito', methods=['GET'])
def descarga_carrito():
    global carrito
    #Escribir el archivo xml del carrito de compras los producto en el carrito
    tree = ET.parse(CART_FILE)
    root = tree.getroot()
    #Limpiando el archivo del carrito
    root.clear()
    #creando el elemento carrito
    carrito_element = ET.Element('carrito')
    root.append(carrito_element)
    # recorriendo la lista de productos en el carrito tomando en cuanta que cada producto es un diccionario
    for producto in carrito.productos:
        #si el producto ya esta en el carrito, se suma la cantidad
        producto_existente = root.find(f"producto[@id='{producto['id']}']")
        if producto_existente is not None:
            cantidad_actual = int(producto_existente.find('cantidad').text)
            nueva_cantidad = cantidad_actual + int(producto['cantidad'])
            producto_existente.find('cantidad').text = str(nueva_cantidad)
            continue
        #si el producto no esta en el carrito, se agrega
        elemento_producto = ET.Element('producto')
        elemento_producto.set('id', producto['id'])
        ET.SubElement(elemento_producto, 'nombre').text = producto['producto']
        ET.SubElement(elemento_producto, 'cantidad').text = producto['cantidad']
        root.append(elemento_producto)
    
    indentar(root)
    tree.write(CART_FILE, encoding="utf-8", xml_declaration=True)
    
    #descargar el archivo
    file_path = CART_FILE 
    return send_file(file_path, as_attachment=True) #descarga el archivo

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def obtener_productos_stock():
    try:
        tree = ET.parse(PRODUCTS_FILE)
        root = tree.getroot()
        productos = []
        for elemento_producto in root.findall('producto'):
            nombre = elemento_producto.find('nombre').text if elemento_producto.find('nombre') is not None else ""
            cantidad = elemento_producto.find('cantidad').text if elemento_producto.find('cantidad') is not None else ""
            precio = elemento_producto.find('precio').text if elemento_producto.find('precio') is not None else ""
            productos.append({'producto': nombre, 'cantidad': cantidad, 'precio': precio})
        return productos
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/comprar', methods=['POST'])
def comprar():
    global username, carrito, compras
    try:
        #leyendo el Purchases_file para saber el numero de compra que se va a realizar
        tree = ET.parse(PURCHASES_FILE)
        root = tree.getroot()
        num_compra = str(int(compras[-1]['num_compra']) + 1 if len(compras) != 0 else 1)
        
        id_usuario = username
        
        #buscando el nombre del usuario en el archivo de usuarios
        tree_usuarios = ET.parse(USERS_FILE)
        root_usuarios = tree_usuarios.getroot()
        nombre_usuario = ""
        for usuario in root_usuarios.findall('usuario'):
            if usuario.get('id') == id_usuario:
                nombre_usuario = usuario.find('nombre').text
                break
        
        productos_stock = obtener_productos_stock()
        if len(carrito.productos) == 0:
            return jsonify({"error": "No hay productos en el carrito"}), 400

        #si la cantidad de un producto en el carrito es mayor a la cantidad en stock, se manda un error
        for producto in carrito.productos:
            for producto_stock in productos_stock:
                if producto['producto'] == producto_stock['producto']:
                    if int(producto['cantidad']) > int(producto_stock['cantidad']):
                        return jsonify({"error": f"No hay suficiente stock para el producto {producto['producto']}"}), 400
        
        new_compra = Compra(num_compra, id_usuario, nombre_usuario, carrito.productos, productos_stock)
        
        #eliminando los productos comprados del stock
        for producto in new_compra.productos_carrito:
            #leyendo el archivo de productos
            tree_productos = ET.parse(PRODUCTS_FILE)
            root_productos = tree_productos.getroot()
            for producto_stock in root_productos.findall('producto'):
                if producto_stock.find('nombre').text == producto['producto']:
                    cantidad_actual = int(producto_stock.find('cantidad').text)
                    nueva_cantidad = cantidad_actual - int(producto['cantidad'])
                    producto_stock.find('cantidad').text = str(nueva_cantidad)
                    break
            #guardando los cambios en el archivo de productos
            indentar(root_productos)
            tree_productos.write(PRODUCTS_FILE, encoding="utf-8", xml_declaration=True)
            
        #agregando la compra a la lista de compras
        compras.append(new_compra.to_json())
        
        #limpiando el carrito de compras
        carrito.vaciar_carrito()

        return jsonify({"success": "Compra añadida correctamente"}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

#Endpoint para descargar el archivo de compras
@app.route('/descarga_compras', methods=['GET'])
def descarga_compras():
    global compras
    # Escribiendo en el archivo de compras
    tree = ET.parse(PURCHASES_FILE)
    root = tree.getroot()

    # Si no hay compras en la lista de compras, se manda un XML vacío
    if len(compras) == 0:
        indentar(root)
        tree.write(PURCHASES_FILE, encoding="utf-8", xml_declaration=True)
        file_path = PURCHASES_FILE
        return send_file(file_path, as_attachment=True)
    
    # Obteniendo el número de compra más alto en root para asignar el siguiente número de compra
    compras_element = root.find('compras')
    if compras_element is None:
        compras_element = ET.SubElement(root, 'compras')
    
    ultima_compra = compras_element.findall('compra')
    numero_ultima_compra = 0
    
    if len(ultima_compra) != 0:
        numero_ultima_compra = int(ultima_compra[-1].get('numero'))
    else:
        numero_ultima_compra = 0
    
    # Recorriendo la lista de compras
    for compra in compras:
        numero_ultima_compra += 1
        numero_ultima_compra_str = str(numero_ultima_compra)
        
        # Creando el elemento compra
        compra_element = ET.Element('compra')
        compra_element.set('numero', numero_ultima_compra_str)
        
        # Creando el elemento usuario
        usuario_element = ET.SubElement(compra_element, 'usuario')
        usuario_element.set('id', compra['id_usuario'])
        usuario_element.text = compra['nombre_usuario']
        
        # Creando el elemento productos
        productos_element = ET.SubElement(compra_element, 'productos')
        
        # Recorriendo la lista de productos en la compra
        for producto in compra['productos_carrito']:
            # Creando el elemento producto
            producto_element = ET.Element('producto')
            producto_element.set('id', producto['id'])
            
            # Creando el elemento nombre
            nombre_element = ET.SubElement(producto_element, 'nombre')
            nombre_element.text = producto['producto']
            
            # Creando el elemento cantidad
            cantidad_element = ET.SubElement(producto_element, 'cantidad')
            cantidad_element.text = str(producto['cantidad'])
            
            productos_element.append(producto_element)
        
        # Creando el elemento total
        total_element = ET.SubElement(compra_element, 'total')
        total_element.text = str(compra['total'])
        
        compras_element.append(compra_element)
    
    indentar(root)
    tree.write(PURCHASES_FILE, encoding="utf-8", xml_declaration=True)
    
    # Vaciando la lista de compras 
    compras = []
    
    # Descargar el archivo    
    file_path = PURCHASES_FILE
    return send_file(file_path, as_attachment=True)

def get_activities_today():
    try:
        # Limpiar el archivo de actividades de hoy
        tree_today = ET.parse(ACTIVITIES_TODAY_FILE)
        root_today = tree_today.getroot()
        root_today.clear()
        tree_today.write(ACTIVITIES_TODAY_FILE, encoding="utf-8", xml_declaration=True)
        # Parsear el archivo de actividades y empleados una sola vez
        tree = ET.parse(ACTIVITIES_FILE)
        root = tree.getroot()
        tree_empleados = ET.parse(EMPLOYEES_FILE)
        root_empleados = tree_empleados.getroot()

        # Obtener el día actual
        dia_actual = datetime.datetime.today().weekday() + 1
        dia_actual_nombre = dia_nombre(dia_actual)

        # Preparar el archivo de actividades de hoy
        tree_today = ET.parse(ACTIVITIES_TODAY_FILE)
        root_today = tree_today.getroot()

        # Verificar si ya existe un elemento <dia> para el día actual
        if not any(dia.text == dia_actual_nombre for dia in root_today.findall('dia')):
            ET.SubElement(root_today, 'dia').text = dia_actual_nombre

        for elemento_actividad in root.findall('actividad'):
            dia = elemento_actividad.find('dia').text if elemento_actividad.find('dia') is not None else ""
            if int(dia) == dia_actual:
                id = elemento_actividad.get('id')
                nombre = elemento_actividad.find('nombre').text if elemento_actividad.find('nombre') is not None else ""
                descripcion = elemento_actividad.find('descripcion').text if elemento_actividad.find(
                    'descripcion') is not None else ""
                empleado_codigo = elemento_actividad.find('empleado').text if elemento_actividad.find(
                    'empleado') is not None else ""
                dia_element = elemento_actividad.find('dia')
                hora = dia_element.get('hora', "") if dia_element is not None else ""

                # Obtener el nombre del empleado
                empleado_nombre = ""
                for empleado in root_empleados.findall('empleado'):
                    if empleado.get('codigo') == empleado_codigo:
                        empleado_nombre = empleado.find('nombre').text
                        break

                # Crear y añadir la nueva actividad
                actividad_element = ET.Element('actividad')
                actividad_element.set('id', id)
                ET.SubElement(actividad_element, 'nombre').text = nombre
                ET.SubElement(actividad_element, 'descripcion').text = descripcion
                ET.SubElement(actividad_element, 'empleado').text = empleado_nombre
                ET.SubElement(actividad_element, 'hora').text = hora + ":00"

                root_today.append(actividad_element)

        indentar(root_today)
        tree_today.write(ACTIVITIES_TODAY_FILE, encoding="utf-8", xml_declaration=True)
        return jsonify({"success": f"Actividades del día {dia_actual_nombre} exportadas correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#Endpoint para descargar el archivo de actividades del dia actual
@app.route('/descarga_actividades_hoy', methods=['GET'])
def descarga_actividades_hoy():
    #actualizar el archivo de actividades del dia antes de la descarga 
    get_activities_today()
    #descargar el archivo
    file_path = ACTIVITIES_TODAY_FILE
    return send_file(file_path, as_attachment=True)

#Funcion para obtener el nombre del día
def dia_nombre(dia_num):
            dias = {
                1: 'Lunes',
                2: 'Martes',
                3: 'Miércoles',
                4: 'Jueves',
                5: 'Viernes',
                6: 'Sábado',
                7: 'Domingo'
            }
            return dias.get(dia_num, "")

@app.route('/admin', methods=['GET'])
def protected():
    # Aquí tenemos el recurso protegido
    return jsonify({"msg": "Has accedido al módulo de administrador"}), 200


@app.route('/categorias_estadisticas', methods=['GET'])
def categorias_estadisticas():
    try:
        tree = ET.parse(PRODUCTS_FILE)  # Asegúrate de que PRODUCTS_FILE esté correctamente definido
        root = tree.getroot()
        categorias = [prod.find('categoria').text for prod in root.findall('producto') if
                    prod.find('categoria') is not None]
        categoria_count = Counter(categorias)

        # Selecciona las tres categorías con más productos
        top_categorias = categoria_count.most_common(3)
        top_categorias_dict = {categoria: count for categoria, count in top_categorias}

        return jsonify(top_categorias_dict), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/productos_con_mas_cantidad', methods=['GET'])
def productos_con_mas_cantidad():
    try:
        tree = ET.parse(PRODUCTS_FILE)  # Asegúrate de que PRODUCTS_FILE esté correctamente definido
        root = tree.getroot()

        productos = [(prod.find('nombre').text, int(prod.find('cantidad').text)) for prod in root.findall('producto')]
        producto_count = Counter(dict(productos))

        # Selecciona los tres productos con más cantidad
        top_productos = producto_count.most_common(3)
        top_productos_dict = {producto: cantidad for producto, cantidad in top_productos}

        return jsonify(top_productos_dict), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
