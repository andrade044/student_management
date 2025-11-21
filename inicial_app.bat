@echo off
REM -
call venv\Scripts\activate.bat

REM
streamlit run main.py --browser.serverAddress=localhost
pause