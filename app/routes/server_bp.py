"""Server bp"""


from flask import Blueprint, request, jsonify
from ..controllers.server_controller import ServerController

server_bp = Blueprint("server", __name__)
server_controller = ServerController()


@server_bp.route("/create_server", methods=["POST"])
def create_server():
    """Funcion crear server"""
    data = request.json
    server_id = data.get("server_id")
    name = data.get("name")
    description = data.get("description")

    server_controller.create_server(server_id, name, description)

    return jsonify({"message": "Server created successfully"}), 201


@server_bp.route("/get_server/<int:server_id>", methods=["GET"])
def get_server(server_id):
    """Funcion obtener server"""
    server = server_controller.get_server_by_id(server_id)
    if server:
        return (
            jsonify(
                {
                    "server_id": server.server_id,
                    "name": server.name,
                    "description": server.description,
                }
            ),
            200,
        )
    else:
        return jsonify({"message": "Server not found"}), 404
