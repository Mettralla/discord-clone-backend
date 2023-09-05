"""Control del servidor"""

from ..models.server_model import Server


class ServerController:
    """Clase control del servidor"""

    def __init__(self):
        self.servers = []

    def create_server(self, server_id, name, description):
        """Funcion para crear el servidor"""
        server = Server(server_id, name, description)
        self.servers.append(server)

    def get_server_by_id(self, server_id):
        """Funcion para obtener el servidor por id"""
        for server in self.servers:
            if server.server_id == server_id:
                return server
        return None
