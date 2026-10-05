@echo off
title A customer contact manager for my business - Local Server
cd /d "%~dp0backend"
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)
call .venv\Scripts\activate.bat
if not exist ".venv\installed.flag" (
    echo Installing dependencies...
    pip install -r requirements.txt
    echo done > ".venv\installed.flag"
)
echo.
echo ============================================
echo  A customer contact manager for my business - Backend running
echo  Open: http://127.0.0.1:8000
echo  Docs: http://127.0.0.1:8000/docs
echo  Admin: http://127.0.0.1:8000/admin
echo ============================================
echo.
python main.py
pause
