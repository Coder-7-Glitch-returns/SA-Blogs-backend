# ===============
# app/__init__.py
# ===============

# --- Imports ---
# --- Imports ---
from flask import Flask
from flask_cors import CORS
from .routes import init_routes
from flask_mail import Mail


def create_app():
    app = Flask(__name__)
    CORS(app)
    mail = Mail()
    
    # --- Configure Flask-Mail ---
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'ahad.dev.eng@gmail.com'
    app.config['MAIL_PASSWORD'] = 'nrrj eslw czht qtmv'
    app.config['MAIL_DEFAULT_SENDER'] = 'ahad.dev.eng@gmail.com'

    mail.init_app(app)
    
    init_routes(app, mail)

    return app