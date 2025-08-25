# ==================================
# app/controllers/user_controller.py
# ==================================

# --- Imports ---
from flask import request, jsonify
import pymysql
from flask_bcrypt import Bcrypt
import secrets
import pymysql.cursors
import os


# --- Class for export
class userController:
    # --- To function the conn and mail objects ---
    def __init__(self, db_connection, mail):
        # Initialize the database connection and the mail object
        self.conn = db_connection
        self.mail = mail
        # Make sure the directory for storing user images exists
        # This is where we will save the retrieved images
        os.makedirs("client/public/assets/user_profiles", exist_ok=True)
        print(f"userController initialized. db_connection received: {self.conn}")
