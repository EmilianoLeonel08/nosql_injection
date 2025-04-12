from flask import Flask, request, render_template
from pymongo import MongoClient
import ast  

app = Flask(__name__)

# Conexión a MongoDB
client = MongoClient("mongodb+srv://student:dPgF0sb0ADBUZHCI@clusterunam.6pxlppf.mongodb.net/?retryWrites=true&w=majority&appName=ClusterUNAM")
db = client["nosqlapp"]
users = db["users"]


if users.count_documents({"username": "admin"}) == 0:
    users.insert_one({
        "username": "admin",
        "password": "admin"
    })
    print("✅ Usuario de prueba creado: admin / admin123")

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        
        try:
            username = ast.literal_eval(request.form['username'])
        except:
            username = request.form['username']

        try:
            password = ast.literal_eval(request.form['password'])
        except:
            password = request.form['password']

  
        user = users.find_one({
            "username": username,
            "password": password
        })

        if user:
            message = f"¡Bienvenido, {username}!"
        else:
            message = "Usuario o contraseña incorrectos."

    return render_template("login.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)
