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
    def __init__(self, db_connection):
        self.conn = db_connection
        print(f"userController initialized. db_connection received: {self.conn}")
        
    
    # --- User's Table ---
    # --- SIGNUP ---
    def signUp(self):
        try:
            data = request.get_json()
            firstName = data.get('firstName')
            lastName = data.get('lastName')
            email = data.get('email')
            password = data.get('password')
            
            # Check whether the fields are filled
            if not all([firstName, lastName, email, password]):
                return jsonify({'success': False, 'message': 'Fields are required.'}), 400
            
            # Check whether user exists
            cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT email FROM users WHERE email = %s", (email,))
            existed_user = cursor.fetchone()
            
            if existed_user:
                return jsonify({'success': False, 'message': 'User already exists.'}), 400
            
            # Insert users
            bcrypt = Bcrypt()
            token = secrets.token_hex(16)
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            cursor.execute(
                "INSERT INTO users (firstName, lastName, email, password, token) VALUES (%s, %s, %s, %s, %s)",
                (firstName,lastName, email, hashed_password, token)
                )
            
            self.conn.commit()
            
            return jsonify({'success': True, 'message': 'User Created Successfully'}), 200

        # SQL Errors
        except pymysql.Error as err:
            print(f"Error in Signup API: {err}")
            return jsonify({'message': 'Database Error'}), 500
        except Exception as e:
            print('Error in Signup API')
            return jsonify({'message': 'An unexpected error occurred'}), 500
    
    # --- SIGNIN ---
    def signin(self):
        