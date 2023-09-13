from flask import Blueprint
from ..controllers.message_controller import MessageController

message_bp = Blueprint('message_bp', __name__)

#Ejemplo
# message_bp.route('', methods = ['GET'])(MessageController)