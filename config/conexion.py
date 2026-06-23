import mysql.connector
import streamlit as st

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="be5bmntqvmjb45dbc68h-mysql.services.clever-cloud.com",
            user="ufrsewvahgrdaghy",
            password="UxDnJbPxibZaLwBC6Xt1",
            database="be5bmntqvmjb45dbc68h",
            port="3306"
        )
        return conexion
    except mysql.connector.Error as err:
        st.error(f"Error al conectar a la base de datos: {err}")
        return None
