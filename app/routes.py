# ===============
# app/routes.py
# ===============

# --- Imports ---
from flask import request, jsonify
from .controllers.user_controllers import userController
from .models.db import get_db_connection
from .models.schemas import users_table
from flask_mail import Mail


# --- Route Function ---
def init_routes(app, mail):

    db_connection = get_db_connection()
    if db_connection:
        users_table(db_connection)

    # Pass the db connection to the userController
    user_controller = userController(db_connection)

    # --- API Routes ---

    # --- SignUp API ---
    @app.route('/api/users/signup', methods=['POST'])
    def signup_api():
        return user_controller.signUp()
    
    # --- Login API ---
    @app.route('/api/users/login', methods=['POST'])
    def login_api():
        return user_controller.login()

    # --- Signup OTP API ---
    @app.route('/api/users/signup/otp', methods=['POST'])
    def signup_otp_api():
        return user_controller.signupOtp(mail)
