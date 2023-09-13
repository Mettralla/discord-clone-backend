from flask import Flask
from flask_cors import CORS
from config import Config
from .routes.user_bp import user_bp
from .routes.auth_bp import auth_bp
from .routes.error_handlers import errors

def init_app():
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER)
    CORS(app, supports_credentials=True)
    app.config.from_object(Config)

    #BLUEPRINTS ------------
    app.register_blueprint(user_bp, url_prefix= '/users')

    app.register_blueprint(auth_bp, url_prefix= '/auth')
    app.register_blueprint(errors)
    
    return app