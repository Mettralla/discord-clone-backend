from ..models.user_model import User
from flask import request, jsonify, session
from ..models.exceptions import NotFound, ForbiddenAction

class UserController:
    @classmethod
    def get_users(cls):
        server_id = request.args.get('server_id')
        users = User.get_users(server_id)
        response = {}

        if users:
            users_list = []
            for user in users:
                users_list.append(user.serialize())

            response["users"] = users_list
            response["total"] = len(users_list)
            return jsonify(response), 200
        else:
            return jsonify(response), 200
    
    @classmethod
    def get_user(cls, user_id):
        if session['user_id'] == user_id:
            if not User.exist(user_id):
                raise NotFound(user_id, "user")

            user = User.get_user(user_id)
            return jsonify(user.serialize()), 200
        else:
            raise ForbiddenAction()
    
    @classmethod
    def delete_user(cls, user_id):
        if not User.exist(user_id):
            raise NotFound(user_id, "user")

        if session['user_id'] == user_id:
            User.delete_user(user_id)
            return jsonify({'message': 'User deleted successfully'}), 204
        else:
            raise ForbiddenAction()
    
    @classmethod
    def update_user(cls, user_id):
        if not User.exist(user_id):
            raise NotFound(user_id, "user")
        
        if session['user_id'] == user_id:
            update_data = request.json
            og_user = User.get_user(user_id)
            
            User.update_user((
                update_data.get('username', og_user.username),
                update_data.get('image', og_user.image),
                user_id
            ))
            return jsonify({'message': 'User updated successfully'}), 200
        else:
            raise ForbiddenAction()