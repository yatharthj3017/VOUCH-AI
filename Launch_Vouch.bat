@echo off
title VOUCH SYSTEM TERMINAL
color 0b
echo ==========================================
echo      INITIALIZING VOUCH NEURAL LINK...
echo ==========================================
echo.
echo [System] Booting local AI server...
start /b streamlit run vouch.py --server.headless true

echo [System] Establishing connection...
timeout /t 3 /nobreak > NUL

echo [System] Launching Interface...
:: 🔥 THE MASTER HACK: Disabling Chrome's Autoplay Blocker
start chrome --app="http://localhost:8501" --autoplay-policy=no-user-gesture-required

echo.
echo ==========================================
echo Vouch is running. DO NOT CLOSE THIS WINDOW.
echo ==========================================
pause > NUL