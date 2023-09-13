"""Controlador de servidor"""

from ..models.server_model import Server

class ServerController:
    servers = []

    @classmethod
    def create_server(cls, server_name, server_description, owner_id):
        server_id = len(cls.servers) + 1
        server = Server(server_id, server_name, server_description, owner_id)
        cls.servers.append(server)
        return server

    @classmethod
    def update_server(cls, server_id, server_name=None, server_description=None):
        for server in cls.servers:
            if server.server_id == server_id:
                if server_name:
                    server.server_name = server_name
                if server_description:
                    server.server_description = server_description
                return server

    @classmethod
    def get_all_servers(cls):
        return cls.servers

    @classmethod
    def get_server_by_id(cls, server_id):
        for server in cls.servers:
            if server.server_id == server_id:
                return server

    @classmethod
    def delete_server(cls, server_id):
        for server in cls.servers:
            if server.server_id == server_id:
                cls.servers.remove(server)
                return
