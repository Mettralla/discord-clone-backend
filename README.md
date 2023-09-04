<h3 align="center">Discord Clone API</h3>

---

Se busca desarrollar una aplicación web para un sistema de mensajería, similar a Discord.
Dicha aplicación debe permitir registrar usuarios, los cuales podrán crear o unirse a uno o más servidores.
Un servidor es un espacio que puede contener usuarios y a su vez canales. Un canal puede ser creado dentro de un servidor en concreto, y únicamente por un usuario perteneciente a dicho servidor. Cada canal define el nombre de un único chat, el cual es un registro histórico de los mensajes enviados por los usuarios.

---

## 📝 Tabla de Contenidos
- [Instalación/Ejecucion](#getting_started)
- [Flujo de trabajo](#workflow)
- [Base de Datos](#der)
- [Autor](#authors)

## 🏁 Instalación/Ejecución <a name = "getting_started"></a>

Crear entorno virtual

```bash
python -m venv env
```

Activar entorno

```bash
source env/Scripts/activate
```

Clonar el repositorio

```bash
git clone git@github.com:Mettralla/discord-clone-backend.git
```

Ir al directorio del proyecto

```bash
cd discord-clone-backend
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Crear archivo `.env` e ingresar credenciales de MYSQL

```bash
# ./.env
MYSQL_USER = "root"
MYSQL_PASSWORD = "password"
```

Migrar la base de datos
```bash
python migrate.py
```

Iniciar programa

```bash
python run.py
```

## ⛏️ Flujo de Trabajo <a name = "workflow"></a>

Moverse a rama develop

```bash
git checkout develop
```

Crear rama feature para nueva tarea

```bash
git checkout -b nueva-feature
```

Se hace los cambios

```bash
git add .
git commit -m "Agregando nueva feature"
```

Seguimos trabajanado

```bash
git add .
git commit -m "Feature terminada"
```

Enviarla a develop

```bash
git checkout develop
git merge nueva-feature
```

Eliminar la rama
```bash
git branch -d nueva-feature
```

## ⛏️ Base de datos <a name = "der"></a>

<p align="center">
 <img src=https://drive.google.com/uc?export=view&id=1jsPq7SZ-81qWtVzpnBVNL5HvJHHvHyek alt="Banner"></a>
</p>

## ✍️ Autor <a name = "authors"></a>
- Fernando Maldonado ()
- Edgardo Lamas ([@Edgardo768](https://github.com/edgardo768))
- Daniel Tejerina ([@mettralla](https://github.com/mettralla)) 
