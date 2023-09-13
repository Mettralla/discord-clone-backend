"""Modelo de servidor"""


class Server:
    """Class Server Inicializar"""

    def __init__(self, server_id, server_name, server_description, owner_id):
        self.server_id = server_id
        self.server_name = server_name
        self.server_description = server_description
        self.owner_id = owner_id
