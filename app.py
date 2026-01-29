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

# --- DATA CHARAKTEROV (Teraz s .png) ---
# Uisti sa, že tvoje obrázky majú tieto názvy a sú vo formáte PNG s priehľadným pozadím
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
    /* Štýl tlačidla */
    .stButton button {
        width: 100%;
        height: 80px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 12px;
        background: linear-gradient(45deg, #1e3c72, #2a5298);
        border: none;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background: linear-gradient(45deg, #2a5298, #1e3c72);
        color: #FFD700;
        transform: scale(1.02);
    }
    
    /* Nadpis postavy */
    .char-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
        text-shadow: 3px 3px 0px #000000;
        letter-spacing: 1px;
    }
    
    /* Hláška */
    .char-quote {
        text-align: center;
        font-size: 18px;
        font-style: italic;
        margin-bottom: 25px;
        color: #dddddd;
        opacity: 0.8;
    }
    
    /* Obrázok (Karta) */
    img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-height: 550px; /* Aby sa to zmestilo na obrazovku */
        object-fit: contain;
        /* Odstránil som box-shadow, aby PNG vyzeralo čisto */
        filter: drop-shadow(0px 0px 10px rgba(0,0,0,0.5)); /* Toto spraví tieň len okolo postavy, nie štvorca! */
    }
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
    # Efekt čakania
    placeholder = st.empty() # Prázdne miesto pre texty
    
    with st.spinner("Pripájam sa k Dračiemu Bohu..."):
        time.sleep(1.0)
    
    with st.spinner("Osud vyberá tvoju cestu..."):
        time.sleep(1.2)
        
    # Výber
    chosen_name = random.choice(list(CHARACTERS.keys()))
    st.session_state.chosen_char = chosen_name

# --- ZOBRAZENIE VÝSLEDKU ---
if st.session_state.chosen_char:
    char_name = st.session_state.chosen_char
    char_data = CHARACTERS[char_name]
    
    st.divider()
    
    # 1. Nadpis
    st.markdown(f'<div class="char-title" style="color: {char_data["color"]};">{char_name}</div>', unsafe_allow_html=True)
    
    # 2. Hláška
    st.markdown(f'<div class="char-quote">"{char_data["quote"]}"</div>', unsafe_allow_html=True)
    
    # 3. Obrázok
    if os.path.exists(char_data["img"]):
        st.image(char_data["img"])
    else:
        st.warning(f"⚠️ Chýba obrázok: `{char_data['img']}`. Nahraj ho do zložky (PNG format).")

    st.write("")
    st.write("")
    
    if st.button("Skúsiť osud znova? 🔄", type="secondary"):
        st.session_state.chosen_char = None
        st.rerun()

# --- PÄTIČKA ---
st.divider()
st.caption("Metin2 Destiny Chooser")
