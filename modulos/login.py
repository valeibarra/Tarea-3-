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
                
                # Ajustado a minúsculas tanto para la tabla como para las columnas
                query = "SELECT * FROM empleado WHERE usuario = %s AND contra = %s"
                cursor.execute(query, (usuario, contra))
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
                # Si sigue fallando, te mostrará el error técnico real de MySQL en pantalla para saber el nombre exacto
                st.error(f"Error técnico de MySQL: {e}")
        else:
            st.error("Error al conectar con la base de datos.")
