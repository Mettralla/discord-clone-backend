"""Server Controller"""

from flask import request, jsonify
from ..models.server_model import Server
from ..models.exceptions import NotFound

class ServerController:
    @classmethod
    def create_server(cls):
        server_data = request.json
        server = Server(
            server_name=server_data.get("server_name"),
            server_description=server_data.get("server_description"),
            owner_id=server_data.get("owner_id")
        )
        Server.create_server(server)
        return jsonify({"message": "Server created successfully"}), 201

    @classmethod
    def get_servers(cls):
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
                    "owner_id": server.owner_id
                }
                servers_list.append(server_dict)

            response["servers"] = servers_list
            response["total"] = len(servers_list)
            return jsonify(response), 200
        else:
            return jsonify(response), 200

    @classmethod
    def get_server(cls, server_id):
        server = Server.get_server(server_id)
        if server:
            server_dict = {
                "server_id": server.server_id,
                "server_name": server.server_name,
                "server_description": server.server_description,
                "owner_id": server.owner_id
            }
            return jsonify(server_dict), 200
        else:
            raise NotFound(server_id, "server")

    @classmethod
    def update_server(cls, server_id):
        update_data = request.json
        Server.update_server(server_id, update_data)
        return jsonify({"message": "Server updated successfully"}), 200

    @classmethod
    def delete_server(cls, server_id):
        if Server.get_server(server_id):
            Server.delete_server(server_id)
            return jsonify({"message": "Server deleted successfully"}), 204
        else:
            raise NotFound(server_id, "server")
