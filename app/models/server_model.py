"""Server Model"""

from ..database import DatabaseConnection


class Server:
    """Class Server"""

    def __init__(self, **kwargs) -> None:
        self.server_id = kwargs.get("server_id", None)
        self.server_name = kwargs.get("server_name", None)
        self.server_description = kwargs.get("server_description", None)
        self.owner_id = kwargs.get("owner_id", None)
        self.owner_name = None

    @classmethod
    def create_server(cls, server):
        """Create Server"""
        query = "INSERT INTO servers (server_name, server_description, owner_id) VALUES (%s, %s, %s)"
        params = (server.server_name, server.server_description, server.owner_id)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_servers(cls, server_name=None):
        """Get Servers"""
        if server_name:
            query = "SELECT servers.server_id, servers.server_name, servers.server_description, servers.owner_id, users.username FROM servers JOIN users ON servers.owner_id = users.user_id WHERE servers.server_name LIKE %s"
            params = (f"%{server_name}%",)
        else:
            query = "SELECT servers.server_id, servers.server_name, servers.server_description, servers.owner_id, users.username FROM servers JOIN users ON servers.owner_id = users.user_id"
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
            server_data.owner_name = server[4]
            servers_list.append(server_data)

        return servers_list

    @classmethod
    def get_server(cls, server_id):
        """Get Server"""
        query = "SELECT servers.server_id, servers.server_name, servers.server_description, servers.owner_id, users.username FROM servers JOIN users ON servers.owner_id = users.user_id WHERE servers.server_id = %s"
        server_data = DatabaseConnection.fetch_one(query, (server_id,))
        if server_data is not None:
            server = Server(
                server_id=server_data[0],
                server_name=server_data[1],
                server_description=server_data[2],
                owner_id=server_data[3],
            )
            server.owner_name = server_data[4]
            return server
        else:
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