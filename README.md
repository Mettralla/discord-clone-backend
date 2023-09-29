<h3 align="center">Discord Clone API</h3>

---

Este repositorio se enfoca en el desarrollo de una aplicación web de mensajería, similar a Discord. Los usuarios pueden registrarse y crear o unirse a servidores. Cada servidor es un espacio que aloja usuarios y canales, donde un canal es creado exclusivamente por un miembro del servidor y representa un chat con un historial de mensajes.

---

## 📝 Tabla de Contenidos
- [Estructura del Proyecto](#project_structure)
- [Instalación/Ejecucion](#getting_started)
- [Base de Datos](#der)
- [Autores](#authors)

## 🏁 Estructura del Proyecto <a name = "project_structure"></a>

Antes de ejecutar el proyecto, es necesario clonar ambos repositorios (frontend y backend) en la misma raíz. A continuación, encontrarás los enlaces a los repositorios:

- Frontend: El frontend de la aplicación está desarrollado utilizando HTML, CSS y JavaScript. Puedes encontrar el código fuente en el siguiente repositorio: Enlace al Repositorio Frontend

- Backend: El backend de la aplicación está implementado con Flask. Puedes acceder al código fuente en el repositorio dedicado: Enlace al Repositorio Backend

Para obtener información detallada sobre cómo configurar y ejecutar el proyecto, consulta la sección [Instalación/Ejecucion](#getting_started) a continuación.

### Estructura:

    .
    ├── discord-clone-backend           
    |   ├── app/                             
    │   │   ├── controllers/ 
    |   |   ├── models/ 
    |   |   ├── routes/ 
    |   |   ├── static/
    |   |   ├── __init__.py
    │   │   └── database.py                 
    |   ├── env/                         
    |   ├── .gitignore                   
    |   ├── README.md                    
    |   ├── config.py                    
    |   ├── migrate.py                   
    |   ├── requirements.txt             
    |   ├── .env                         
    │   └── run.py                       
    ├── discord-clone-frontend
    |   ├── css/                             
    │   ├── img/ 
    |   ├── js/ 
    |   ├── pages/        
    |   ├── README.md                    
    |   └── index.html                   
    .


## 🏁 Instalación/Ejecución <a name = "getting_started"></a>

Clonar el repositorio backend

```bash
git clone https://github.com/Mettralla/discord-clone-backend.git
```

Ir al directorio del proyecto

```bash
cd discord-clone-backend
```

Crear entorno virtual

```bash
python -m venv env
```

Activar entorno

```bash
source env/Scripts/activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Crear archivo `.env` e ingresar credenciales de MYSQL y SECRET_KEY

```bash
# ./.env
MYSQL_USER = "root"
MYSQL_PASSWORD = "password"
SECRET_KEY = "secret_key"
```

Migrar la base de datos
```bash
python migrate.py
```

Iniciar backend

```bash
python run.py
```

Volver al directorio padre

```bash
cd ..
```

Clonar el repositorio frontend

```bash
git clone https://github.com/Mettralla/discord-clone-frontend.git
```

Ir al directorio del proyecto

```bash
cd discord-clone-frontend
```

Iniciar live server en index.html

## ⛏️ Base de datos <a name = "der"></a>

<p align="center">
 <img src=https://drive.google.com/uc?export=view&id=1jsPq7SZ-81qWtVzpnBVNL5HvJHHvHyek alt="Banner"></a>
</p>

## ✍️ Autores <a name = "authors"></a>
- Fernando Maldonado ([@Ferco7](https://github.com/Ferco7))
- Daniel Tejerina ([@mettralla](https://github.com/mettralla)) 
