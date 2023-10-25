import streamlit as st
import pandas as pd

# Título
html_title = """
    <h2 style="color:#ebd234;text-align:center;">Body Performance Classification App V1.0 </h2>
    </div>
    """
st.markdown(html_title, unsafe_allow_html=True)

html_subtitle = """
<p style="color:#9ea0a3;text-align:center;">This app is used to help to classify body performance based on the data inputted by the user</p>
    </div>"""

st.markdown(html_subtitle, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.header("Ingrese los datos")

    # Lecctura de datos
    # Datos = st.text_input("Ingrese los valores : N P K Temp Hum pH lluvia:")
    N = st.text_input("Nitrógeno:")
    P = st.text_input("Fósforo:")
    K = st.text_input("Potasio:")
    Temp = st.text_input("Temperatura:")
    Hum = st.text_input("Humedad:")
    pH = st.text_input("pH:")
    rain = st.text_input("Lluvia:")
