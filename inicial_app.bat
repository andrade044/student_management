@echo off
REM --- Navega para a pasta de scripts do ambiente virtual (se necessário) ---
call venv\Scripts\activate.bat

REM --- Comando para rodar o Streamlit ---
streamlit run main.py --browser.serverAddress=localhost
pause