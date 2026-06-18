@echo off
REM Build a single Windows executable for the Flask game.
SETLOCAL
cd /d "%~dp0"

if not exist "%~dp0venv\Scripts\activate.bat" (
    echo Activate your virtual environment first with:
    echo    "%~dp0venv\Scripts\activate.bat"
    pause
    exit /b 1
)

call "%~dp0venv\Scripts\activate.bat"
python -m pip install --upgrade pyinstaller
python -m PyInstaller --onefile --add-data "templates;templates" app.py

echo.
echo Build complete. The executable is in dist\app.exe
pause
