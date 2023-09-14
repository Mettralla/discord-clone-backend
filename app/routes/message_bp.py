from flask import Blueprint
from ..controllers.message_controller import MessageController
from ..controllers.auth_controller import AuthController

message_bp = Blueprint('message_bp', __name__)

#Ejemplo
message_bp.route('/<int:message_id>', methods = ['GET'])(AuthController.login_required(MessageController.get_message))
message_bp.route('', methods = ['GET'])(AuthController.login_required(MessageController.get_messages))