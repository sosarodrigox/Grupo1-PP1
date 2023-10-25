import streamlit as st
import pandas as pd

# Título
html_title = """
    <h2 style="color:#ebd234;text-align:center;">Body Performance Classification App V1.0 </h2>
    </div>
    """
st.markdown(html_title, unsafe_allow_html=True)

html_subtitle = """
<p style="color:#9ea0a3;text-align:center;">Esta aplicación ha sido diseñada para ayudar a clasificar el rendimiento corporal de las personas en función de los datos ingresados por el usuario.</p>
    </div>"""

st.markdown(html_subtitle, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Ingrese datos:")
    edad = st.text_input("Edad:")
    genero = st.text_input("Género:")
    alto_m = st.text_input("Altura (m):")
    peso_kg = st.text_input("Peso (kg):")
    grasa_corporal = st.text_input("Grasa corporal (%):")
    IMC = st.text_input("IMC:")
with col2:
    st.subheader(" ")
    diastolica = st.text_input("Presión diastólica:")
    sistolica = st.text_input("Presión sistólica:")
    fuerza_agarre = st.text_input("Fuerza de agarre:")
    sentarse_inclinarse_m = st.text_input("Sentarse e inclinarse (m):")
    cant_abdominales = st.text_input("Cantidad de abdominales:")
    salto_largo_m = st.text_input("Salto largo (m):")
