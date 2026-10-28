import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="nouva",
        port=3306,
        ssl_disabled=True,
        auth_plugin="caching_sha2_password",
        get_server_public_key=True
    )

