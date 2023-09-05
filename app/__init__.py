from flask import Flask
from config import Config
from .routes.user_bp import user_bp
from .routes.server_bp import server_bp


def init_app():
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER)

    app.config.from_object(Config)

    # BLUEPRINTS ------------
    app.register_blueprint(user_bp)
    app.register_blueprint(server_bp, url_prefix="/server")

    return app
