import streamlit as st
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent

st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("Vectores y Matrices ")
    image = Image.open(BASE_DIR / 'fruta-parecida.png')
    st.image(image, width=190)
    st.write("En el siguiente enlace usaremos una aplicación para trabajar vectores y matrices.")
    url = "https://migue2509-mipstr-frutas-app-edw4gn.streamlit.app/"
    st.write(f"¿Qué fruta es más parecida?: [Enlace]({url})")


    st.subheader("Calculo aplicado, gradiente")
    image = Image.open(BASE_DIR / 'gradiente.png')
    st.image(image, width=200)
    st.write("En este enlace veremos de forma práctica cómo funciona el gradiente y su aplicación en procesos de optimización.")
    url = "https://pagradiente-g6bbqkpnzklbfme2vmz3dx.streamlit.app/"
    st.write(f" Descenso de Gradiente Interactivo: [Enlace]({url})")

    st.subheader("Lógica, Big-O y Vectorización")
    image = Image.open(BASE_DIR / 'big0.png')
    st.image(image, width=200)
    st.write("En esta aplicación exploraremos la lógica de programación, la eficiencia de los algoritmos y el uso de Big-O y vectorización.")
    url = "https://pamodulodetectoranomalias-8ywdwy2hafzybctqkye4u9.streamlit.app/"
    st.write(f" Detector de Anomalías: Lógica + Big-O + NumPy: [Enlace]({url})")


with col2:
    st.subheader("Preparación de datos")
    image = Image.open(BASE_DIR / 'datos.png')
    st.image(image, width=200)
    st.write("En esta aplicación trabajaremos la limpieza, organización y transformación de datos para dejarlos listos para su análisis.")
    url = "https://padetectoranomalias-nspxar85ayspvlutnl4siu.streamlit.app/"
    st.write(f"Datos: preparación y estructura: [Enlace]({url})")

    st.subheader("Aplicación Preparación de datos")
    image = Image.open(BASE_DIR / 'aplicacion.png')
    st.image(image, width=200)
    st.write("En esta aplicación pondremos en práctica la preparación y análisis de datos ambientales, trabajando con información real.")
    url = "https://paappnivelcornare-4akbtl7x2h4vvcbdgpn9qj.streamlit.app/"
    st.write(f" Nivel de ríos y quebradas — CORNARE: [Enlace]({url})")

    st.subheader("Regresión Lineal")
    image = Image.open(BASE_DIR / 'regresion.png')
    st.image(image, width=200)
    st.write("En esta aplicación aprenderemos a analizar la relación entre variables y realizar predicciones mediante regresión lineal.")
    url = "https://paregresion-p9iafqumuzhxgkimhsvwi7.streamlit.app/"
    st.write(f" Regresión — Conceptos clave: [Enlace]({url})")


with col3:

    st.subheader("Series de Tiempo")
    image = Image.open(BASE_DIR / 'series.png')
    st.image(image, width=200)
    st.write("En esta aplicación analizaremos datos a través del tiempo para identificar patrones, tendencias y realizar predicciones.")
    url = "https://paappseriestiempo-nd5o4xwqdggrva2vgshudw.streamlit.app/"
    st.write(f"Series de Tiempo — Sensor IoT interactivo: [Enlace]({url})")

    st.subheader("Predicción y modelado de la calidad de aire.")
    image = Image.open(BASE_DIR / 'prediccion.png')
    st.image(image, width=200)
    st.write("En esta aplicación utilizaremos datos ambientales para estimar y pronosticar la calidad del aire.")
    url = "https://paapppronosticocornare-8ilkzhqggycmnibcewhtkg.streamlit.app/"
    st.write(f"Predictor de calidad del aire: [Enlace]({url})")
