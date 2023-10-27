import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Carga el modelo desde el archivo serializado:
with open("modelo_logistico.pkl", "rb") as modelo:
    modelo_logistico = pickle.load(modelo)

# Carga el escalador desde el archivo serializado:
with open("escalador.pkl", "rb") as escalador:
    scaler = pickle.load(escalador)


# Función para predecir el rendimiento corporal:
def clase_predict(
    edad,
    genero,
    alto_m,
    peso_kg,
    grasa_corporal,
    imc,
    diastolica,
    sistolica,
    fuerza_agarre,
    sentarse_inclinarse,
    cant_abdominales,
    salto_largo,
    scaler: StandardScaler = scaler,
    model: LogisticRegression = modelo_logistico,
):
    print(
        # Imprimir los valores ingresados por el usuario:
        f"Edad: {edad}\n"
        f"Género: {genero}\n"
        f"Altura (m): {alto_m}\n"
        f"Peso (kg): {peso_kg}\n"
        f"Grasa corporal (%): {grasa_corporal}\n"
        f"IMC: {imc}\n"
        f"Presión diastólica: {diastolica}\n"
        f"Presión sistólica: {sistolica}\n"
        f"Fuerza de agarre: {fuerza_agarre}\n"
        f"Sentarse e inclinarse (m): {sentarse_inclinarse}\n"
        f"Cantidad de abdominales: {cant_abdominales}\n"
        f"Salto largo (m): {salto_largo}\n"
    )
    # Crear un DataFrame con los valores de las variables independientes
    datos_entrada = pd.DataFrame(
        {
            "edad": [edad],
            "genero": [genero],
            "alto_m": [alto_m],
            "peso_kg": [peso_kg],
            "grasa_corporal_%": [grasa_corporal],
            "IMC": [imc],
            "diastolica": [diastolica],
            "sistolica": [sistolica],
            "fuerza_agarre": [fuerza_agarre],
            "sentarse_inclinarse_m": [sentarse_inclinarse],
            "cant_abdominales": [cant_abdominales],
            "salto_largo_m_": [salto_largo],
        }
    )

    # Columnas a escalar (todas excepto 'genero')
    columnas_a_escalar = [
        "edad",
        "alto_m",
        "peso_kg",
        "grasa_corporal_%",
        "IMC",
        "diastolica",
        "sistolica",
        "fuerza_agarre",
        "sentarse_inclinarse_m",
        "cant_abdominales",
        "salto_largo_m_",
    ]

    # Escalar las columnas seleccionadas utilizando el mismo scaler
    datos_entrada[columnas_a_escalar] = scaler.transform(
        datos_entrada[columnas_a_escalar]
    )

    # Hacer la predicción
    prediccion_clase = model.predict(datos_entrada)

    if prediccion_clase[0] == 0:
        return "A"
    elif prediccion_clase[0] == 1:
        return "B"
    elif prediccion_clase[0] == 2:
        return "C"
    else:
        return "D"


# # Prueba de la función: Ejemplo de uso (Segundo valor del dataset):
# prediccion = clase_predict(
#     edad=25,
#     genero=1,
#     alto_m=1.65,
#     peso_kg=55.8,
#     grasa_corporal=15.7,
#     imc=20.49,
#     diastolica=77,
#     sistolica=126,
#     fuerza_agarre=36.4,
#     sentarse_inclinarse=0.163,
#     cant_abdominales=53,
#     salto_largo=2.29,
#     scaler=scaler,
# )

# # Debería predecir la clase 0
# print(f"La clase predicha es: {prediccion}")

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

st.subheader("Ingrese datos de la persona:")

col1, col2, col3 = st.columns(3)
imc = 0.00
prediccion = ""
diferencia = 0.00

with col1:
    genero = st.selectbox("Género:", ("Masculino", "Femenino"))
    edad = st.slider("Edad:", 0, 110)
    alto_m = st.slider("Altura (m):", 0.00, 2.20)
    peso_kg = st.text_input("Peso (kg):")
    grasa_corporal = st.text_input("Grasa corporal (%):")
    diastolica = st.text_input("Presión diastólica:")
with col2:
    sistolica = st.text_input("Presión sistólica:")
    fuerza_agarre = st.text_input("Fuerza de agarre:")
    sentarse_inclinarse_m = st.text_input("Sentarse e inclinarse (m):")
    cant_abdominales = st.slider("Cantidad de abdominales:", 0, 70)
    salto_largo_m = st.text_input("Salto largo (m):")

    st.write("Realiza la evaluación:")
    # Botón para realizar la predicción
    if st.button("Predecir clase", use_container_width=True, type="primary"):
        imc = round(float(peso_kg) / (float(alto_m) ** 2), 2)
        diferencia = round(float(imc) - float(grasa_corporal), 2)
        # Usar la función de predicción
        prediccion = clase_predict(
            edad,
            0
            if genero == "Hombre"
            else 0,  # Convertir género a código (1 para Hombre, 0 para Mujer)
            alto_m,
            peso_kg,
            grasa_corporal,
            imc,
            diastolica,
            sistolica,
            fuerza_agarre,
            sentarse_inclinarse_m,
            cant_abdominales,
            salto_largo_m,
            scaler,
            modelo_logistico,
        )

with col3:
    st.subheader("Resultados:")
    st.metric(label=" % Grasa Corporal:", value=grasa_corporal)
    st.divider()
    st.metric(label="IMC:", value=imc, delta=diferencia, delta_color="normal")
    st.divider()
    st.metric(label="CLASE:", value=prediccion)
