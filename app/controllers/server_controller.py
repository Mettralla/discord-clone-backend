"""Server Controller"""

from flask import request, jsonify, session
from ..models.server_model import Server
from ..models.exceptions import NotFound, ForbiddenAction
from ..controllers.auth_controller import AuthController


class ServerController:
    """Class Server Controller"""

    @classmethod
    @AuthController.login_required
    def create_server(cls):
        """Create Server"""
        server_data = request.json
        owner_id = session["user_id"]

        # Validate data and create the server object
        server = Server.validate_data(
            {
                "server_name": server_data.get("server_name"),
                "server_description": server_data.get("server_description"),
                "owner_id": owner_id,
            }
        )

        # Create the server in the database
        Server.create_server(server)
        return jsonify({"message": "Server created successfully"}), 201

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
        server = Server.get_server(server_id)
        if server:
            server_dict = {
                "server_id": server.server_id,
                "server_name": server.server_name,
                "server_description": server.server_description,
                "owner_id": server.owner_id,
            }
            return jsonify(server_dict), 200

        raise NotFound(server_id, "server")

    @classmethod
    @AuthController.login_required
    def update_server(cls, server_id):
        """Update Server"""
        update_data = request.json
        updated_fields = {}

        if "server_name" in update_data:
            updated_fields["server_name"] = update_data["server_name"]

        if "server_description" in update_data:
            updated_fields["server_description"] = update_data["server_description"]

        if updated_fields:
            if not Server.exist(server_id):
                raise NotFound(server_id, "server")

            server = Server.get_server(server_id)
            if server.owner_id != session["user_id"]:
                raise ForbiddenAction()

            Server.update_server(server_id, updated_fields)
            return jsonify({"message": "Server updated successfully"}), 200

        return jsonify({"message": "No valid fields to update"}), 400

    @classmethod
    @AuthController.login_required
    def delete_server(cls, server_id):
        """Delete Server"""
        if not Server.exist(server_id):
            raise NotFound(server_id, "server")

        server = Server.get_server(server_id)
        if server.owner_id != session["user_id"]:
            raise ForbiddenAction()

        Server.delete_server(server_id)
        return jsonify({"message": "Server deleted successfully"}), 204
