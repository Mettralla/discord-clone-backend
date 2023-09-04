from flask import Blueprint
from ..controllers.users_controller import UserController

user_bp = Blueprint('user_bp', __name__)

#Ejemplo
#user_bp.route('/users, methods = ['GET'])(UserController.get_users)