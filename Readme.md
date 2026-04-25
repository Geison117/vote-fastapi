# 🗳️ Vote FastAPI

Backend API desarrollada con FastAPI para gestionar un sistema de votación. Permite crear, listar y votar sobre diferentes opciones de manera eficiente y escalable.

## 🚀 Características

* API REST construida con FastAPI
* Validación de datos con Pydantic
* Arquitectura modular
* Manejo de votos en tiempo real
* Documentación automática con Swagger/OpenAPI
* Código limpio y fácil de extender

## 🛠️ Tecnologías

* Python 3.x
* FastAPI
* Uvicorn
* Pydantic
* (Opcional: SQLAlchemy / Base de datos si aplica)

## 📂 Estructura del proyecto

```bash
vote-fastapi/
│── app/
│   ├── main.py          # Punto de entrada
│   ├── models.py        # Modelos de datos
│   ├── schemas.py       # Esquemas (Pydantic)
│   ├── routers/         # Endpoints
│   ├── database.py      # Configuración DB (si aplica)
│
│── requirements.txt
│── README.md
```

## ⚙️ Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Geison117/vote-fastapi.git
cd vote-fastapi
```

2. Crea un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

## ▶️ Ejecución

```bash
uvicorn app.main:app --reload
```

Servidor disponible en:

```
http://127.0.0.1:8000
```

## 📄 Documentación interactiva

FastAPI genera documentación automáticamente:

* Swagger UI:
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* Redoc:
  👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📌 Endpoints principales

Ejemplo (ajusta según tu código real):

* `GET /votes` → Obtener todas las votaciones
* `POST /votes` → Crear una votación
* `POST /votes/{id}/vote` → Votar por una opción
* `GET /votes/{id}` → Obtener detalle de una votación

## 🧪 Testing

```bash
pytest
```

## 👨‍💻 Autor

* Geison Blanco
* GitHub: [https://github.com/Geison117](https://github.com/Geison117)