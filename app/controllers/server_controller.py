"""Controlador de servidor"""

from ..database import DatabaseConnection


class ServerController:
    """Clase de controlador de servidor"""

    def create_server(self, server_name, server_description, owner_id):
        """Crear servidor"""
        try:
            # Crear una conexión a la base de datos
            db_connection = DatabaseConnection.get_connection()

            # Crear un cursor para ejecutar consultas
            cursor = db_connection.cursor()

            # Consulta SQL para insertar un nuevo servidor
            insert_query = "INSERT INTO servers (server_name, server_description, owner_id) VALUES (%s, %s, %s)"
            params = (server_name, server_description, owner_id)

            # Ejecutar la consulta SQL
            cursor.execute(insert_query, params)

            # Confirmar la transacción
            db_connection.commit()

            # Cerrar el cursor
            cursor.close()

        except Exception as error:
            # Manejar cualquier excepción que pueda ocurrir al crear el servidor
            db_connection.rollback()
            raise error
