# ===============
# app/__init__.py
# ===============

# --- Imports ---
# --- Imports ---
from flask import Flask
from flask_cors import CORS
from .routes import init_routes


def create_app():
    app = Flask(__name__)
    CORS(app) # Enable CORS for all routes

    # --- Configure Flask-Mail ---
    # app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    # app.config['MAIL_PORT'] = 587
    # app.config['MAIL_USE_TLS'] = True
    # app.config['MAIL_USERNAME'] = 'ahad.dev.eng@gmail.com'
    # app.config['MAIL_PASSWORD'] = 'wnyx khfv vvsm swza'

    init_routes(app)

    return app