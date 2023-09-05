"""Blueprint del servidor"""

from flask import Blueprint, request, jsonify
from ..controllers.server_controller import ServerController

server_bp = Blueprint("server", __name__)
server_controller = ServerController()


@server_bp.route("/servers", methods=["POST"])
def create_server_route():
    """Crear servidor"""
    # Obtener los datos del servidor desde la solicitud
    data = request.get_json()
    server_name = data.get("server_name")
    server_description = data.get("server_description", "")  # Valor opcional
    owner_id = data.get("owner_id")

    # Puedes agregar lógica de validación de datos aquí si es necesario

    # Llama al método para crear el servidor en el controlador existente
    server_controller.create_server(server_name, server_description, owner_id)

    # Devuelve una respuesta con el código de estado 201 y un mensaje de éxito
    return jsonify({"message": "Servidor creado exitosamente"}), 201
