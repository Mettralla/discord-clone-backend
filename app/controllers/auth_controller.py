from ..models.user_model import User
from ..models.exceptions import NameConflictError, UnauthorizedAccess, InvalidDataError
from functools import wraps
from flask import request, jsonify, session


class AuthController:
    @classmethod
    def register(cls):
        user_data = request.json
        new_user = User.validate_data(user_data)

        if User.check_user(user_data.get('username')):
            raise NameConflictError('user', 'username', user_data.get('username'))

        User.create_user(new_user)
        return jsonify({'message': 'User created successfully'}), 201
    
    @classmethod
    def login(cls):
        data = request.json
        if not User.check_user(data.get('username')):
            raise InvalidDataError(description="Username or Password Incorrect")
        
        user = User(username = data.get('username'), password = data.get('password'))

        if user.is_registered():
            session['user_id'] = user.user_id
            return jsonify({'message': 'Inicio de sesión exitoso'}), 200
        else:
            raise InvalidDataError(description="Username or Password Incorrect")

    @classmethod
    def logout(cls):
        session.pop('user_id', None)
        return jsonify({'message': 'Cierre de sesión exitoso'}), 200

    @classmethod
    def login_required(cls, func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if 'user_id' not in session:
                raise UnauthorizedAccess()
            return func(*args, **kwargs)
        return decorated_view
    
    