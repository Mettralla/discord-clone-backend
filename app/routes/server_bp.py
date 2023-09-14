"""Server Bp"""

from flask import Blueprint
from ..controllers.server_controller import ServerController

server_bp = Blueprint("server_bp", __name__)

server_bp.route("/servers", methods=["POST"])(ServerController.create_server)
server_bp.route("/servers", methods=["GET"])(ServerController.get_servers)
server_bp.route("/servers/<int:server_id>", methods=["GET"])(
    ServerController.get_server
)
server_bp.route("/servers/<int:server_id>", methods=["PUT"])(
    ServerController.update_server
)
server_bp.route("/servers/<int:server_id>", methods=["DELETE"])(
    ServerController.delete_server
)
