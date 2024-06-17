from flask import Flask, request, jsonify

app = Flask(__name__)

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

@app.route('/protected', methods=['GET'])
def protected():
    # Aquí tenemos el recurso protegido
    return jsonify({"msg": "Has accedido al recurso protegido"}), 200

if __name__ == '__main__':
    app.run(debug=True)
