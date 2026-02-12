import streamlit as st

import time


# Configuración de la página
st.set_page_config(page_title="Para mi persona favorita", page_icon="❤️")

# Título con estilo
st.title("❤️ Feliz San Valentín, bella durmiente!! ❤️")

# Globos de celebración
st.balloons()



st.markdown("### 🎵 Sonido ambiente")

# Cargar y mostrar el reproductor
# "autoplay=True" intentará reproducirlo solo, pero recuerda que el navegador manda
st.audio("data/Just Give Me One More Day (Official Audio).mp3", format="audio/mp3", autoplay=True)

st.caption("Dale al play para acompañar")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #9E1B32;
    }
    
    /* Esto hace que los textos sean blancos para que se lean bien */
    h1, h2, h3, p, span, label {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --- Sección 1: Nuestra Historia ---
st.header("Algunos recuerdos... ")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("data/cafe.jpg", caption="Cuando quemaron el malvavisco", width=200) # Cambia por tus archivos
with col2:
    st.image("data/malvquemado.jpeg")
with col3:
    st.image("data/yougurt.jpg", caption="Como siempre, matandote de risa 😎")

# --- Sección 2 ---
st.subheader("¿Quién hace reír más al otro?")
if st.button('Respuesta:'):
    with st.spinner('pensando...'):
        time.sleep(3)
        st.success("Evidentemente Yax jajjajjdja")
        st.success("De hecho, según mi base de datos, te he hecho reír 21930930254 veces desde el pasado 14 ☝️🤓")


st.subheader("Más recuerdos")

col4, col5 = st.columns(2)

with col4:
    st.image("data/carro.jpg", caption="La comodidad ante todo!", width=200)
with col5:
    st.image("data/sigua.jpg", caption="Nuestra parada en Sigua 🚗")

col6, col7 = st.columns(2)

with col6:
    st.image("data/sopa.jpg", caption="Cuando casi morimos de tanta sopaa 🍲")
with col7:
    st.image("data/megapaca.jpg", caption="Megapaqueando 🐄")


# --- Sección 3: Mensaje sorpresa ---
st.write("---")
st.subheader("Autorizo que leas mi mente por un segundo")

if st.button('Clic para leer la mente de Yax'):
    with st.spinner('Cargando mucho amor...'):
        time.sleep(2)
        st.success("Mi novia hermosa es lo mejor que me ha pasado. ¡Te amo muuucho! 🌹")
        st.snow() # Un efecto visual lindo adicional


st.title("Una sorprecita...")



#video de harry
if 'mostrar_video' not in st.session_state:
    st.session_state.mostrar_video = False

# El botón cambia el estado de la variable
if st.button("Presiona para un San Valentín con estilo 😉"):
    st.session_state.mostrar_video = True
    st.balloons() # ¡Añadimos globos para que sea más divertido!

# Si la variable es verdadera, mostramos el video
if st.session_state.mostrar_video:
    # RECUERDA: Cambia 'shorts/' por 'watch?v=' en tu link
    video_url = "https://youtube.com/watch?v=UcIAvaKahIE?si=bWSyj_WnmORcLMUP" 
    
    st.markdown("### ✨ ¡¡SORPRESAA!!")
    st.video(video_url)
    st.write("Al principio estaba tímido pero lo logré convencer")

st.subheader("Algunas fotos tuyas que me gustan mucho 🙂")

st.image("data/concierto.jpg", caption="En un concierto de mafiosos, muuuuy lejos de sps")

st.image("data/basket.jpg", caption = "Nada que agregar a este estilazo...")

st.image("data/cataleya.jpeg", caption = "Definitivamente, top fotos que te he tomado, oh yeah!")

st.image("data/vang.jpg", caption = "¿¿Cómo se supone que no me iba a enamorar de esa mirada?? AAAAAHhhHHHhhH (no pude con tanta hermosura, lo siento 😵‍💫)", use_container_width=True)

#final
if st.button("clicliclicliclic"):
    st.image("data/otaku.jpg", caption="Me gustó mucho esta foto no sé por qué jajaja")
    st.write("Te amo mucho, mi amor. Espero que te haya gustado. FELIZ SAN VALENTÍN WUJUUU 💓")