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
import random
from flask_mail import Message
# --- Class for export ---
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
            print(f'Error in Signup API: {e}')
            return jsonify({'message': 'An unexpected error occurred'}), 500
        
    # --- SIGNUP OTP SEND ---
    def signupOtp(self, mail=None):
        try:
            data = request.get_json()
            email = data.get("email")
    
            # Check whether the email field is filled
            if not email:
                return jsonify({'success': False, 'message': 'Email is required'}), 400
    
            # Check whether the user exists or not
            cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT email FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
    
            if not user:
                return jsonify({'success': False, 'message': 'User not Found'}), 400
            
            # Otp Code sending
            otp = str(random.randint(100000, 999999))
            
            msg = Message(
                subject='Your OTP Code to Verify',
                recipients=[email]
            )
            msg.body = f'Your OTP code for verifying your account is: {otp}'
            
            if mail:
                mail.send(msg)   # ✅ actually send the mail
    
            # ⚠️ Don’t return OTP in production
            return jsonify({"success": True, "message": "OTP sent successfully", "otp": otp}), 200
    
        # SQL Errors
        except pymysql.Error as err:
            print(f"Error in Signup OTP API: {err}")
            return jsonify({'message': 'Database Error'}), 500
        except Exception as e:
            print(f'Error in Signup OTP API: {e}')
            return jsonify({'message': 'An unexpected error occurred'}), 500

    # --- LOGIN ---
    def login(self):
        try:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
            
            # check whether the fields are filled
            if not all([email, password]):
                return jsonify({'success': False, 'message': 'Fields are required.'}), 400
            
            # Check whether user exists
            cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT email, password FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()   # ✅ call it, don’t assign the method
            
            if not user:
                return jsonify({'success': False, 'message': 'User Not Found.'}), 400
            
            # Check whether password matches
            bcrypt = Bcrypt()
            if not bcrypt.check_password_hash(user['password'], password):
                return jsonify({'message': 'Password do not match', 'success': False}), 401
            
            # Success
            return jsonify({'success': True, 'message': 'Welcome Back.', 'email': email}), 200
        
        # SQL Errors
        except pymysql.Error as err:
            print(f"Error in Login API: {err}")
            return jsonify({'message': 'Database Error'}), 500
        except Exception as e:
            print(f'Error in Login API: {e}')
            return jsonify({'message': 'An unexpected error occurred'}), 500