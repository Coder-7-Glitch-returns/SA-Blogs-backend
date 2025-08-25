# =====================
# app/models/schemas.py
# =====================

# --- Imports ---
import pymysql
import pymysql.cursors

# --- Users Table (used to add, remove, update and block users) ---
def users_table(conn):
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                fullName VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                token VARCHAR(255) NOT NULL,
                role VARCHAR(255) DEFAULT 'user',
                gender VARCHAR(255) NOT NULL,
                category VARCHAR(255) DEFAULT NULL,
                isActive BOOLEAN DEFAULT FALSE,
                isBlocked BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
        )
        conn.commit()
        print("Users Table created successfully or already exists.")
    except pymysql.Error as err:
        print(f"Error in creating User Table: {err}")
        conn.rollback()
        raise