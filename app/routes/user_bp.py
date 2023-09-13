from flask import Blueprint
from ..controllers.users_controller import UserController
from ..controllers.auth_controller import AuthController

user_bp = Blueprint('user_bp', __name__)

#Ejemplo
user_bp.route('', methods = ['GET'])(UserController.get_users)
user_bp.route('/<int:user_id>', methods = ['GET'])(UserController.get_user)
user_bp.route('/<int:user_id>', methods = ['DELETE'])(UserController.delete_user)
user_bp.route('/<int:user_id>', methods = ['PATCH'])(UserController.update_user)