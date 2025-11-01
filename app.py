import streamlit as st
from modulos.verificar_usuario import verificar_Usuario  # <--- importante

def login():
    st.title("Inicio de sesión")

    if st.session_state.get("conexion_exitosa"):
        st.success("✅ Conexión a la base de datos establecida correctamente.")

    Usuario = st.text_input("Usuario", key="Usuario_input")
    Contra = st.text_input("Contraseña", type="password", key="Contra_input")

    if st.button("Iniciar sesión"):
        tipo = verificar_Usuario(Usuario, Contra)
        if tipo:
            st.session_state["Usuario"] = Usuario
            st.session_state["sesion_iniciada"] = True
            st.success(f"👋 Bienvenido {Usuario}")
            st.rerun()
        else:
            st.error("❌ Credenciales incorrectas.")
