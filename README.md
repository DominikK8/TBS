# TBS

Textbasiertes Spielprojekt mit lokalem HTML-Frontend.

## Lokales Spiel starten

### Voraussetzungen
- Python 3.10+ installiert
- `pip` verfügbar

### Einrichtung
1. Öffne ein Terminal / PowerShell im Projektordner
2. Erstelle und aktiviere eine virtuelle Umgebung

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

3. Installiere die Abhängigkeiten

```bash
pip install -r requirements.txt
```

### Spiel starten

macOS / Linux:

```bash
chmod +x run_server.sh
./run_server.sh
```

Windows:

```cmd
run_server.bat
```

Alternativ kannst du direkt ausführen:

```bash
python app.py
```

### Spiel benutzen
- Öffne im Browser: `http://127.0.0.1:5000`
- Das HTML-Design aus `templates/index.html` wird geladen
- Gib Befehle wie `umschauen`, `norden`, `westen`, `hilfe` ein

## Lokale Verfügbarkeit auf Windows und macOS

### Als reines Python-Projekt
- Auf beiden Systemen genügt Python + Flask
- Du kannst das Projekt als Ordner verteilen
- Nutzer müssen nur `requirements.txt` installieren und `app.py` starten

### Optional: In eine eigenständige App packen
Für ein echtes Doppelklick-Programm auf Windows kannst du `PyInstaller` verwenden.

1. Aktiviere die virtuelle Umgebung:

```cmd
venv\Scripts\activate
```

2. Starte den Build:

```cmd
build_exe.bat
```

Das erzeugt eine ausführbare Datei in `dist\app.exe`.

Wenn du den Befehl manuell ausführen möchtest, benutze:

```cmd
pip install pyinstaller
pyinstaller --onefile --add-data "templates;templates" app.py
```

> Hinweis: Ein Windows `.exe` lässt sich am zuverlässigsten auf einem Windows-System bauen. Auf macOS erzeugt `PyInstaller` keinen Windows-Executable.

## Hinweise
- `app.py` startet den lokalen Flask-Server
- `templates/index.html` ist die HTML-Oberfläche
- `main.py` bleibt der Konsolenmodus, `app.py` ist der Browsermodus
