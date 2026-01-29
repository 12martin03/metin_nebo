import streamlit as st
import random
import time
import os

# --- NASTAVENIE STRÁNKY ---
st.set_page_config(
    page_title="Metin2: New Server Destiny",
    page_icon="⚔️",
    layout="centered"
)

# --- DATA CHARAKTEROV (PNG) ---
CHARACTERS = {
    "Warrior - Telo (Body)": {
        "img": "war_body.png",
        "color": "#FF4B4B", 
        "quote": "Nezastaviteľná sila. Rozrazíš línie nepriateľa!"
    },
    "Warrior - Mentál (Mental)": {
        "img": "war_mental.png",
        "color": "#A52A2A", 
        "quote": "Neprekonateľná stena. Tvoje telo je z ocele."
    },
    "Šaman - Drak (Dragon)": {
        "img": "shaman_dragon.png",
        "color": "#FFD700", 
        "quote": "Oheň a buffy. Srdce každej dobrej party."
    },
    "Šaman - Heal (Liečenie)": {
        "img": "shaman_heal.png",
        "color": "#00CED1", 
        "quote": "Život a rýchlosť. Udržíš spojencov na nohách."
    },
    "Sura - WP (Weapon)": {
        "img": "sura_wp.png",
        "color": "#4B0082", 
        "quote": "Čepeľ a mágia. Najlepší PvE stroj na serveri."
    },
    "Sura - BM (Black Magic)": {
        "img": "sura_bm.png",
        "color": "#800080", 
        "quote": "Temné umenie. V PvP sa ťa budú báť."
    },
    "Ninja - Dagger (Dýka)": {
        "img": "ninja_dagger.png",
        "color": "#2E8B57", 
        "quote": "Rýchlosť a stealth. Smrtiace kombá z tieňov."
    },
    "Ninja - Arch (Luk)": {
        "img": "ninja_arch.png",
        "color": "#FFA500", 
        "quote": "Smrť z diaľky. Nikto ti neutečie."
    }
}

# --- CSS ŠTÝLY ---
st.markdown("""
<style>
    /* 1. Zarovnanie textov na stred */
    .block-container {
        text-align: center;
    }
    h1, h2, h3, p {
        text-align: center !important;
    }
    
    /* 2. Zarovnanie obrázkov na stred */
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

    /* 3. TLAČIDLO NA CELÚ ŠÍRKU */
    div.stButton {
        display: flex;
        justify-content: center; 
        align-items: center;
        width: 100%;
    }

    div.stButton > button {
        display: inline-flex;
        justify-content: center;
        align-items: center;
        width: 100% !important; /* ZMENA: 100% šírka */
        height: 80px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 12px;
        background: linear-gradient(45deg, #1e3c72, #2a5298);
        border: none;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: transform 0.2s;
    }
    
    div.stButton > button:hover {
        background: linear-gradient(45deg, #2a5298, #1e3c72);
        color: #FFD700;
        transform: scale(1.02); /* Jemnejšie zväčšenie pri plnej šírke */
    }
    
    /* 4. Typografia pre výsledok */
    .char-title {
        font-size: 42px;
        font-weight: 800;
        margin-top: 10px;
        text-shadow: 3px 3px 0px #000000;
        letter-spacing: 1px;
        text-align: center;
        /* Pridáme animáciu pre objavenie textu */
        animation: fadeIn 1s;
    }
    .char-quote {
        font-size: 18px;
        font-style: italic;
        margin-top: 10px;
        margin-bottom: 50px;
        color: #dddddd;
        opacity: 0.8;
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

st.title("⚔️ Nový Server: Volanie Osudu")
st.write("Nevieš sa rozhodnúť? Nechaj server, nech vyberie za teba.")

st.divider()
st.write("") 

if 'chosen_char' not in st.session_state:
    st.session_state.chosen_char = None

# --- TLAČIDLO "SPIN" ---
if st.button("🌀 CHOOSE YOUR PATH 🌀"):
    with st.spinner("Pripájam sa k Dračiemu Bohu..."):
        time.sleep(0.8)
    
    with st.spinner("Osud vyberá tvoju cestu..."):
        time.sleep(1.0)
        
    chosen_name = random.choice(list(CHARACTERS.keys()))
    st.session_state.chosen_char = chosen_name

# --- ZOBRAZENIE VÝSLEDKU ---
if st.session_state.chosen_char:
    char_name = st.session_state.chosen_char
    char_data = CHARACTERS[char_name]
    
    st.divider()
    
    # 1. OBRÁZOK (Zobrazí sa prvý)
    if os.path.exists(char_data["img"]):
        st.image(char_data["img"])
    else:
        st.warning(f"⚠️ Chýba obrázok: `{char_data['img']}`")
    
    # --- HERE IS THE TRICK ---
    # Krátky delay, kým sa načíta text. 
    # Tým pádom používateľ najprv vidí obrázok, mozog ho spracuje,
    # a až potom "naskočí" text pod ním.
    time.sleep(0.5) 
    
    # 2. TEXT (S oneskorením)
    st.markdown(f'<div class="char-title" style="color: {char_data["color"]};">{char_name}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="char-quote">"{char_data["quote"]}"</div>', unsafe_allow_html=True)

# --- PÄTIČKA ---
st.divider()
st.caption("Metin2 Destiny Chooser")
