import streamlit as st
from config.conexion import obtener_conexion

def login():
    st.title("Inicio de sesión")
    
    usuario = st.text_input("Usuario")
    contra = st.text_input("Contraseña", type="password")
    
    if st.button("Iniciar sesión"):
        if usuario.strip() == "" or contra.strip() == "":
            st.warning("Por favor, llene ambos campos.")
            return

        conn = obtener_conexion()
        if conn:
            try:
                cursor = conn.cursor()
                
                # Consulta directa usando los nombres de tus columnas con mayúsculas exactas
                query = "SELECT * FROM `bx4sb42e5pzf9fyyiznh`.`Empleados` WHERE `Usuario` = %s AND `Contra` = %s"
                cursor.execute(query, (usuario.strip(), contra.strip()))
                resultado = cursor.fetchone()
                
                cursor.close()
                conn.close()
                
                if resultado:
                    st.session_state["sesion_iniciada"] = True
                    st.session_state["usuario_actual"] = usuario
                    st.success(f"¡Sesión iniciada correctamente como {usuario}!")
                    st.rerun()
                else:
                    st.error("Usuario o contraseña incorrectos.")
            except Exception as e:
                st.error(f"Error inesperado en la base de datos: {e}")
        else:
            st.error("Error al conectar con la base de datos.")
