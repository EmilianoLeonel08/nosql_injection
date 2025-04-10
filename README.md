# NoSQL Injection App

Esta es una aplicación web simple construida en el IDE Visual Studio Code con Python (Flask) y MongoDB que simula una vulnerabilidad NoSQL. Fue creada con fines educativos, para aprender cómo funcionan las inyecciones NoSQL y cómo se pueden evitar.

---

# Objetivo

Demostrar cómo una aplicación vulnerable puede permitir el acceso no autorizado a través de una inyección NoSQL en los campos de login.

---

# Tecnologías utilizadas

- Python 3
- Flask
- MongoDB (Atlas)
- HTML (interfaz básica)
- Git

---

# Instalación y ejecución

# 1. Clonar el repositorio

```bash
git clone git@github.com:EmilianoLeonel08/nosql_injection.git
cd nosql_injection
```

# 2. Crear un entorno virtual 

```bash
python3 -m venv venv
source venv/bin/activate
```

# 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

# 4. Ejecutar la app

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
