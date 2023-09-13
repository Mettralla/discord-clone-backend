from app import init_app
from flask import session
from itsdangerous import URLSafeSerializer

app = init_app()

if __name__ == "__main__":
    app.run()
    