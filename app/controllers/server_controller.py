"""Server Controller"""

from flask import request, jsonify, session
from ..models.server_model import Server
from ..controllers.auth_controller import AuthController
from ..models.exceptions import InvalidDataError


class ServerController:
    """Class Server Controller"""

    @classmethod
    @AuthController.login_required
    def create_server(cls):
        """Create Server"""
        server_data = request.json
        try:
            server = Server.validate_data(server_data)
            Server.create_server(server)
            return jsonify({"message": "Server created successfully"}), 201
        except InvalidDataError as e:  # pylint: disable = invalid-name
            return jsonify({"error": str(e)}), 400

    @classmethod
    @AuthController.login_required
    def get_servers(cls):
        """Get Servers"""
        server_name = request.args.get("server_name")
        servers = Server.get_servers(server_name)
        response = {"servers": [], "total": 0}

        if servers:
            servers_list = []
            for server in servers:
                server_dict = {
                    "server_id": server.server_id,
                    "server_name": server.server_name,
                    "server_description": server.server_description,
                    "owner_id": server.owner_id,
                }
                servers_list.append(server_dict)

            response["servers"] = servers_list
            response["total"] = len(servers_list)
            return jsonify(response), 200

        return jsonify(response), 200

    @classmethod
    @AuthController.login_required
    def get_server(cls, server_id):
        """Get Server"""
        if Server.exist(server_id):
            server = Server.get_server(server_id)
            if server:
                server_dict = {
                    "server_id": server.server_id,
                    "server_name": server.server_name,
                    "server_description": server.server_description,
                    "owner_id": server.owner_id,
                }
                return jsonify(server_dict), 200
        return jsonify({"error": "Server not found"}), 404

    @classmethod
    @AuthController.login_required
    def update_server(cls, server_id):
        """Update Server"""
        update_data = request.json
        user_id = session.get("user_id")

        if Server.exist(server_id, user_id):
            updated_fields = {}
            if "server_name" in update_data:
                updated_fields["server_name"] = update_data["server_name"]

            if "server_description" in update_data:
                updated_fields["server_description"] = update_data["server_description"]

            if updated_fields:
                Server.update_server(server_id, updated_fields)
                return jsonify({"message": "Server updated successfully"}), 200

            return jsonify({"message": "No valid fields to update"}), 400
        else:
            return jsonify({"error": "Server not found or you are not the owner"}), 404

    @classmethod
    @AuthController.login_required
    def delete_server(cls, server_id):
        """Delete Server"""
        if Server.exist(server_id):
            Server.delete_server(server_id)
            return jsonify({"message": "Server deleted successfully"}), 204
        return jsonify({"error": "Server not found"}), 404
