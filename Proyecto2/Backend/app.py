from flask import Flask, request, jsonify
from flask_cors import CORS 
import xml.etree.ElementTree as ET
import os

app = Flask(__name__)
CORS(app)

# Inicializa el archivo xml donde se almacenan los usuarios si no existe
USERS_FILE = 'data/uploads/users.xml'
if not os.path.exists(USERS_FILE):
    root = ET.Element('users')
    tree = ET.ElementTree(root)
    tree.write(USERS_FILE)

users = {
    "testuser": "testpassword"
}

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username in users and users[username] == password:
        return jsonify({"msg": "Login Exitoso"}), 200
    else:
        return jsonify({"msg": "Usuario o contraseña incorrecta"}), 401

# Endpoint para obtener los usuarios del xml de usuarios 
@app.route('/get_users', methods=['GET'])
def get_users():
    try:
        tree = ET.parse(USERS_FILE)
        root = tree.getroot()
        usuarios = []
        for elemento_usuario in root.findall('usuario'):
            id = elemento_usuario.get('id')
            password = elemento_usuario.get('password')
            nombre = elemento_usuario.find('nombre').text
            edad = elemento_usuario.find('edad').text
            email = elemento_usuario.find('email').text
            telefono = elemento_usuario.find('telefono').text
            usuarios.append({
                'id': id,
                'nombre': nombre,
                'edad': edad,
                'email': email,
                'telefono': telefono,
                'password': password
            })
        return jsonify(usuarios)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para cargar masivamente usuarios al archivo xml de usuarios
@app.route('/carga_masiva_usuarios', methods=['POST'])
def carga_masiva_usuarios():
    if 'file' not in request.files:
        return jsonify({'error': 'No hay archivo para cargar'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No se selecciono ningun archivo'}), 400
    if file:
        try:
            tree = ET.parse(file)
            new_root = tree.getroot()
            existing_tree = ET.parse(USERS_FILE)
            existing_root = existing_tree.getroot()
            for user in new_root.findall('usuario'):
                existing_root.append(user)
            existing_tree.write(USERS_FILE)
            return jsonify({'success': 'Archivo procesado y cargado correctamente todos los usuarios al xml de persistencia'}), 200
        except ET.ParseError:
            return jsonify({'error': 'Error en el parseo del xml'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@app.route('/protected', methods=['GET'])
def protected():
    # Aquí tenemos el recurso protegido
    return jsonify({"msg": "Has accedido al recurso protegido"}), 200

if __name__ == '__main__':
    app.run(debug=True)
