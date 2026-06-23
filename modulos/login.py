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
                
                # Modificado a 'empleado' (en minúscula y singular) según tu phpMyAdmin
                # Se asume que las columnas dentro se llaman 'Usuario' y 'Contra'
                query = "SELECT * FROM empleado WHERE Usuario = %s AND Contra = %s"
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
                # Si las columnas se llaman diferente en tu tabla (ej: 'usuario' o 'contraseña'), aquí saltará el aviso
                st.error("Error en la consulta SQL: Verifica si las columnas se llaman exactamente 'Usuario' y 'Contra' dentro de tu tabla 'empleado'.")
        else:
            st.error("Error al conectar con la base de datos.")
