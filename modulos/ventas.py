import streamlit as st
from config.conexion import obtener_conexion

def mostrar_ventas():
    st.title("🛒 Control de Ventas")
    
    # --- FORMULARIO PARA REGISTRAR NUEVA VENTA ---
    st.subheader("Registrar Nueva Transacción")
    with st.form("form_venta", clear_on_submit=True):
        producto = st.text_input("Producto Vendido")
        cantidad = st.text_input("Cantidad")
        btn_venta = st.form_submit_button("Procesar Venta")
        
        if btn_venta:
            if producto and cantidad:
                conn = obtener_conexion()
                if conn:
                    cursor = conn.cursor()
                    # Inserta en la tabla 'Ventas' con la estructura de la Guía 6
                    query = "INSERT INTO Ventas (Producto, Cantidad) VALUES (%s, %s)"
                    cursor.execute(query, (producto, cantidad))
                    conn.commit()
                    cursor.close()
                    conn.close()
                    st.success("La venta ha sido procesada y registrada en Clever Cloud.")
                else:
                    st.error("Error: Fallo de conexión de datos.")
            else:
                st.warning("Por favor rellene todos los campos del formulario.")

    # --- TABLA DE VISUALIZACIÓN ---
    st.subheader("Historial de Ventas")
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT Id_Venta AS 'N° Transacción', Producto AS 'Artículo', Cantidad AS 'Unidades' FROM Ventas")
        columnas = [desc[0] for desc in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        
        if datos:
            st.dataframe(datos, column_config={i: col for i, col in enumerate(columnas)}, use_container_width=True)
        else:
            st.info("Aún no existen ventas registradas en el sistema.")
