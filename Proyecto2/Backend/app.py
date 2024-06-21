from flask import Flask, request, jsonify, Response, send_file
from flask_cors import CORS 
import xml.etree.ElementTree as ET
import os
import datetime
import re

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
    global username, users
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

# Función para cargar datos masivos desde XML
def cargar_datos_masivos(file, file_path, tag_name):
    try:
        tree = ET.parse(file)
        new_root = tree.getroot()
        existing_tree = ET.parse(file_path)
        existing_root = existing_tree.getroot()
        contador = 0
        usuarios_repetidos = []
        for elem in new_root.findall(tag_name):
            #verificando que el id no exista
            if tag_name != 'empleado': 
                if existing_root.find(f"{tag_name}[@id='{elem.get('id')}']") is not None:
                    contador += 1
                    usuarios_repetidos.append(elem.get('id'))
                else: 
                    existing_root.append(elem)
            else:
                #verificando que el codigo no exista
                if existing_root.find(f"{tag_name}[@codigo='{elem.get('codigo')}']") is not None:
                    contador += 1
                    usuarios_repetidos.append(elem.get('codigo'))
                else:
                    existing_root.append(elem)
        existing_tree.write(file_path, encoding="utf-8", xml_declaration=True)
        load_users()
        if contador == 0: 
            return {"success": f"Archivo procesado y cargado correctamente todos los {tag_name} al xml de persistencia"}, 200
        else: 
            return {"error": (f"Error al cargar {contador} {tag_name} al XML de persistencia. IDs de {tag_name} repetidos: {usuarios_repetidos}")}, 500
    except ET.ParseError:
        return {"error": "Error en el parseo del xml"}, 500
    except Exception as e:
        return {"error": str(e)}, 500

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
        for usuario in root.findall('usuario'):
            id_usuario = usuario.get('id')
            email = usuario.find('email').text if usuario.find('email') is not None else ""
            telefono = usuario.find('telefono').text if usuario.find('telefono') is not None else ""

            if id_usuario in existing_ids:
                errors.append(f"ID repetido: {id_usuario}")
                continue
            if email and not validar_email(email):
                errors.append(f"Email inválido: {email} en usuario ID: {id_usuario}")
                continue
            if telefono and not validar_telefono(telefono):
                errors.append(f"Teléfono inválido: {telefono} en usuario ID: {id_usuario}")
                continue

            existing_root.append(usuario)
            existing_ids.add(id_usuario)

        print("Guardando archivo en:", USERS_FILE)
        existing_tree.write(USERS_FILE, encoding="utf-8", xml_declaration=True)
        if errors:
            return jsonify({"success": "Algunos usuarios cargados correctamente", "errors": errors}), 207
        return jsonify({"success": "Todos los usuarios cargados correctamente"}), 200
    except ET.ParseError:
        return jsonify({'error': 'Error en el parseo del xml'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Función para validar el formato del correo electrónico
def validar_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None


# Función para validar el formato del número de teléfono
def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) == 8


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

            # Validar el email y el teléfono
            if email and not validar_email(email):
                return jsonify({"error": f"Email inválido: {email}"}), 400
            if telefono and not validar_telefono(telefono):
                return jsonify({"error": f"Teléfono inválido: {telefono}"}), 400

            usuarios.append({
                'id': id,
                'nombre': nombre,
                'edad': edad,
                'email': email,
                'telefono': telefono,
                'password': password
            })
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Función para validar el formato del precio (debe contener decimales)
def validar_precio(precio):
    try:
        float(precio)
        return '.' in precio
    except ValueError:
        return False

# Función para validar el formato de la cantidad (debe ser un entero)
def validar_cantidad(cantidad):
    return cantidad.isdigit()

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

        for producto in root.findall('producto'):
            id_producto = producto.get('id')
            precio = producto.find('precio').text if producto.find('precio') is not None else ""
            cantidad = producto.find('cantidad').text if producto.find('cantidad') is not None else ""

            # Validar ID, precio y cantidad
            if id_producto in existing_ids:
                errors.append(f"ID repetido en producto: {id_producto}")
                continue  # Saltar al siguiente producto sin añadir este
            if not validar_precio(precio):
                errors.append(f"Precio inválido: {precio} en producto ID: {id_producto}")
                continue
            if not validar_cantidad(cantidad):
                errors.append(f"Cantidad inválida: {cantidad} en producto ID: {id_producto}")
                continue

            existing_root.append(producto)
            existing_ids.add(id_producto)

        existing_tree.write(PRODUCTS_FILE, encoding="utf-8", xml_declaration=True)

        if errors:
            return jsonify({"success": "Algunos productos cargados correctamente", "errors": errors}), 207
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

            # Validar Precio y cantidad
            if not validar_precio(precio):
                return jsonify({"error": f"Precio inválido en producto: {precio}"}), 400
            if not validar_cantidad(cantidad):
                return jsonify({"error": f"Cantidad inválida en producto: {cantidad}"}), 400

            productos.append({
                'id': id_producto,
                'nombre': nombre,
                'precio': precio,
                'descripcion': descripcion,
                'categoria': categoria,
                'cantidad': cantidad,
                'imagen': imagen
            })
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

        existing_tree.write(EMPLOYEES_FILE, encoding="utf-8", xml_declaration=True)

        if errors:
            return jsonify({"success": "Algunos empleados cargados correctamente", "errors": errors}), 207
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
            empleados.append({
                'codigo': codigo,
                'nombre': nombre,
                'puesto': puesto,
            })
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

        for actividad in root.findall('actividad'):
            id_actividad = actividad.get('id')

            # Validar ID
            if id_actividad in existing_ids:
                errors.append(f"ID repetido en actividad: {id_actividad}")
                continue  # Saltar al siguiente actividad sin añadir esta

            existing_root.append(actividad)
            existing_ids.add(id_actividad)

        existing_tree.write(ACTIVITIES_FILE, encoding="utf-8", xml_declaration=True)

        if errors:
            return jsonify({"success": "Algunas actividades cargadas correctamente", "errors": errors}), 207
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

            actividades.append({
                'id': id_actividad,
                'nombre': nombre,
                'descripcion': descripcion,
                'empleado': empleado,
                'dia': dia,
                'hora': hora,
            })
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
    try:
        # Obtener nombre del producto y cantidad desde el frontend
        data = request.form  # Cambiado a form si los datos se envían como formulario
        nombre_producto = data.get('nombre_producto')
        cantidad = data.get('cantidad')

        if not nombre_producto or not cantidad:
            print("Faltan datos obligatorios (nombre_producto o cantidad)")
            return jsonify({"error": "Faltan datos obligatorios (nombre_producto o cantidad)"}), 400

        # Cargar el archivo de productos
        tree_productos = ET.parse(PRODUCTS_FILE)
        root_productos = tree_productos.getroot()

        # Buscar el producto por nombre
        producto_encontrado = None
        for producto in root_productos.findall('producto'):
            nombre = producto.find('nombre').text
            if nombre == nombre_producto:
                producto_encontrado = producto
                break

        if producto_encontrado is None:
            print(f"No se encontró el producto '{nombre_producto}'")
            return jsonify({"error": f"No se encontró el producto '{nombre_producto}'"}), 404

        # Obtener detalles del producto
        id_producto = producto_encontrado.get('id')
        nombre = producto_encontrado.find('nombre').text

        # Crear un elemento para el carrito de compras
        carrito_element = ET.Element('producto')
        carrito_element.set('id', id_producto)

        # Añadir subelementos al carrito de compras
        ET.SubElement(carrito_element, 'nombre').text = nombre
        ET.SubElement(carrito_element, 'cantidad').text = str(cantidad)

        # Añadir al archivo XML del carrito de compras de la misma forma que en carga_masiva
        if not os.path.exists(CART_FILE):
            root_carrito = ET.Element('cart')
        else:
            tree_carrito = ET.parse(CART_FILE)
            root_carrito = tree_carrito.getroot()

        # Verificar si ya existe un producto con el mismo ID en el carrito
        for elemento_carrito in root_carrito.findall('producto'):
            if elemento_carrito.get('id') == id_producto:
                # Si existe, aumentar la cantidad en lugar de agregar uno nuevo
                cantidad_actual = int(elemento_carrito.find('cantidad').text)
                nueva_cantidad = cantidad_actual + int(cantidad)
                elemento_carrito.find('cantidad').text = str(nueva_cantidad)
                break
        else:
            # Si no existe, agregar el nuevo producto al carrito
            root_carrito.append(carrito_element)

        # Indentar el XML (es opcional pero útil para legibilidad)
        indentar(root_carrito)
        
        # Escribir el archivo XML del carrito de compras
        tree_carrito = ET.ElementTree(root_carrito)
        tree_carrito.write(CART_FILE, encoding="utf-8", xml_declaration=True)

        return jsonify({"success": f"Producto '{nombre_producto}' añadido al carrito correctamente"}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500
    
# Endpoint para obtener los productos del carrito de compras
@app.route('/descarga_carrito', methods=['GET'])
def descarga_carrito():
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

@app.route('/comprar', methods=['POST'])
def comprar():
    global username
    try:
        #leyendo el Purchases_file para saber el numero de compra que se va a realizar
        tree = ET.parse(PURCHASES_FILE)
        root = tree.getroot()
        num_compra = str(len(root.findall('compra')) + 1)
        
        id_usuario = username
        
        #buscando el nombre del usuario en el archivo de usuarios
        tree_usuarios = ET.parse(USERS_FILE)
        root_usuarios = tree_usuarios.getroot()
        nombre_usuario = ""
        for usuario in root_usuarios.findall('usuario'):
            if usuario.get('id') == id_usuario:
                nombre_usuario = usuario.find('nombre').text
                break
        
        #leyendo el archivo del carrito de compras para obtener los productos y la cantidad 
        tree_carrito = ET.parse(CART_FILE)
        root_carrito = tree_carrito.getroot()
        productos = []
        total = 0
        for producto in root_carrito.findall('producto'):
            #obteniendo el nombre del producto y la cantidad 
            nombre_producto = producto.find('nombre').text
            cantidad = int(producto.find('cantidad').text)
            #buscando el producto en el archivo de productos
            tree_productos = ET.parse(PRODUCTS_FILE)
            root_productos = tree_productos.getroot()
            for producto_xml in root_productos.findall('producto'):
                if producto_xml.find('nombre').text == nombre_producto:
                    precio = float(producto_xml.find('precio').text)
                    total += precio * cantidad
                    #restando la cantidad comprada al xml de productos
                    cantidad_actual = int(producto_xml.find('cantidad').text)
                    producto_xml.find('cantidad').text = str(cantidad_actual - cantidad)
                    #guardando los cambios 
                    tree_productos.write(PRODUCTS_FILE, encoding="utf-8", xml_declaration=True)
                    #agregando el producto a la lista de productos                    
                    productos.append({
                        'id': producto_xml.get('id'),
                        'nombre': nombre_producto,
                        'cantidad': str(cantidad)
                    })
                    break
                
        if not all([num_compra, id_usuario, nombre_usuario, total, productos]):
            return jsonify({"error": "Faltan datos obligatorios"}), 400

        # Crear el elemento de la compra
        compra_element = ET.Element('compra')
        compra_element.set('numero', num_compra)

        usuario_element = ET.SubElement(compra_element, 'usuario')
        usuario_element.set('id', id_usuario)
        usuario_element.text = nombre_usuario

        total_element = ET.SubElement(compra_element, 'Total')
        total_element.text = str(total)

        productos_element = ET.SubElement(compra_element, 'productos')

        for producto in productos:
            producto_element = ET.SubElement(productos_element, 'producto')
            producto_element.set('id', producto.get('id'))

            nombre_element = ET.SubElement(producto_element, 'nombre')
            nombre_element.text = producto.get('nombre')

            cantidad_element = ET.SubElement(producto_element, 'cantidad')
            cantidad_element.text = str(producto.get('cantidad'))

        # Parsear el archivo de compras
        tree_compras = ET.parse(PURCHASES_FILE)
        root_compras = tree_compras.getroot()

        # Añadir la nueva compra al archivo XML
        root_compras.append(compra_element)

        # Indentar el XML
        indent(root_compras)

        # Escribir el archivo XML de compras
        tree_compras = ET.ElementTree(root_compras)
        tree_compras.write(PURCHASES_FILE, encoding="utf-8", xml_declaration=True)
        
        # Limpiar el archivo del carrito de compras
        root_carrito.clear()
        tree_carrito.write(CART_FILE, encoding="utf-8", xml_declaration=True)
        

        return jsonify({"success": "Compra añadida correctamente"}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

#Endpoint para descargar el archivo de compras
@app.route('/descarga_compras', methods=['GET'])
def descarga_compras():
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

if __name__ == '__main__':
    app.run(debug=True)
