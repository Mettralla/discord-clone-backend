from decouple import config
import os

class Config:
    SERVER_NAME = "127.0.0.1:5000"
    SECRET_KEY = config("SECRET_KEY")
    DEBUG = True
    UPLOAD_FOLDER = '../discord-clone-frontend/img'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    
    STATIC_FOLDER = "app/static/"
    APP_NAME = "Discord Clone API"
    APP_VER = "1.0.0"