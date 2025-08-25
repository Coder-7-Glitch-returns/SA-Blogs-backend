# ==================================
# app/controllers/user_controller.py
# ==================================

# --- Imports ---
from flask import request, jsonify, Blueprint
import pymysql
from flask_bcrypt import Bcrypt
import secrets
import pymysql.cursors
import os


# --- Blueprint for routes ---
user_bp = Blueprint("user", __name__)

# --- Class for export
class userController:
    def __init__(self, db_connection):
        self.conn = db_connection
        print(f"userController initialized. db_connection received: {self.conn}")