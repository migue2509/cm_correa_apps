from pathlib import Path

import streamlit as st
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Miguel Ángel Ospina | Portafolio",
    page_icon="📊",
    layout="wide",
)

st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
        background: linear-gradient(135deg, #020817 0%, #0f172a 35%, #111827 100%);
        color: #e2e8f0;
    }
    .main {
        background: transparent;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    [data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.95);
        border-right: 1px solid rgba(148, 163, 184, 0.15);
    }
    .hero-card {
        background: rgba(15, 23, 42, 0.82);
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 28px;
        padding: 2rem 2rem 1.5rem;
        box-shadow: 0 24px 60px rgba(15, 23, 42, 0.45);
        backdrop-filter: blur(10px);
        margin-bottom: 1.5rem;
    }
    .badge {
        display: inline-block;
        padding: 0.45rem 0.9rem;
        border-radius: 999px;
        background: linear-gradient(90deg, rgba(59, 130, 246, 0.15), rgba(168, 85, 247, 0.18));
        border: 1px solid rgba(147, 197, 253, 0.2);
        color: #dbeafe;
        font-size: 0.72rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .titulo {
        font-size: 3.2rem;
        font-weight: 900;
        line-height: 1.1;
        margin: 0;
        background: linear-gradient(90deg, #f8fafc 0%, #c4b5fd 40%, #7dd3fc 100%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }
    .subtitulo {
        margin-top: 0.8rem;
        font-size: 1.2rem;
        color: #cbd5e1;
        font-weight: 500;
    }
    .descripcion {
        margin-top: 1rem;
        font-size: 1.06rem;
        line-height: 1.8;
        color: #e2e8f0;
        max-width: 980px;
    }
    .hero-actions {
        margin-top: 1.2rem;
        display: flex;
        gap: 0.8rem;
        flex-wrap: wrap;
    }
    .cta-button {
        display: inline-block;
        text-decoration: none;
        padding: 0.8rem 1.25rem;
        border-radius: 12px;
        font-weight: 700;
        transition: 0.2s ease;
    }
    .cta-primary {
        background: linear-gradient(90deg, #2563eb, #7c3aed);
        color: white;
    }
    .cta-secondary {
        border: 1px solid rgba(148, 163, 184, 0.28);
        color: #e2e8f0;
        background: rgba(15, 23, 42, 0.4);
    }
    .cta-button:hover {
        transform: translateY(-1px);
        opacity: 0.95;
    }
    .section-title {
        font-size: 2rem;
        font-weight: 800;
        color: #f8fafc;
        margin: 2rem 0 1rem;
    }
    .info-card {
        background: rgba(15, 23, 42, 0.72);
        border: 1px solid rgba(148, 163, 184, 0.15);
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 18px 45px rgba(15, 23, 42, 0.25);
    }
    .info-card p {
        color: #dfe7f5;
        line-height: 1.8;
        margin: 0;
    }
    .stats-box {
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.12), rgba(124, 58, 237, 0.12));
        border: 1px solid rgba(147, 197, 253, 0.18);
        border-radius: 20px;
        padding: 1.3rem;
    }
    .stats-box ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .stats-box li {
        color: #dbeafe;
        padding: 0.6rem 0;
        border-bottom: 1px solid rgba(148, 163, 184, 0.12);
        font-size: 0.98rem;
    }
    .stats-box li:last-child {
        border-bottom: none;
    }
    .skills-wrap {
        display: flex;
        flex-wrap: wrap;
        gap: 0.75rem;
        margin-top: 0.3rem;
    }
    .skill {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(148, 163, 184, 0.15);
        color: #dbeafe;
        border-radius: 999px;
        padding: 0.65rem 1rem;
        font-size: 0.9rem;
        font-weight: 600;
    }
    .project-card {
        background: rgba(15, 23, 42, 0.78);
        border: 1px solid rgba(148, 163, 184, 0.15);
        border-radius: 20px;
        padding: 1rem;
        height: 100%;
        box-shadow: 0 20px 40px rgba(15, 23, 42, 0.2);
    }
    .project-card img {
        border-radius: 14px;
        margin-bottom: 0.9rem;
        display: block;
        width: 100%;
        object-fit: cover;
    }
    .project-category {
        color: #7dd3fc;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }
    .project-title {
        color: #f8fafc;
        font-size: 1.25rem;
        font-weight: 800;
        margin: 0 0 0.5rem;
    }
    .project-card p {
        color: #dfe7f5;
        line-height: 1.7;
        font-size: 0.92rem;
    }
    .project-link {
        display: inline-block;
        margin-top: 0.5rem;
        text-decoration: none;
        color: #93c5fd;
        font-weight: 700;
    }
    .project-link:hover {
        color: #bfdbfe;
    }
    .external-link-box {
        margin-top: 2rem;
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(148, 163, 184, 0.15);
        border-radius: 18px;
        padding: 1.1rem 1.2rem;
    }
    .external-link-box a {
        color: #bfdbfe;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-card">
        <div class="badge">Portfolio • IA • Data Science</div>
        <div class="titulo">Miguel Ángel Ospina</div>
        <div class="subtitulo">Portafolio de proyectos de inteligencia artificial, análisis de datos y aprendizaje automático</div>
        <div class="descripcion">
            Este portafolio reúne una colección de aplicaciones interactivas y proyectos orientados a la exploración de datos,
            la modelación predictiva, la visualización analítica y la resolución de problemas reales con técnicas de IA.
            Aquí puedes encontrar proyectos de preparación de datos, regresión, clasificación, series de tiempo,
            optimización y lógica algorítmica aplicados a contextos concretos.
        </div>
        <div class="hero-actions">
            <a class="cta-button cta-primary" href="#proyectos">Ver proyectos</a>
            <a class="cta-button cta-secondary" href="#sobre-mi">Sobre mí</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div id="sobre-mi" class="section-title">Sobre mí</div>', unsafe_allow_html=True)

about_col, stats_col = st.columns([2, 1])

with about_col:
    st.markdown(
        """
        <div class="info-card">
            <p>
                Soy una persona interesada en la combinación de datos, tecnología y toma de decisiones.
                A lo largo de este portafolio presento soluciones prácticas que exploran desde la limpieza y estructuración
                de datos hasta modelos predictivos y análisis estadísticos. El enfoque principal está en convertir información
                compleja en experiencias comprensibles y útiles para resolver problemas reales.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with stats_col:
    st.markdown(
        """
        <div class="stats-box">
            <ul>
                <li>📊 Análisis de datos</li>
                <li>🤖 Inteligencia artificial</li>
                <li>📈 Machine learning</li>
                <li>🧠 Visualización aplicada</li>
                <li>🔬 Optimización y modelos</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="section-title">Habilidades</div>', unsafe_allow_html=True)
skills = [
    "Python",
    "Streamlit",
    "Pandas",
    "NumPy",
    "Machine Learning",
    "Regresión",
    "Clasificación",
    "Series de tiempo",
    "Visualización",
    "Lógica algorítmica",
    "Big-O",
    "IA aplicada",
]

st.markdown(
    '<div class="skills-wrap">' + ''.join(f'<span class="skill">{skill}</span>' for skill in skills) + '</div>',
    unsafe_allow_html=True,
)

st.markdown('<div id="proyectos" class="section-title">Proyectos destacados</div>', unsafe_allow_html=True)

projects = [
    {
        "title": "¿Qué fruta es más parecida?",
        "category": "Vectores y matrices",
        "description": "Aplicación para comparar similitudes entre objetos a partir de vectores y matrices.",
        "image": "fruta-parecida.png",
        "url": "https://migue2509-mipstr-frutas-app-edw4gn.streamlit.app/",
    },
    {
        "title": "Descenso de gradiente interactivo",
        "category": "Cálculo aplicado",
        "description": "Exploración visual del comportamiento del gradiente y la optimización de funciones.",
        "image": "gradiente.png",
        "url": "https://pagradiente-g6bbqkpnzklbfme2vmz3dx.streamlit.app/",
    },
    {
        "title": "Detector de anomalías",
        "category": "Lógica + Big-O + NumPy",
        "description": "Proyecto para entender eficiencia algorítmica, lógica y procesamiento vectorizado.",
        "image": "big0.png",
        "url": "https://pamodulodetectoranomalias-8ywdwy2hafzybctqkye4u9.streamlit.app/",
    },
    {
        "title": "Preparación de datos",
        "category": "Datos",
        "description": "Proceso de limpieza, organización y estructuración de datos para análisis posterior.",
        "image": "datos.png",
        "url": "https://padetectoranomalias-nspxar85ayspvlutnl4siu.streamlit.app/",
    },
    {
        "title": "Nivel de ríos y quebradas CORNARE",
        "category": "Datos ambientales",
        "description": "Análisis aplicado a indicadores ambientales reales con enfoque en preparación y exploración de datos.",
        "image": "aplicacion.png",
        "url": "https://paappnivelcornare-4akbtl7x2h4vvcbdgpn9qj.streamlit.app/",
    },
    {
        "title": "Regresión — conceptos clave",
        "category": "Modelado predictivo",
        "description": "Aplicación para comprender la relación entre variables y la predicción basada en regresión.",
        "image": "regresion.png",
        "url": "https://paregresion-p9iafqumuzhxgkimhsvwi7.streamlit.app/",
    },
    {
        "title": "Series de tiempo sensor IoT",
        "category": "Series de tiempo",
        "description": "Análisis de datos a través del tiempo para detectar tendencias y patrones.",
        "image": "series.png",
        "url": "https://paappseriestiempo-nd5o4xwqdggrva2vgshudw.streamlit.app/",
    },
    {
        "title": "Predictor de calidad del aire",
        "category": "Modelado ambiental",
        "description": "Proyecto para estimar y pronosticar indicadores ambientales usando datos reales.",
        "image": "prediccion.png",
        "url": "https://paapppronosticocornare-8ilkzhqggycmnibcewhtkg.streamlit.app/",
    },
    {
        "title": "Sensación térmica con IoT",
        "category": "Predicción",
        "description": "Aplicación para analizar condiciones ambientales y estimar sensación térmica.",
        "image": "termica.png",
        "url": "https://paapppronosticocornare-8ilkzhqggycmnibcewhtkg.streamlit.app/",
    },
    {
        "title": "Regresión logística",
        "category": "Clasificación",
        "description": "Uso de regresión logística para estimar probabilidades y evaluar variables influyentes.",
        "image": "logistica.png",
        "url": "https://pa-app-regresion-logistica-tpzaolqbadsvdnqbxd6cug.streamlit.app/",
    },
    {
        "title": "KNN con suelos AGROSAVIA",
        "category": "Clasificación",
        "description": "Aplicación para explorar clasificación supervisada con vecinos más cercanos.",
        "image": "KN.png",
        "url": "https://m8pfkwwhemh9slj7yxb5va.streamlit.app/",
    },
]

project_cols = st.columns(4)
for i, project in enumerate(projects):
    with project_cols[i % 4]:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.image(Image.open(BASE_DIR / project["image"]), use_container_width=True)
        st.markdown(f"<div class='project-category'>{project['category']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='project-title'>{project['title']}</div>", unsafe_allow_html=True)
        st.write(project["description"])
        st.markdown(f'<a class="project-link" href="{project["url"]}" target="_blank">Abrir proyecto →</a>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="external-link-box">
        En el siguiente enlace puedes encontrar páginas y ejercicios prácticos: 
        <a href="https://sites.google.com/view/aplicacionesdeia/inicio" target="_blank">Enlace a recursos</a>
    </div>
    """,
    unsafe_allow_html=True,
)
