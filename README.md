# NoSQL Injection App

Esta es una aplicación web simple desarrollada en Ubuntu linux con el IDE Visual Studio Code, el lenguaje Python3 (Flask) y MongoDB que simula una vulnerabilidad NoSQL. Fue creada con fines educativos, para aprender cómo funcionan las inyecciones NoSQL y cómo se pueden evitar.

---

# Objetivo

Demostrar cómo una aplicación vulnerable puede permitir el acceso no autorizado a través de una inyección NoSQL en los campos de login.

---

# Tecnologías utilizadas

- Ubuntu Linux 24.04
- Visual Studio Code 1.99.1
- Python3 3.12.3
- Flask
- MongoDB (Atlas)
- HTML 
- Git

---

# Instalación y ejecución

# Instalación de Python y pip en Ubuntu

Si aún no tienes Python 3, pip ni git instalados en tu sistema, puedes hacerlo ejecutando los siguientes comandos:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
sudo apt install git
```

# 1. Instalar Visual Studio Code

```
Puedes instalar el IDE de su página oficial: https://code-visualstudio-com.translate.goog/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
```

# 2. Clonar el repositorio o descargarlo direcramente de github en .zip

```bash
git clone git@github.com:EmilianoLeonel08/nosql_injection.git
cd nosql_injection
```
```
https://github.com/EmilianoLeonel08/nosql_injection/archive/refs/heads/master.zip
```

# 3. Abrir Visual Studio Code y descomprimir .zip

```
Descomprimer el archivo .zip
Abre Visual Studio Code.
Haz clic en File (Archivo) en la barra de menú.
Selecciona Open Folder (Abrir carpeta).
Navega hasta la carpeta nosql_injection que clonaste o descomprimiste y selecciónala.
```

# 4. Crear un entorno virtual 

```bash
Abre tu terminal en Visual Studio Code y ejecuta:
python3 -m venv venv
source venv/bin/activate
```

# 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

# 6. Ejecutar la app

```bash
python app.py
```

Luego abre tu navegador en: [http://localhost:5000](http://localhost:5000)

---

# Conexión a MongoDB

La aplicación se conecta a un clúster de MongoDB en la nube con la siguiente cadena de conexión:

```
mongodb+srv://student:dPgF0sb0ADBUZHCI@clusterunam.6pxlppf.mongodb.net/?retryWrites=true&w=majority&appName=ClusterUNAM
```

Base de datos: `nosqlapp`  
Colección: `users`

---

# Cómo probar la vulnerabilidad NoSQL

1. En el formulario de login, intenta escribir cualquier cosa (o nada) como usuario y contraseña y verás un mensaje de error.

2. Para explotar la vulnerabilidad, ingresa lo siguiente en **Usuario y Contraseña**:

```json
{"$ne": None}
```

Este es un operador de MongoDB que significa "no igual a None". Debido a que no se valida el tipo de entrada, Mongo lo interpreta como una condición válida y permite el acceso si encuentra cualquier usuario con cualquier contraseña.Debido a que la aplicación convierte la entrada del usuario directamente a una estructura de Python (por ejemplo usando eval()), Mongo interpreta esto como una consulta válida: "el campo no debe ser igual a None". Como no se hace validación, se permite el acceso.

---

# ¿Qué es una inyección NoSQL?

Es un tipo de ataque en el que el atacante manipula consultas a bases de datos NoSQL (como MongoDB) para obtener acceso no autorizado o extraer información confidencial.

**Este proyecto intencionalmente omite validaciones de entrada**, lo que lo hace vulnerable. **No implementes este patrón en producción.**

---

# Estructura del proyecto

```
nosql_injection/
│
├── app.py                 # Lógica principal del backend
├── templates/
│   └── login.html         # Interfaz del usuario (frontend)
├── static/                # Archivos estáticos (opcional)
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Este archivo
```

---

# Autor

**Darío Emiliano León Lara**  
Repositorio: [github.com/EmilianoLeonel08/nosql_injection](https://github.com/EmilianoLeonel08/nosql_injection)

---

## Aviso

Este proyecto es solo para fines educativos. No se debe usar en entornos reales sin las debidas medidas de seguridad.
