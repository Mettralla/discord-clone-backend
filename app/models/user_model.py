from ..database import DatabaseConnection
from ..models.exceptions import InvalidDataError
from werkzeug.security import check_password_hash, generate_password_hash

class User:
    def __init__(self, **kwargs) -> None:
        self.user_id = kwargs.get('user_id', None)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)
        self.email = kwargs.get('email', None)
        self.image = kwargs.get('image', None)
        self.creation_date = kwargs.get('creation_date', None)

    @classmethod
    def create_user(cls, user):
        query = "INSERT INTO users (username, password_digest) VALUES (%s, %s)"
        params = (
            user.username, 
            generate_password_hash(user.password)
        )
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_users(cls, server_id: int) -> list['User']:
        query = """
            SELECT users.user_id, users.username, users.image 
            FROM users JOIN user_servers
            ON users.user_id = user_servers.user_id
            WHERE user_servers.server_id = %s"""
        users = DatabaseConnection.fetch_all(query, (server_id,))
        
        users_list = []
        for user in users:
            user_data = User(
                user_id = user[0],
                username = user[1],
                image = user[2]
            )
            users_list.append(user_data)

        return users_list
    
    @classmethod
    def get_user(cls, user_id: int):
        query = "SELECT user_id, username, image FROM users WHERE user_id = %s"
        user_data = DatabaseConnection.fetch_one(query, (user_id,))
        if user_data is not None:
            return User(
                user_id = user_data[0],
                username = user_data[1],
                image = user_data[2]
            )
        else:
            return None
    
    @classmethod
    def delete_user(cls, user_id: int):
        query = "DELETE FROM users WHERE user_id = %s"
        DatabaseConnection.execute_query(query, (user_id,))
    
    @classmethod
    def update_user(cls, params: tuple):
        query = "UPDATE users SET username = %s, image = %s WHERE user_id = %s"
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def validate_data(cls, data) -> 'User':
        """Validate user data"""
        new_username = data.get('username')
        if len(new_username) < 3:
            raise InvalidDataError("Username must have at least three characters")

        new_password = data.get('password')
        if len(new_password) < 8:
            raise InvalidDataError("Password must have at least eight characters")
        
        return User(username = new_username, password = new_password)

    @classmethod
    def check_user(cls, username: str) -> bool:
        """Check if username is taken"""
        query = "SELECT 1 FROM users WHERE username = %s"
        result = DatabaseConnection.fetch_one(query, (username,))
        return result is not None
    
    @classmethod
    def exist(cls, user_id: int) -> bool:
        """Check if user_exist"""
        query = "SELECT 1 FROM users WHERE user_id = %s"
        result = DatabaseConnection.fetch_one(query, (user_id,))
        return result is not None
    
    def serialize(self) -> dict:
        return {
            'user_id': self.user_id,
            'username': self.username,
            'image': self.image
        }