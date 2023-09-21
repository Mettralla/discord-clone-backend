"""Server Model"""

from ..database import DatabaseConnection
from ..models.exceptions import InvalidDataError


class Server:
    """Class Server"""

    def __init__(self, **kwargs):
        self.server_id = kwargs.get("server_id", None)
        self.server_name = kwargs.get("server_name", None)
        self.server_description = kwargs.get("server_description", None)
        self.owner_id = kwargs.get("owner_id", None)

    @classmethod
    def create_server(cls, server):
        """Create Server"""
        query = """
            INSERT INTO servers (server_name, server_description, owner_id)
            VALUES (%s, %s, %s)
        """
        params = (server.server_name, server.server_description, server.owner_id)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_servers(cls, server_name=None):
        """Get Servers"""
        if server_name:
            query = """
                SELECT server_id, server_name, server_description, owner_id
                FROM servers
                WHERE server_name LIKE %s
            """
            params = (f"%{server_name}%",)
        else:
            query = """
                SELECT server_id, server_name, server_description, owner_id
                FROM servers
            """
            params = ()

        servers = DatabaseConnection.fetch_all(query, params)

        servers_list = []
        for server in servers:
            server_data = Server(
                server_id=server[0],
                server_name=server[1],
                server_description=server[2],
                owner_id=server[3],
            )
            servers_list.append(server_data)

        return servers_list

    @classmethod
    def get_server(cls, server_id):
        """Get Server"""
        query = """
            SELECT server_id, server_name, server_description, owner_id
            FROM servers
            WHERE server_id = %s
        """
        server_data = DatabaseConnection.fetch_one(query, (server_id,))
        if server_data is not None:
            server = Server(
                server_id=server_data[0],
                server_name=server_data[1],
                server_description=server_data[2],
                owner_id=server_data[3],
            )
            return server

        return None

    @classmethod
    def update_server(cls, server_id, params):
        """Update Server"""
        query = "UPDATE servers SET server_name = %s, server_description = %s WHERE server_id = %s"
        DatabaseConnection.execute_query(
            query,
            (params.get("server_name"), params.get("server_description"), server_id),
        )

    @classmethod
    def delete_server(cls, server_id):
        """Delete Server"""
        query = "DELETE FROM servers WHERE server_id = %s"
        DatabaseConnection.execute_query(query, (server_id,))

    @classmethod
    def validate_data(cls, data):
        """Validate server data"""
        server_name = data.get("server_name", None)
        server_description = data.get("server_description", None)
        owner_id = data.get("owner_id", None)

        if server_name and len(server_name) < 5:
            raise InvalidDataError("Server name must have at least 5 characters")

        if owner_id is not None and not isinstance(owner_id, int):
            raise InvalidDataError("Owner Id must be an integer")

        return Server(
            server_name=server_name,
            server_description=server_description,
            owner_id=owner_id,
        )

    @classmethod
    def exist(cls, server_id):
        """Exists"""
        query = "SELECT 1 FROM servers WHERE server_id = %s"
        result = DatabaseConnection.fetch_one(query, (server_id,))
        return result is not None

    @classmethod
    def exists_by_name(cls, server_name):
        """Check Exists Server Name"""
        query = "SELECT 1 FROM servers WHERE server_name = %s"
        result = DatabaseConnection.fetch_one(query, (server_name,))
        return result is not None
