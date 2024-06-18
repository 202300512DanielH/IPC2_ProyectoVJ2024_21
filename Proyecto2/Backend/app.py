from flask import Flask, request, jsonify
from flask_cors import CORS 
import xml.etree.ElementTree as ET
import os

app = Flask(__name__)
CORS(app)

# Inicializa el archivo xml donde se almacenan los archivos si no existe
DATA_DIR = 'data/uploads'
USERS_FILE = os.path.join(DATA_DIR, 'users.xml')
PRODUCTS_FILE = os.path.join(DATA_DIR, 'products.xml')
EMPLOYEES_FILE = os.path.join(DATA_DIR, 'employees.xml')
ACTIVITIES_FILE = os.path.join(DATA_DIR, 'activities.xml')

# Asegura que el directorio exista
os.makedirs(DATA_DIR, exist_ok=True)

# Crea archivos XML vacíos si no existen
for file in [USERS_FILE, PRODUCTS_FILE, EMPLOYEES_FILE, ACTIVITIES_FILE]:
    if not os.path.exists(file):
        root = ET.Element(os.path.splitext(os.path.basename(file))[0])
        tree = ET.ElementTree(root)
        tree.write(file)

# Usuarios estáticos para login (no me dejaron usar pandas pipipi)
users = {}

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
    load_users()
    username = request.form.get('username')
    password = request.form.get('password')
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
        return jsonify({'error': 'No se selecciono ningun archivo'}), 400
    response, status = cargar_datos_masivos(file, USERS_FILE, 'usuario')
    return jsonify(response), status

# Endpoint para obtener los usuarios del xml de usuarios
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

# Endpoint para cargar masivamente productos al archivo xml de productos
@app.route('/carga_masiva_productos', methods=['POST'])
def carga_masiva_productos():
    if 'file' not in request.files:
        return jsonify({'error': 'No hay archivo para cargar'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 400
    response, status = cargar_datos_masivos(file, PRODUCTS_FILE, 'producto')
    return jsonify(response), status

# Endpoint para obtener los productos del xml de productos
@app.route('/get_products', methods=['GET'])
def get_products():
    try:
        tree = ET.parse(PRODUCTS_FILE)
        root = tree.getroot()
        productos = []
        for elemento_producto in root.findall('producto'):
            id = elemento_producto.get('id')
            nombre = elemento_producto.find('nombre').text if elemento_producto.find('nombre') is not None else ""
            precio = elemento_producto.find('precio').text if elemento_producto.find('precio') is not None else ""
            descripcion = elemento_producto.find('descripcion').text if elemento_producto.find('descripcion') is not None else ""
            categoria = elemento_producto.find('categoria').text if elemento_producto.find('categoria') is not None else ""
            cantidad = elemento_producto.find('cantidad').text if elemento_producto.find('cantidad') is not None else ""
            imagen = elemento_producto.find('imagen').text if elemento_producto.find('imagen') is not None else ""
            productos.append({
                'id': id,
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
    response, status = cargar_datos_masivos(file, EMPLOYEES_FILE, 'empleado')
    return jsonify(response), status

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
        return jsonify({'error': 'No se selecciono ningun archivo'}), 400
    response, status = cargar_datos_masivos(file, ACTIVITIES_FILE, 'actividad')
    return jsonify(response), status

# Endpoint para obtener las actividades del xml de actividades
@app.route('/get_activities', methods=['GET'])
def get_activities():
    try:
        tree = ET.parse(ACTIVITIES_FILE)
        root = tree.getroot()
        actividades = []
        for elemento_actividad in root.findall('actividad'):
            id = elemento_actividad.get('id')
            nombre = elemento_actividad.find('nombre').text if elemento_actividad.find('nombre') is not None else ""
            descripcion = elemento_actividad.find('descripcion').text if elemento_actividad.find('descripcion') is not None else ""
            empleado = elemento_actividad.find('empleado').text if elemento_actividad.find('empleado') is not None else ""
            dia = elemento_actividad.find('dia').text if elemento_actividad.find('dia') is not None else ""
            hora = elemento_actividad.get('hora', "")
            actividades.append({
                'id': id,
                'nombre': nombre,
                'descripcion': descripcion,
                'empleado': empleado,
                'dia': dia,
                'hora': hora,
            })
        return jsonify(actividades), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/protected', methods=['GET'])
def protected():
    # Aquí tenemos el recurso protegido
    return jsonify({"msg": "Has accedido al recurso protegido"}), 200

if __name__ == '__main__':
    app.run(debug=True)
