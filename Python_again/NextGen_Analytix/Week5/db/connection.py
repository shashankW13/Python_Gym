import mysql.connector
import streamlit as st

@st.cache_resource
def create_connection():
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root"
        )

        conn_cursor = conn.cursor()
        conn_cursor.execute("CREATE DATABASE IF NOT EXISTS library_prod")
        conn_cursor.close()
        print("Connection established")
        return conn
    
    except Exception as e:
        print("Can't connect to MySQL database", e)
        return False

@st.cache_resource
def connect_db():
    try:
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            db = "library_prod"
        )
        print("DB connected")
        return db
    
    except Exception as e:
        print("Can't connect to MySQL database", e)
        return False
    
def reconnect_db():
    db = connect_db()
    if not db.is_connected():
        db.reconnect(attempts=3, delay=2)
    return db.cursor()

    