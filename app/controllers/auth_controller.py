from ..models.user_model import User
from ..models.exceptions import UsernameConflictError, InvalidDataError
from flask import request, jsonify

class AuthController:
    @classmethod
    def register(cls):
        user_data = request.json
        new_user = User.validate_data(user_data)

        if User.exist(user_data.get('username')):
            raise UsernameConflictError()

        User.create_user(new_user)
        return jsonify({'message': 'User created successfully'}), 201