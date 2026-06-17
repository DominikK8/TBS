@echo off
REM Build a single Windows executable for the Flask game.
SETLOCAL

if not exist venv\Scripts\activate.bat (
    echo Activate your virtual environment first with:
    echo    venv\Scripts\activate
    pause
    exit /b 1
)

call venv\Scripts\activate.bat
python -m pip install --upgrade pyinstaller
pyinstaller --onefile --add-data "templates;templates" app.py

echo.
echo Build complete. The executable is in dist\app.exe
pause
