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
    """Pomocná funkcia na prečítanie obrázka do formátu base64"""
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    """Nastaví obrázok ako pozadie stránky"""
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    /* 1. Nastavenie pozadia pre celú aplikáciu (.stApp) */
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* 2. Polopriehľadný box pod obsahom, aby bol text čitateľný */
    .block-container {{
        background-color: rgba(255, 255, 255, 0.85); /* Biela s 85% nepriehľadnosťou */
        border-radius: 20px;
        padding: 3rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# --- DATA CHARAKTEROV (PNG) ---
CHARACTERS = {
    "War - aurák": {
        "img": "war_body.png",
        "color": "#FF4B4B", 
        "quote": "Nezastaviteľná sila. Rozrazíš línie nepriateľa!"
    },
    "War - mentál": {
        "img": "war_mental.png",
        "color": "#A52A2A", 
        "quote": "Neprekonateľná stena. Tvoje telo je z ocele."
    },
    "Šaman - Drak": {
        "img": "shaman_dragon.png",
        "color": "#FFD700", 
        "quote": "Oheň a buffy. Srdce každej dobrej party."
    },
    "Šaman - Heal": {
        "img": "shaman_heal.png",
        "color": "#00CED1", 
        "quote": "Život a rýchlosť. Udržíš seba a spojencov na nohách."
    },
    "Sura - WP": {
        "img": "sura_wp.png",
        "color": "#4B0082", 
        "quote": "Čepeľ a mágia. Najlepší PvM stroj na serveri."
    },
    "Sura - BM": {
        "img": "sura_bm.png",
        "color": "#800080", 
        "quote": "Temné umenie. Budú sa ťa báť."
    },
    "Ninja - Dagger": {
        "img": "ninja_dagger.png",
        "color": "#2E8B57", 
        "quote": "Rýchlosť a stealth. Smrtiace kombá z tieňov."
    },
    "Ninja - Archer": {
        "img": "ninja_arch.png",
        "color": "#FFA500", 
        "quote": "Smrť z diaľky. Nikto ti neutečie."
    }
}

# --- APLIKOVANIE POZADIA ---
# Skúsi načítať background.png, ak existuje
background_file = "background.png" 
if os.path.exists(background_file):
    set_background(background_file)
else:
    # Fallback ak zabudneš nahrať fotku (aby appka nespadla)
    st.markdown("""
    <style>
    .block-container {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CSS ŠTÝLY (Zvyšok dizajnu) ---
st.markdown("""
<style>
    /* Zarovnanie textov na stred */
    .block-container {
        text-align: center;
    }
    h1, h2, h3, p {
        text-align: center !important;
    }
    
    /* Zarovnanie obrázkov */
    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin-top: 30px;    
        margin-bottom: 20px; 
    }
    
    div[data-testid="stImage"] > img {
        max-height: 650px;
        object-fit: contain;
        filter: drop-shadow(0px 0px 15px rgba(0,0,0,0.6));
    }

    /* Tlačidlo na celú šírku */
    .stButton button {
        width: 100% !important;
        height: 80px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 12px;
        background: linear-gradient(45deg, #1e3c72, #2a5298);
        border: none;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: transform 0.2s;
        display: block !important;
    }
    
    .stButton button:hover {
        background: linear-gradient(45deg, #2a5298, #1e3c72);
        color: #FFD700;
        transform: scale(1.02);
    }
    
    /* Typografia výsledku */
    .char-title {
        font-size: 42px;
        font-weight: 800;
        margin-top: 10px;
        text-shadow: 2px 2px 0px #000000; /* Jemnejší tieň kvôli bielemu pozadiu */
        letter-spacing: 1px;
        text-align: center;
        animation: fadeIn 1s;
    }
    .char-quote {
        font-size: 18px;
        font-style: italic;
        margin-top: 10px;
        margin-bottom: 50px;
        color: #333333; /* Tmavšia farba, aby to bolo vidno na bielom boxe */
        opacity: 0.9;
        text-align: center;
        animation: fadeIn 1.5s;
    }

    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
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
st.write("") 

if 'chosen_char' not in st.session_state:
    st.session_state.chosen_char = None

# --- TLAČIDLO "SPIN" ---
if st.button("🌀 Takže čo mám hrať?! 🌀", use_container_width=True):
    with st.spinner("Pripájam sa k Dračiemu Bohu..."):
        time.sleep(0.8)
    
    with st.spinner("Osud vyberá tvoju cestu..."):
        time.sleep(1.0)
        
    chosen_name = random.choice(list(CHARACTERS.keys()))
    st.session_state.chosen_char = chosen_name

# --- ZOBRAZENIE VÝSLEDKU ---
if st.session_state.chosen_char:
    char_name = st.session_state.chosen_char
    
    # Bezpečnostná kontrola
    if char_name in CHARACTERS:
        char_data = CHARACTERS[char_name]
        
        st.divider()
        
        # 1. OBRÁZOK
        if os.path.exists(char_data["img"]):
            st.image(char_data["img"])
        else:
            st.warning(f"⚠️ Chýba obrázok: `{char_data['img']}`")
        
        time.sleep(0.5) 
        
        # 2. TEXT
        st.markdown(f'<div class="char-title" style="color: {char_data["color"]};">{char_name}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="char-quote">"{char_data["quote"]}"</div>', unsafe_allow_html=True)
    
    else:
        st.session_state.chosen_char = None
        st.rerun()

# --- PÄTIČKA ---
st.divider()
st.caption("Tvoj tatko records")
