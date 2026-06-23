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
                resultado = None
                
                # OPCIÓN 1: Ruta completa en Clever Cloud con mayúsculas (Empleados)
                try:
                    query = "SELECT * FROM `bx4sb42e5pzf9fyyiznh`.`Empleados` WHERE Usuario = %s AND Contra = %s"
                    cursor.execute(query, (usuario, contra))
                    resultado = cursor.fetchone()
                except Exception:
                    # OPCIÓN 2: Ruta completa con columnas en minúsculas
                    try:
                        query = "SELECT * FROM `bx4sb42e5pzf9fyyiznh`.`Empleados` WHERE usuario = %s AND contra = %s"
                        cursor.execute(query, (usuario, contra))
                        resultado = cursor.fetchone()
                    except Exception:
                        pass
                
                # OPCIÓN 3: Por si acaso en el servidor quedó en singular (Empleado)
                if not resultado:
                    try:
                        query = "SELECT * FROM `bx4sb42e5pzf9fyyiznh`.`Empleado` WHERE usuario = %s AND contra = %s"
                        cursor.execute(query, (usuario, contra))
                        resultado = cursor.fetchone()
                    except Exception:
                        pass

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
