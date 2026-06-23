import mysql.connector
import streamlit as st

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="bx4sb42e5pzf9fyyiznh-mysql.services.clever-cloud.com",
            user="u6ur63bxmknb68m8",
            password="QDtu4BXTVTnlmFcqkBAt",
            database="bx4sb42e5pzf9fyyiznh",
            port="3306"
        )
        return conexion
    except mysql.connector.Error as err:
        st.error(f"Error al conectar a la base de datos: {err}")
        return None
