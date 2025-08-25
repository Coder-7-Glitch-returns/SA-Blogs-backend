# ===============
# app/routes.py
# ===============

# --- Imports ---
from flask import request, jsonify
from flask_mail import Mail
from .controllers.user_controllers import userController
from .models.db import get_db_connection
from .models.schemas import users_table


# --- Route Function ---
def init_routes(app):

    # --- Initialize Flask-Mail with the app ---
    mail = Mail(app)

    db_connection = get_db_connection()
    if db_connection:
        users_table(db_connection)

    # Pass the mail instance to the userController
    user_controller = userController(db_connection, mail)

    # --- API Routes ---

    # --- User Table APIs ---