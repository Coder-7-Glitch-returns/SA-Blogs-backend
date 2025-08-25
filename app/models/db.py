# ================
# app/models/db.py
# ================

import pymysql

def get_db_connection():
    """Create a database connection."""
    try:
        connection = pymysql.connect(
            host='mysql-sa-blogs.alwaysdata.net',
            user='sa-blogs',
            password='3104944Tony',
            db='sa-blogs_db',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to the database: {e}")
        return None
