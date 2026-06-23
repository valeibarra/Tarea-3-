import streamlit as st
from config.conexion import obtener_conexion

def mostrar_clientes():
    st.title("👥 Gestión de Clientes")
    
    # --- FORMULARIO PARA REGISTRAR NUEVOS CLIENTES ---
    st.subheader("Añadir un Nuevo Cliente")
    with st.form("form_cliente", clear_on_submit=True):
        nombre = st.text_input("Nombre Completo del Cliente")
        direccion = st.text_input("Dirección de Residencia")
        telefono = st.text_input("Número de Teléfono")
        btn_guardar = st.form_submit_button("Guardar Cliente")
        
        if btn_guardar:
            if nombre.strip() != "":
                conn = obtener_conexion()
                if conn:
                    cursor = conn.cursor()
                    query = "INSERT INTO Clientes (Nombre, Direccion, Telefono) VALUES (%s, %s, %s)"
                    cursor.execute(query, (nombre, direccion, telefono))
                    conn.commit()
                    cursor.close()
                    conn.close()
                    st.success(f"¡El cliente '{nombre}' se registró con éxito!")
                else:
                    st.error("Error: No se pudo conectar a la base de datos.")
            else:
                st.warning("El campo 'Nombre Completo' es obligatorio.")

    # --- TABLA PARA VISUALIZAR LOS CLIENTES YA EXISTENTES ---
    st.subheader("Clientes Registrados en el Sistema")
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT Id_Cliente AS 'ID', Nombre AS 'Nombre', Direccion AS 'Dirección', Telefono AS 'Teléfono' FROM Clientes")
        columnas = [desc[0] for desc in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        
        if datos:
            st.dataframe(datos, column_config={i: col for i, col in enumerate(columnas)}, use_container_width=True)
        else:
            st.info("Aún no hay clientes registrados en la base de datos.")
