""" app/__init__.py """

from flask import Flask
from flask_cors import CORS
from config import Config
from .routes.user_bp import user_bp
from .routes.auth_bp import auth_bp
from .routes.error_handlers import errors
from .routes.server_bp import server_bp
from .routes.message_bp import message_bp
from .routes.channel_bp import channel_bp

def init_app():
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER)
    CORS(app, supports_credentials=True)
    app.config.from_object(Config)
    # BLUEPRINTS ------------
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(errors)
    app.register_blueprint(server_bp, url_prefix="/server")
    app.register_blueprint(message_bp, url_prefix= '/messages')
    app.register_blueprint(channel_bp, url_prefix="/channel")

    return app
