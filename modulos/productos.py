import streamlit as st
from config.conexion import obtener_conexion

def mostrar_productos():
    st.title("📦 Gestión de Productos")
    
    # --- FORMULARIO PARA INSERTAR REGISTROS ---
    st.subheader("Registrar Nuevo Producto")
    with st.form("form_producto", clear_on_submit=True):
        nombre_prod = st.text_input("Nombre del Producto")
        precio = st.number_input("Precio ($)", min_value=0.0, step=0.01)
        btn_producto = st.form_submit_button("Guardar Producto")
        
        if btn_producto:
            if nombre_prod.strip() != "":
                conn = obtener_conexion()
                if conn:
                    cursor = conn.cursor()
                    query = "INSERT INTO Productos (Nombre_Producto, Precio) VALUES (%s, %s)"
                    cursor.execute(query, (nombre_prod, precio))
                    conn.commit()
                    cursor.close()
                    conn.close()
                    st.success(f"¡El producto '{nombre_prod}' se guardó con éxito!")
                else:
                    st.error("Error: No se pudo conectar a la base de datos.")
            else:
                st.warning("El nombre del producto es obligatorio.")

    # --- TABLA PARA VISUALIZAR REGISTROS ---
    st.subheader("Inventario de Productos Existentes")
    conn = obtener_conexion()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT Id_Producto AS 'Código', Nombre_Producto AS 'Descripción', Precio AS 'Precio ($)' FROM Productos")
        columnas = [desc[0] for desc in cursor.description]
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        
        if datos:
            st.dataframe(datos, column_config={i: col for i, col in enumerate(columnas)}, use_container_width=True)
        else:
            st.info("No hay productos registrados en el catálogo.")
