from ..models.user_model import User
from flask import request, jsonify

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