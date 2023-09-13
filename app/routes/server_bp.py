"""Blueprint del servidor"""

from flask import Blueprint, request, jsonify
from ..controllers.server_controller import ServerController

server_bp = Blueprint("server_bp", __name__)


@server_bp.route("/", methods=["POST"])
def create_server():
    data = request.json
    server_name = data["server_name"]
    server_description = data.get("server_description", None)
    owner_id = data["owner_id"]

    ServerController.create_server(server_name, server_description, owner_id)

    return jsonify({"message": "Server created successfully"}), 201


@server_bp.route("/<int:server_id>", methods=["PUT"])
def update_server(server_id):
    data = request.json
    server_name = data.get("server_name", None)
    server_description = data.get("server_description", None)

    server = ServerController.update_server(server_id, server_name, server_description)

    if server is not None:
        return jsonify({"message": "Server updated successfully"}), 200
    else:
        return jsonify({"message": "Server not found"}), 404


@server_bp.route("/", methods=["GET"])
def get_servers():
    servers = ServerController.get_all_servers()
    response_data = [
        {
            "server_id": server.server_id,
            "server_name": server.server_name,
            "server_description": server.server_description,
            "owner_id": server.owner_id,
        }
        for server in servers
    ]
    return jsonify({"servers": response_data, "total": len(servers)}), 200


@server_bp.route("/servers/<int:server_id>", methods=["GET"])
def get_server(server_id):
    server = ServerController.get_server_by_id(server_id)
    if server is not None:
        return (
            jsonify(
                {
                    "server_id": server.server_id,
                    "server_name": server.server_name,
                    "server_description": server.server_description,
                    "owner_id": server.owner_id,
                }
            ),
            200,
        )
    else:
        return jsonify({"message": "Server not found"}), 404


@server_bp.route("/servers/<int:server_id>", methods=["DELETE"])
def delete_server(server_id):
    ServerController.delete_server(server_id)
    return jsonify({"message": "Server deleted successfully"}), 204
