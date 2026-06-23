import streamlit as st
from config.conexion import obtener_conexion

def login():
    st.title("Inicio de sesión")
    
    usuario = st.text_input("Usuario")
    contra = st.text_input("Contraseña", type="password")
    
    if st.button("Iniciar sesión"):
        conn = obtener_conexion()
        if conn:
            cursor = conn.cursor()
            
            # Buscamos en la tabla Empleados si existe el usuario
            query = "SELECT Usuario, Contra FROM Empleados WHERE Usuario = %s AND Contra = %s"
            cursor.execute(query, (usuario, contra))
            resultado = cursor.fetchone()
            
            cursor.close()
            conn.close()
            
            if resultado:
                st.session_state["sesion_iniciada"] = True
                st.session_state["usuario_actual"] = usuario
                st.success(f"Sesión iniciada correctamente como {usuario}")
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos.")
        else:
            st.error("Error al conectar con la base de datos.")
