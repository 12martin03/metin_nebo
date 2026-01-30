import streamlit as st
import random
import time
import os
import base64

# --- NASTAVENIE STRÁNKY ---
st.set_page_config(
    page_title="Nebo vol. 4",
    page_icon="⚔️",
    layout="centered"
)

# --- FUNKCIE PRE POZADIE ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* HLAVNÝ KONTAJNER - EFEKT MLIEČNEHO SKLA */
    .block-container {{
        /* Svetlý režim (predvolený) */
        background-color: rgba(255, 255, 255, 0.8) !important;
        backdrop-filter: blur(12px); /* Rozmaže fotku pod boxom */
        -webkit-backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 3rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.18);
        margin-top: 50px;
    }}

    /* Úprava pre tmavý režim */
    @media (prefers-color-scheme: dark) {{
        .block-container {{
            background-color: rgba(20, 20, 25, 0.8) !important;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# --- DATA CHARAKTEROV (PNG) ---
CHARACTERS = {
    "War - aurák": {"img": "war_body.png", "color": "#FF4B4B", "quote": "Nezastaviteľná sila. Rozrazíš línie nepriateľa!"},
    "War - mentál": {"img": "war_mental.png", "color": "#A52A2A", "quote": "Neprekonateľná stena. Tvoje telo je z ocele."},
    "Šaman - Drak": {"img": "shaman_dragon.png", "color": "#FFD700", "quote": "Oheň a buffy. Srdce každej dobrej party."},
    "Šaman - Heal": {"img": "shaman_heal.png", "color": "#00CED1", "quote": "Život a rýchlosť. Udržíš seba a spojencov na nohách."},
    "Sura - WP": {"img": "sura_wp.png", "color": "#4B0082", "quote": "Čepeľ a mágia. Najlepší PvM stroj na serveri."},
    "Sura - BM": {"img": "sura_bm.png", "color": "#800080", "quote": "Temné umenie. Budú sa ťa báť."},
    "Ninja - Dagger": {"img": "ninja_dagger.png", "color": "#2E8B57", "quote": "Rýchlosť a stealth. Smrtiace kombá z tieňov."},
    "Ninja - Archer": {"img": "ninja_arch.png", "color": "#FFA500", "quote": "Smrť z diaľky. Nikto ti neutečie."}
}

# --- APLIKOVANIE POZADIA ---
background_file = "background.png" 
if os.path.exists(background_file):
    set_background(background_file)

# --- CSS ŠTÝLY ---
st.markdown("""
<style>
    .block-container {
        text-align: center;
    }
    
    /* Dynamická farba textu podľa témy */
    h1, h2, h3, p, span, .stMarkdown {
        text-align: center !important;
        color: var(--text-color) !important;
    }
    
    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    
    div[data-testid="stImage"] > img {
        max-height: 600px;
        object-fit: contain;
        filter: drop-shadow(0px 0px 15px rgba(0,0,0,0.5));
    }

    /* Tlačidlo */
    .stButton button {
        width: 100% !important;
        height: 70px;
        font-size: 22px;
        font-weight: bold;
        border-radius: 12px;
        background: linear-gradient(45deg, #1e3c72, #2a5298);
        border: none;
        color: white !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }
    
    .char-title {
        font-size: 40px;
        font-weight: 850;
        margin-top: 15px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
        text-align: center;
    }
    
    .char-quote {
        font-size: 19px;
        font-style: italic;
        margin-top: 10px;
        margin-bottom: 40px;
        opacity: 0.9;
        text-align: center;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- HLAVNÁ APLIKÁCIA ---
st.title("Nebo vol. 4")
st.subheader("❤️ 30.1.-1.2.2026 ❤️")
st.write("Daj si za jeden na zdravie.")

st.divider()

if 'chosen_char' not in st.session_state:
    st.session_state.chosen_char = None

if st.button("🌀 Takže čo mám hrať?! 🌀", use_container_width=True):
    with st.spinner("Pripájam sa k Dračiemu Bohu..."):
        time.sleep(0.8)
    st.session_state.chosen_char = random.choice(list(CHARACTERS.keys()))

if st.session_state.chosen_char:
    char_name = st.session_state.chosen_char
    if char_name in CHARACTERS:
        char_data = CHARACTERS[char_name]
        st.divider()
        if os.path.exists(char_data["img"]):
            st.image(char_data["img"])
        
        time.sleep(0.4)
        st.markdown(f'<div class="char-title" style="color: {char_data["color"]};">{char_name}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="char-quote">"{char_data["quote"]}"</div>', unsafe_allow_html=True)

st.divider()
st.caption("Tvoj tatko records")
