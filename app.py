import streamlit as st
# Importamos las funciones de las pantallas que programaste en la carpeta 'modulos'
from modulos.login import login
from modulos.clientes import mostrar_clientes
from modulos.productos import mostrar_productos
from modulos.ventas import mostrar_ventas

# 1. Inicializar el estado de la sesión si no existe
if "sesion_iniciada" not in st.session_state:
    st.session_state["sesion_iniciada"] = False

# 2. Verificar si el usuario ya inició sesión
if st.session_state["sesion_iniciada"]:
    
    # Mostrar el usuario activo arriba en la barra lateral y botón de cerrar sesión
    st.sidebar.markdown(f"👤 Usuario: **{st.session_state.get('usuario_actual', 'Empleado')}**")
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state["sesion_iniciada"] = False
        st.session_state["usuario_actual"] = None
        st.rerun()  # Recarga la app para volver al login de inmediato
        
    st.sidebar.markdown("---")
    
    # 3. Menú lateral con las tres secciones obligatorias de tu tarea
    opciones = ["Clientes", "Productos", "Ventas"]
    seleccion = st.sidebar.selectbox("Navegación del Sistema", opciones)
    
    # 4. Enrutador dinámico: Muestra la pantalla correspondiente según el menú
    if seleccion == "Clientes":
        mostrar_clientes()
    elif seleccion == "Productos":
        mostrar_productos()
    elif seleccion == "Ventas":
        mostrar_ventas()

else:
    # Si la sesión es False, únicamente muestra el formulario de Login
    login()
