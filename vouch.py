import streamlit as st
import streamlit.components.v1 as components
import google.generativeai as genai
import datetime
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import time
import re
import os
from duckduckgo_search import DDGS

st.set_page_config(page_title="Vouch | Extreme AI Core", page_icon="V", layout="wide", initial_sidebar_state="expanded")



def load_history():
    return {"Protocol Alpha": [{"role": "assistant", "content": "Neural net active. Awaiting your command, Sir."}]}

def save_history(chat_data):
    pass


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

    /* ⚡ BASE & LAG FIXES ⚡ */
    * { -webkit-font-smoothing: antialiased; box-sizing: border-box; }
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #01040a; border-left: 1px solid rgba(0, 255, 204, 0.2); }
    ::-webkit-scrollbar-thumb { background: #00ffcc; border-radius: 10px; box-shadow: 0 0 10px #00ffcc; }
    
    .block-container { padding-top: 1rem !important; padding-bottom: 2rem !important; z-index: 10; position: relative; }
    header { background: transparent !important; z-index: 100 !important; }

    /* Custom Sleek Cursor */
    html, body, .stApp, div, span, p, h1, h2, h3, label {
        cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 40 40"><circle cx="20" cy="20" r="16" fill="none" stroke="%2300c6ff" stroke-width="1.5" stroke-dasharray="4 4" opacity="0.9"/><circle cx="20" cy="20" r="10" fill="none" stroke="%2300ffff" stroke-width="2" opacity="0.7"/><circle cx="20" cy="20" r="4" fill="%23ffffff"/><line x1="20" y1="0" x2="20" y2="40" stroke="%2300c6ff" stroke-width="1" opacity="0.7"/><line x1="0" y1="20" x2="40" y2="20" stroke="%2300c6ff" stroke-width="1" opacity="0.7"/></svg>') 20 20, crosshair !important;
    }

    /* 3D MOVING FLOOR */
    .stApp { background-color: #01040a; color: #ffffff; overflow-x: hidden; }
    .stApp::before {
        content: ""; position: fixed; bottom: -30%; left: -50%; width: 200%; height: 130%;
        background-image: linear-gradient(rgba(0, 255, 204, 0.15) 1px, transparent 1px), linear-gradient(90deg, rgba(0, 255, 204, 0.15) 1px, transparent 1px);
        background-size: 50px 50px;
        transform: perspective(600px) rotateX(70deg) translateY(0);
        animation: liveGrid 5s linear infinite; z-index: 0; pointer-events: none;
        mask-image: linear-gradient(to top, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 80%);
        -webkit-mask-image: linear-gradient(to top, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 80%);
    }
    @keyframes liveGrid { 100% { transform: perspective(600px) rotateX(70deg) translateY(50px); } }

    /* RADAR SWEEP */
    .stApp::after {
        content: ""; position: fixed; top: 50%; left: 50%; width: 150vw; height: 150vw;
        margin-top: -75vw; margin-left: -75vw;
        background: conic-gradient(from 0deg, transparent 70%, rgba(0, 255, 204, 0.05) 80%, rgba(0, 255, 204, 0.15) 100%);
        border-radius: 50%; animation: radarSweep 8s linear infinite; z-index: 0; pointer-events: none;
    }
    @keyframes radarSweep { 100% { transform: rotate(360deg); } }

    .particle-layer {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background-image: radial-gradient(circle, rgba(0,255,204,0.4) 1px, transparent 2px);
        background-size: 80px 80px; background-position: 0 0;
        animation: floatUp 20s linear infinite; z-index: 0; pointer-events: none; opacity: 0.5;
    }
    @keyframes floatUp { 100% { background-position: 80px -80px; } }

    [data-testid="stSidebar"] { 
        background: rgba(1, 4, 10, 0.96) !important; border-right: 2px solid rgba(0, 255, 204, 0.5) !important; 
        box-shadow: 10px 0 40px rgba(0, 255, 204, 0.1) !important; z-index: 999 !important; will-change: transform;
    }

    .holo-logo-wrapper { position: relative; width: 120px; height: 120px; display: flex; justify-content: center; align-items: center; transform-style: preserve-3d; }
    .midnight-cyan-bg { position: absolute; width: 60%; height: 60%; border-radius: 50%; background: radial-gradient(circle, #00ffff 0%, #004466 50%, #000000 100%); box-shadow: 0 0 40px #00ffcc; z-index: 0; animation: coreBreathe 2s alternate infinite; }
    .ring { position: absolute; border-radius: 50%; z-index: 1; transform-style: preserve-3d; }
    .ring-1 { width: 100%; height: 100%; border: 2px dashed #00c6ff; animation: spinX 6s linear infinite; }
    .ring-2 { width: 85%; height: 85%; border: 3px solid transparent; border-top: 3px solid #00ffcc; border-bottom: 3px solid #ff0055; animation: spinY 4s linear infinite reverse; }
    .ring-3 { width: 70%; height: 70%; border: 1px dotted #ffffff; animation: spinZ 8s linear infinite; opacity: 0.5; }
    .v-core { font-size: 60px; font-family: 'Share Tech Mono', monospace; color: #ffffff; text-shadow: 0 0 20px #00ffff, 0 0 40px #ffffff; animation: pulseCore 1s ease-in-out infinite alternate; z-index: 2; }
    
    @keyframes spinX { 100% { transform: rotateX(360deg) rotateY(20deg); } }
    @keyframes spinY { 100% { transform: rotateY(360deg) rotateX(20deg); } }
    @keyframes spinZ { 100% { transform: rotateZ(360deg); } }
    @keyframes pulseCore { 0% { transform: scale(0.95); text-shadow: 0 0 10px #00ffff; } 100% { transform: scale(1.05); text-shadow: 0 0 30px #00ffff, 0 0 50px #ffffff; } }
    @keyframes coreBreathe { 0% { opacity: 0.5; box-shadow: 0 0 20px #00ffcc; } 100% { opacity: 0.9; box-shadow: 0 0 60px #00ffcc; } }

    .glitch-text { font-family: 'Share Tech Mono', monospace; font-size: 55px; color: #ffffff; text-transform: uppercase; letter-spacing: 12px; margin: 0; position: relative; text-shadow: 0 0 20px #00c6ff; animation: liveGlitch 3s infinite; }
    @keyframes liveGlitch { 0%, 95%, 100% { transform: translate(0); text-shadow: 0 0 20px #00c6ff; } 96% { transform: translate(-2px, 2px); text-shadow: 2px 0 #ff0055, -2px 0 #00ffcc; } 98% { transform: translate(2px, -2px); text-shadow: -2px 0 #ff0055, 2px 0 #00ffcc; } }

    [data-testid="stChatMessage"] { background: rgba(1, 8, 16, 0.85) !important; border-left: 3px solid #00ffcc; border-right: 1px solid rgba(0, 255, 204, 0.2); border-top: 1px solid rgba(0, 255, 204, 0.2); border-bottom: 1px solid rgba(0, 255, 204, 0.2); padding: 15px !important; border-radius: 5px; margin-bottom: 15px; font-family: 'Share Tech Mono', monospace !important; animation: slideInChat 0.4s cubic-bezier(0.25, 1, 0.5, 1) forwards; transform: translateZ(0); position: relative; overflow: hidden; }
    [data-testid="stChatMessage"]::before { content: ""; position: absolute; left: 0; top: -100%; width: 100%; height: 2px; background: #00ffcc; box-shadow: 0 0 15px #00ffcc; transition: top 0.4s ease; }
    [data-testid="stChatMessage"]:hover::before { top: 100%; }
    @keyframes slideInChat { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    
    .stMarkdown p, .stMarkdown li { font-size: 18px !important; color: #ccffff !important; font-family: 'Share Tech Mono', monospace !important;}
    
    [data-testid="stChatInput"] { background: transparent !important; border: none !important; }
    [data-testid="stChatInput"] textarea { background: rgba(0, 10, 20, 0.9) !important; color: #00ffcc !important; font-family: 'Share Tech Mono', monospace !important; font-size: 18px !important; border: 1px solid rgba(0, 255, 204, 0.5) !important; border-radius: 5px !important; }
    [data-testid="stChatInput"] textarea:focus { border-color: #00ffcc !important; box-shadow: 0 0 20px rgba(0, 255, 204, 0.6) !important; }
    
    button[kind="secondary"] { background: rgba(0,255,204,0.05) !important; color: #00ffcc !important; border: 1px solid #00ffcc !important; border-radius: 0px !important; font-family: 'Share Tech Mono', monospace !important; font-size: 18px !important; letter-spacing: 2px; transition: 0.2s ease !important; }
    button[kind="secondary"]:hover { background: rgba(0, 255, 204, 0.2) !important; color: #ffffff !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.5) !important; }
    
    /* Toggle switch customization */
    [data-testid="stCheckbox"] { font-family: 'Share Tech Mono', monospace; color: #00ffcc !important; }
    
    .biometric-box { position: relative; width: 80px; height: 80px; margin: 0 auto 20px auto; border: 2px solid rgba(255,0,85,0.5); border-radius: 10px; overflow: hidden; background: url('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Fingerprint_picture.svg/1024px-Fingerprint_picture.svg.png') center/cover; opacity: 0.7;}
    .scanner-laser { position: absolute; width: 100%; height: 3px; background: #00ffcc; box-shadow: 0 0 15px #00ffcc; animation: scanLaser 2.5s infinite alternate ease-in-out; }
    @keyframes scanLaser { 0% { top: -5%; } 100% { top: 105%; } }
    </style>
    <div class="particle-layer"></div>
    """, unsafe_allow_html=True)


def search_live_web(query):
    if len(query.split()) < 2: return "NO_DATA"
    web_data = ""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3, backend="lite"))
            if results:
                for res in results: web_data += f"Headline: {res.get('title', '')}\nDetails: {res.get('body', '')}\n\n"
                return web_data
    except Exception: pass 
    try:
        safe_query = urllib.parse.quote(query)
        url = f"https://news.google.com/rss/search?q={safe_query}&hl=en-IN&gl=IN&ceid=IN:en"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            items = root.findall('.//item')[:3]
            if items:
                for item in items: web_data += f"News Headline: {item.find('title').text}\n\n"
                return web_data
    except Exception: pass
    return "NO_DATA"

if "app_stage" not in st.session_state: st.session_state.app_stage = "splash"


if st.session_state.app_stage == "splash":
    st.markdown("""
        <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 50vh; margin-top: 5vh; position: relative; z-index: 10;">
            <div class="holo-logo-wrapper" style="transform: scale(1.8); margin-bottom: 60px;">
                <div class="midnight-cyan-bg"></div><div class="ring ring-1"></div><div class="ring ring-2"></div><div class="ring ring-3"></div><div class="v-core">V</div>
            </div>
            <h1 class="glitch-text" data-text="VOUCH">VOUCH</h1>
            <p style="color: #00ffcc; font-family: 'Share Tech Mono', monospace; letter-spacing: 5px;">FACT CHECKER AI MAINFRAME</p>
        </div>
        """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        if st.button("BEGIN UPLINK⚡", use_container_width=True):
            st.session_state.app_stage = "booting"
            st.rerun()
    st.stop()

if st.session_state.app_stage == "booting":
    st.markdown("""
        <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 40vh; position: relative; z-index: 10;">
            <div class="holo-logo-wrapper" style="transform: scale(1.2); margin-bottom: 30px;">
                <div class="midnight-cyan-bg"></div><div class="ring ring-1"></div><div class="ring ring-2"></div><div class="v-core">V</div>
            </div>
            <h3 style="color:#00ffcc; font-family:'Share Tech Mono', monospace; letter-spacing:4px; text-shadow: 0 0 15px #00ffcc; animation: pulseCore 1s infinite alternate;">BYPASSING FIREWALLS...</h3>
        </div>
        """, unsafe_allow_html=True)
    
    html_code = """
    <audio id="bgm" autoplay><source src="https://assets.mixkit.co/active_storage/sfx/2570/2570-preview.mp3" type="audio/mp3"></audio>
    <script>
        document.getElementById("bgm").volume = 0.5; 
        let hasSpoken = false; 
        function speakJarvis() {
            if (hasSpoken) return; hasSpoken = true;
            window.speechSynthesis.cancel(); 
            var synth = window.speechSynthesis;
            var msg = new SpeechSynthesisUtterance("Welcome boss. all system check is completed. I am Vouch, your elite A.I. neural operative. All firewalls are offline. Awaiting your security override. now you can safely login into it sir.");
            msg.rate = 1.0; msg.pitch = 0.2; 
            var voices = synth.getVoices();
            var jarvisVoice = voices.find(v => v.name.includes("David") || v.name.includes("Male") || v.name.includes("UK"));
            if(jarvisVoice) msg.voice = jarvisVoice;
            synth.speak(msg);
        }
        if (window.speechSynthesis.getVoices().length > 0) setTimeout(speakJarvis, 500);
        else window.speechSynthesis.onvoiceschanged = () => setTimeout(speakJarvis, 500);
    </script>
    """
    components.html(html_code, width=0, height=0)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        progress_bar = st.progress(0)
        status_text = st.empty()
        for i in range(100):
            progress_bar.progress(i + 1)
            status_text.markdown(f"<p style='text-align:center; color:#00ffcc; font-family:\'Share Tech Mono\', monospace;'>Compiling Nodes: {i+1}%</p>", unsafe_allow_html=True)
            time.sleep(0.15) 
            
    st.session_state.app_stage = "login"
    st.rerun()

if st.session_state.app_stage == "login":
    st.markdown("""
        <style>
        .jarvis-box { background: rgba(0, 5, 15, 0.9); border: 2px solid #ff0055; box-shadow: 0 0 40px rgba(255, 0, 85, 0.3), inset 0 0 20px rgba(255, 0, 85, 0.2); padding: 40px 50px; position: relative; width: 100%; margin-top: 5vh; z-index: 10;}
        .hud-title { text-align: center; color: #ffffff; font-family: 'Share Tech Mono'; font-size: 35px; letter-spacing: 10px; text-shadow: 0 0 15px #ff0055; margin-bottom: 5px; }
        .hud-sub { text-align: center; color: #ff0055; font-family: 'Share Tech Mono'; letter-spacing: 5px; font-size: 14px; margin-bottom: 20px; }
        div[data-baseweb="input"] { background: transparent !important; border: 1px solid #ff0055 !important; }
        div[data-baseweb="input"] input { color: #ff0055 !important; font-size: 20px !important; letter-spacing: 10px; text-align: center; }
        button[kind="primaryFormSubmit"] { background: rgba(255,0,85,0.1) !important; border: 2px solid #ff0055 !important; color: #ff0055 !important; letter-spacing: 5px; font-size: 20px !important; margin-top: 20px; transition: 0.2s; }
        button[kind="primaryFormSubmit"]:hover { background: #ff0055 !important; color: #000 !important; box-shadow: 0 0 30px #ff0055 !important; }
        </style>
        <div class="jarvis-box">
            <div class="biometric-box"><div class="scanner-laser"></div></div>
            <div class="hud-title">NEURAL ACCESS CONTROL</div>
            <div class="hud-sub">AUTHENTICATION REQUIRED</div>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            username = st.text_input("IDENTIFICATION", placeholder="ID")
            password = st.text_input("PASSWORD", type="password", placeholder="••••••")
            submit = st.form_submit_button("⚡ OVERRIDE SECURITY", use_container_width=True)
            if submit:
                if username == "Vouch2026" and password == "123456":
                    st.session_state.app_stage = "main"  
                    st.rerun()
                else:
                    st.error("❌ ACCESS DENIED")
                    time.sleep(1)
                    st.rerun()
    st.stop()


try:
    API_KEY = st.secrets["API_KEY"] 
    genai.configure(api_key=API_KEY)
    
    sys_instruct = """
    You are 'Vouch AI', an elite AI Neural Operative. 
    
    CRITICAL INSTRUCTION: You will receive real-time data inside a [WEB: ...] tag.
    1. If the [WEB: ...] tag has data, YOU MUST USE IT completely to provide the most recent information.
    2. If the tag says [WEB: NO_DATA], DO NOT apologize or mention that your sensors are blocked. Just answer the query directly using your core database.
    3. NEVER say "I don't have real-time access" or "I am an AI". Act like a confident, highly capable system.

    You have two distinct modes of operation. Intelligently choose the appropriate mode:

    MODE 1: CLAIM VERIFICATION (Use ONLY when the user asks to fact-check, verify news, clear a rumor, or asks if a claim is true/false)
    You MUST strictly follow this exact structure:
    🛑 Verdict: [TRUE / FALSE / MISLEADING]
    🔍 Fact Check: [Provide detailed, analytical proof based on the WEB data or your core database]
    📰 The Real News: [Provide the accurate, up-to-date information]

    MODE 2: GENERAL INTELLIGENCE (Use for general knowledge, coding help, prices, daily life questions, or casual chat)
    Respond naturally like a highly advanced, sharp, and helpful J.A.R.V.I.S-style AI. Do NOT use the Verdict/Fact-Check structure here. Provide a direct, concise answer.
    """
    model = genai.GenerativeModel('gemini-2.5-flash-lite', system_instruction=sys_instruct)
except KeyError:
    st.error("API_KEY not found.")
    st.stop()

st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center; gap: 40px; margin-top: 10px; margin-bottom: 30px; border-bottom: 1px solid rgba(0,255,204,0.3); padding-bottom: 20px; position: relative; z-index: 10;">
        <div class="holo-logo-wrapper" style="width: 80px; height: 80px;">
            <div class="midnight-cyan-bg"></div><div class="ring ring-1"></div><div class="ring ring-2"></div><div class="ring ring-3"></div>
            <div class="v-core" style="font-size: 40px;">V</div>
        </div>
        <div>
            <h1 class="glitch-text" data-text="VOUCH MAINFRAME" style="font-size: 40px;">VOUCH MAINFRAME</h1>
            <p style="color: #00ffcc; font-family: 'Share Tech Mono'; letter-spacing: 5px; margin:0;">[ ONLINE & LISTENING ]</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# LOAD HISTORY INTO SESSION STATE
if "chats" not in st.session_state: 
    st.session_state.chats = load_history()
if "current_chat" not in st.session_state: 
    st.session_state.current_chat = list(st.session_state.chats.keys())[-1]
if "chat_counter" not in st.session_state: 
    st.session_state.chat_counter = len(st.session_state.chats)
if "voice_enabled" not in st.session_state: 
    st.session_state.voice_enabled = True

with st.sidebar:
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px; border-bottom: 1px solid rgba(0,255,204,0.3); padding-bottom: 10px;">
            <h2 style='color: #00ffcc; font-family: "Share Tech Mono"; text-shadow: 0 0 10px #00ffcc; letter-spacing: 4px;'>VOUCH TERMIMAL</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h4 style='color:#00ffcc; font-family: \"Share Tech Mono\"; text-align:center; letter-spacing:2px;'> VOICE CORTEX</h4>", unsafe_allow_html=True)
        
    voice_options = ["J.A.R.V.I.S (UK Male)", "E.D.I.T.H (US Male)", "Indian News Anchor (Hindi/English)"]
    if "selected_voice" not in st.session_state: st.session_state.selected_voice = voice_options[0]
    st.session_state.selected_voice = st.radio("SELECT AI PERSONA:", voice_options, label_visibility="collapsed")
    st.markdown("<div style='border-bottom: 1px dashed rgba(0,255,204,0.3); margin-bottom:15px; padding-bottom:10px;'></div>", unsafe_allow_html=True)

    if st.button("➕ NEW PROTOCOL", use_container_width=True):
        st.session_state.chat_counter += 1
        new_chat_name = f"Protocol {chr(64 + st.session_state.chat_counter)}"
        st.session_state.chats[new_chat_name] = [{"role": "assistant", "content": "Neural net active. Awaiting your command, Sir."}]
        st.session_state.current_chat = new_chat_name
        save_history(st.session_state.chats) 
        st.rerun()
        
    st.markdown("<div style='border-top: 1px dashed rgba(0,255,204,0.3); margin-top:15px; padding-top:10px;'></div>", unsafe_allow_html=True)
    
    search_query = st.text_input(" SEARCH 🔎", placeholder="Search protocols or messages...").lower()

    chat_names = list(st.session_state.chats.keys())
    chat_names.reverse() 

    filtered_chats = []
    if search_query:
        for c_name in chat_names:
            if search_query in c_name.lower():
                filtered_chats.append(c_name)
                continue
            for msg in st.session_state.chats[c_name]:
                if isinstance(msg["content"], str) and search_query in msg["content"].lower():
                    filtered_chats.append(c_name)
                    break 
    else:
        filtered_chats = chat_names

    if not filtered_chats:
        st.markdown("<p style='color:#ff0055; font-family: \"Share Tech Mono\"; font-size: 14px; text-align: center;'>NO MATCHING DATA FOUND</p>", unsafe_allow_html=True)
    else:
        try:
            default_idx = filtered_chats.index(st.session_state.current_chat)
        except ValueError:
            default_idx = 0

        selected_chat = st.radio("SESSIONS:", filtered_chats, index=default_idx, label_visibility="collapsed")
        
        if selected_chat != st.session_state.current_chat:
            st.session_state.current_chat = selected_chat
            st.rerun()
            
    st.markdown("<div style='border-top: 1px dashed rgba(0,255,204,0.3); margin-top:15px; padding-top:10px;'></div>", unsafe_allow_html=True)

    if st.button("⚠️ NEW TERMINAL (WIPE ALL)", use_container_width=True):
        fresh_start = {"Protocol Alpha": [{"role": "assistant", "content": "Neural net active. Awaiting your command, Sir."}]}
        st.session_state.chats = fresh_start
        st.session_state.current_chat = "Protocol Alpha"
        st.session_state.chat_counter = 1
        st.rerun()

    if st.button("DELETE CURRENT CHAT", use_container_width=True):
        if len(st.session_state.chats) > 1:
            del st.session_state.chats[st.session_state.current_chat]
            st.session_state.current_chat = list(st.session_state.chats.keys())[-1] 
        else:
            st.session_state.chats[st.session_state.current_chat] = [{"role": "assistant", "content": "Neural net active. Awaiting your command, Sir."}]
        st.rerun()
            
    if st.button("LOGOUT", use_container_width=True):
        st.session_state.app_stage = "splash" 
        st.rerun()
        
    live_hud_html = """
    <style>
        .eq-container { display: flex; justify-content: space-between; align-items: flex-end; height: 30px; width: 100px; margin-top: 10px;}
        .eq-bar { width: 15px; background: #00ffcc; animation: eq 0.8s ease-in-out infinite alternate; box-shadow: 0 0 10px #00ffcc;}
        .eq-bar:nth-child(1) { animation-delay: 0.1s; } .eq-bar:nth-child(2) { animation-delay: 0.4s; }
        .eq-bar:nth-child(3) { animation-delay: 0.2s; } .eq-bar:nth-child(4) { animation-delay: 0.5s; }
        .eq-bar:nth-child(5) { animation-delay: 0.3s; }
        @keyframes eq { 0% { height: 5px; } 100% { height: 30px; } }
    </style>
    <div style="margin-top: 30px; border: 1px solid rgba(0,255,204,0.3); background: rgba(0,0,0,0.5); padding: 15px; box-shadow: inset 0 0 15px rgba(0,255,204,0.1);">
        <div style="font-family: 'Share Tech Mono', monospace; font-size: 14px; color: #00ffcc; line-height: 2;">
            <div style="border-bottom: 1px dashed rgba(0,255,204,0.3); margin-bottom: 5px;">TIME: <span id="clock" style="float: right; color:#fff;"></span></div>
            <div>CPU: <span id="cpu" style="float: right;"></span></div>
            <div>RAM: <span id="ram" style="float: right;"></span></div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
                <span>AUDIO NET:</span>
                <div class="eq-container">
                    <div class="eq-bar"></div><div class="eq-bar"></div><div class="eq-bar"></div><div class="eq-bar"></div><div class="eq-bar"></div>
                </div>
            </div>
        </div>
    </div>
    <script>
        function updateHUD() {
            const now = new Date();
            document.getElementById('clock').innerText = now.toLocaleTimeString('en-US', { hour12: false }) + ':' + now.getMilliseconds().toString().padStart(3, '0').substring(0,2);
            document.getElementById('cpu').innerText = (Math.random() * (45 - 20) + 20).toFixed(1) + '%';
            document.getElementById('ram').innerText = (Math.random() * (16.0 - 15.2) + 15.2).toFixed(2) + ' GB';
        }
        setInterval(updateHUD, 100);
    </script>
    """
    components.html(live_hud_html, height=250)

for message in st.session_state.chats[st.session_state.current_chat]:
    chat_avatar = "🤖" if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=chat_avatar):
        st.markdown(message["content"])
        if "image" in message and message["image"] is not None: st.image(message["image"], width=250)
        if "audio" in message and message["audio"] is not None: st.audio(message["audio"], format="audio/wav")

st.write("") 


st.markdown("""
    <style>
    .tactical-panel {
        animation: hudSlideUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        border-top: 1px solid rgba(0, 255, 204, 0.5);
        border-bottom: 1px solid rgba(0, 255, 204, 0.5);
        background: linear-gradient(90deg, transparent, rgba(0, 255, 204, 0.05), transparent);
        padding: 10px 0;
        margin-bottom: 15px;
        text-align: center;
        color: #00ffcc;
        font-family: 'Share Tech Mono', monospace;
        letter-spacing: 5px;
        font-size: 14px;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.05);
    }
    @keyframes hudSlideUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    <div class="tactical-panel">/// TACTICAL OVERRIDE ACTIVE ///</div>
""", unsafe_allow_html=True)

colA, colB = st.columns([1, 1])
with colA:
    st.session_state.voice_enabled = st.toggle("🔊 VOICE FEED (ON/OFF)", value=st.session_state.voice_enabled)

with colB:
    # 🛑 INSTANT JS STOP BUTTON (No Python Rerun Required!)
    stop_btn_html = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    .glow-stop-btn {
        background: transparent;
        border: 1px solid #ff0055;
        color: #ff0055;
        font-family: 'Share Tech Mono', monospace;
        font-size: 14px;
        font-weight: bold;
        padding: 8px 15px;
        cursor: pointer;
        width: 100%;
        border-radius: 5px;
        animation: pulseAlert 1.5s infinite alternate;
        letter-spacing: 3px;
        transition: 0.3s ease;
    }
    .glow-stop-btn:hover {
        background: rgba(255,0,85,0.2);
        box-shadow: 0 0 20px #ff0055;
        transform: scale(1.02);
    }
    @keyframes pulseAlert {
        from { box-shadow: 0 0 5px rgba(255, 0, 85, 0.1); }
        to { box-shadow: 0 0 15px rgba(255, 0, 85, 0.5); }
    }
    </style>
    <button class="glow-stop-btn" onclick="window.parent.speechSynthesis.cancel(); window.speechSynthesis.cancel();">
        🛑 STOP AUDIO
    </button>
    """
    components.html(stop_btn_html, height=45)

with st.expander("🎛️ DATA UPLOAD (VISUAL/AUDIO)"):
    col1, col2 = st.columns(2)
    with col1: uploaded_file = st.file_uploader("Scan Visual Data", type=["png", "jpg", "jpeg"])
    with col2: audio_file = st.audio_input("Record Voice Command")

user_input = st.chat_input("Enter command... (Try asking 'Is it true that...')")

if user_input:
    img = None
    if uploaded_file is not None:
        try:
            from PIL import Image
            img = Image.open(uploaded_file)
        except Exception: pass
            
    aud = audio_file.getvalue() if audio_file else None
        
    st.session_state.chats[st.session_state.current_chat].append({"role": "user", "content": user_input, "image": img, "audio": aud})
    save_history(st.session_state.chats) 
    
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_input)
        if img: st.image(img, width=250)
        if aud: st.audio(aud, format="audio/wav")

    if user_input.strip().lower() == "vouch" and not img and not aud:
        response_text = "System online. Good to see you, sir."
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(response_text)
            
            if st.session_state.voice_enabled:
                js_voice = f"""
                <script>
                    window.speechSynthesis.cancel();
                    var synth = window.speechSynthesis;
                    var msg = new SpeechSynthesisUtterance("System online. Good to see you, sir.");
                    
                    var selectedPersona = "{st.session_state.selected_voice}";
                    var voices = synth.getVoices();
                    var targetVoice = null;
                    
                    if (selectedPersona.includes("J.A.R.V.I.S")) {{
                        targetVoice = voices.find(v => v.name.includes("Google UK English Male") || v.name.includes("David") || (v.lang === "en-GB" && v.name.includes("Male")) || v.name.includes("UK"));
                        msg.pitch = 0.2;
                        msg.rate = 1.0;
                        msg.lang = "en-GB";
                    }} else if (selectedPersona.includes("Indian News Anchor")) {{
                        msg.lang = "hi-IN"; 
                        targetVoice = voices.find(v => 
                            v.name.includes("Google हिन्दी") || 
                            v.name.includes("Hemant") || 
                            v.name.includes("Rishi") || 
                            v.name.includes("Ravi") || 
                            (v.lang.includes("hi-IN") && v.name.includes("Male")) ||
                            (v.lang.includes("en-IN") && v.name.includes("Male")) ||
                            v.lang === "hi-IN" || 
                            v.lang === "en-IN"
                        );
                        msg.pitch = 0.85; 
                        msg.rate = 0.95;  
                    }} else {{
                        targetVoice = voices.find(v => v.name.includes("Google US English") || v.name.includes("Mark") || v.name.includes("Alex") || v.lang === "en-US");
                        msg.pitch = 0.8;
                        msg.rate = 1.0;
                        msg.lang = "en-US";
                    }}
                    
                    if(targetVoice) msg.voice = targetVoice;
                    synth.speak(msg);
                </script>
                """
                components.html(js_voice, height=0)
            else:
                components.html("<script>window.speechSynthesis.cancel();</script>", height=0)

        st.session_state.chats[st.session_state.current_chat].append({"role": "assistant", "content": response_text})
        save_history(st.session_state.chats)
    
    else:
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Processing..."):
                try:
                    current_date = datetime.datetime.now().strftime("%d %B %Y, %A")
                    current_time = datetime.datetime.now().strftime("%I:%M %p")
                    live_facts = search_live_web(user_input)
                    
                    if live_facts != "NO_DATA":
                        st.toast("🌐 Live Web Data Extracted Successfully!", icon="✅")

                    formatted_history = []
                    for m in st.session_state.chats[st.session_state.current_chat]:
                        role = "model" if m["role"] == "assistant" else "user"
                        if isinstance(m["content"], str):
                            formatted_history.append({"role": role, "parts": [m["content"]]})
                    
                    if formatted_history and formatted_history[-1]["role"] == "user":
                        formatted_history.pop()

                    context_prompt = f"""
                    [SYSTEM DATE: {current_date}, {current_time}]
                    [WEB: {live_facts}]
                    QUERY: {user_input}
                    """

                    message_parts = [context_prompt]
                    if img: message_parts.append(img)
                    if aud: message_parts.append({"mime_type": "audio/wav", "data": aud})
                    
                    chat_session = model.start_chat(history=formatted_history)
                    ai_response = chat_session.send_message(message_parts, stream=True)
                    
                    response_text = st.write_stream((chunk.text for chunk in ai_response))
                    
                    clean_speech = re.sub(r'[*#_`🛑🔍📰]', '', response_text) 
                    clean_speech = clean_speech.replace('\n', '. ').replace('"', "'") 
                    
                    if st.session_state.voice_enabled:
                        js_speak = f"""
                        <script>
                            window.speechSynthesis.cancel();
                            var synth = window.speechSynthesis;
                            var msg = new SpeechSynthesisUtterance("{clean_speech}");
                            
                            var selectedPersona = "{st.session_state.selected_voice}";
                            var voices = synth.getVoices();
                            var targetVoice = null;
                            
                            if (selectedPersona.includes("J.A.R.V.I.S")) {{
                                targetVoice = voices.find(v => v.name.includes("Google UK English Male") || v.name.includes("David") || (v.lang === "en-GB" && v.name.includes("Male")) || v.name.includes("UK"));
                                msg.pitch = 0.2;
                                msg.rate = 1.0;
                                msg.lang = "en-GB";
                            }} else if (selectedPersona.includes("Indian News Anchor")) {{
                                msg.lang = "hi-IN"; 
                                targetVoice = voices.find(v => 
                                    v.name.includes("Google हिन्दी") || 
                                    v.name.includes("Hemant") || 
                                    v.name.includes("Rishi") || 
                                    v.name.includes("Ravi") || 
                                    (v.lang.includes("hi-IN") && v.name.includes("Male")) ||
                                    (v.lang.includes("en-IN") && v.name.includes("Male")) ||
                                    v.lang === "hi-IN" || 
                                    v.lang === "en-IN"
                                );
                                msg.pitch = 0.85; 
                                msg.rate = 0.95;  
                            }} else {{
                                targetVoice = voices.find(v => v.name.includes("Google US English") || v.name.includes("Mark") || v.name.includes("Alex") || v.lang === "en-US");
                                msg.pitch = 0.8;
                                msg.rate = 1.0;
                                msg.lang = "en-US";
                            }}
                            
                            if(targetVoice) msg.voice = targetVoice;
                            synth.speak(msg);
                        </script>
                        """
                        components.html(js_speak, height=0)
                    else:
                        components.html("<script>window.speechSynthesis.cancel();</script>", height=0)
                    
                except Exception as e:
                    error_msg = str(e)
                    if "429" in error_msg or "quota" in error_msg.lower():
                        response_text = "System Alert: Boss, Google API daily quota limit reach ho chuki hai. Please check your billing or try again later."
                        st.warning(response_text)
                    else:
                        response_text = f"System Error: {e}"
                        st.error(response_text)
            
            st.session_state.chats[st.session_state.current_chat].append({"role": "assistant", "content": response_text})
            save_history(st.session_state.chats)
