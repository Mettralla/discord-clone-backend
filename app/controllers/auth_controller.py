from ..models.user_model import User
from ..models.exceptions import UsernameConflictError, InvalidDataError
from flask import request, jsonify

class AuthController:
    @classmethod
    def register(cls):
        user_data = request.json
        new_user = User.validate_data(user_data)

        if User.check_user(user_data.get('username')):
            raise UsernameConflictError()

        User.create_user(new_user)
        return jsonify({'message': 'User created successfully'}), 201
    
    # Decorador para proteger rutas restringidas
    # def login_required(func):
    #     def decorated_view(*args, **kwargs):
    #         if 'user_id' not in session:
    #             return jsonify({'error': 'No se ha iniciado sesión'}), 401
    #         return func(*args, **kwargs)
    #     return decorated_view