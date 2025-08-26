# ===============
# app/routes.py
# ===============

# --- Imports ---
from flask import request, jsonify
from .controllers.user_controllers import userController
from .models.db import get_db_connection
from .models.schemas import users_table


# --- Route Function ---
def init_routes(app):

    db_connection = get_db_connection()
    if db_connection:
        users_table(db_connection)

    # Pass the mail instance to the userController
    user_controller = userController(db_connection)

    # --- API Routes ---

    # --- User Table APIs ---
    
    # --- SignUp API ---
    @app.route('/api/users/signup', methods=['POST'])
    def signup_api():
        return user_controller.signUp()
    
    # --- SignUp API ---
    @app.route('/api/users/login', methods=['POST'])
    def login_api():
        return user_controller.login()