@echo off
REM Google Dork Generator - Batch Runner
REM This script runs the Streamlit app using the virtual environment

echo Starting Google Dork Generator...
echo.

REM Change to the script directory
cd /d "%~dp0"

REM Check if virtual environment exists
if not exist ".env\Scripts\python.exe" (
    echo ERROR: Virtual environment not found!
    echo Please make sure the .env folder exists in this directory.
    echo.
    pause
    exit /b 1
)

REM Check if main.py exists
if not exist "main.py" (
    echo ERROR: main.py not found!
    echo Please make sure main.py is in this directory.
    echo.
    pause
    exit /b 1
)

REM Run the Streamlit app
echo Running Streamlit app...
echo The app will open in your default web browser.
echo Press Ctrl+C in this window to stop the server.
echo.

".env\Scripts\python.exe" streamlit run main.py

echo.
echo Google Dork Generator has stopped.
pause