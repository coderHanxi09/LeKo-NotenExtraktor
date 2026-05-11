# NotenExtraktor - Streamlit Web-Anwendung

Dies ist die Streamlit Web-Version von NotenExtraktor, die das PDF-Noten-Extraktions-Werkzeug in eine Online-Website umwandelt.

## 🚀 Lokal ausführen

### Voraussetzungen
- Python 3.8 oder höher
- pip

### Installationsschritte

1. **Zum Projektverzeichnis navigieren**
   ```bash
   cd /Users/Hannah/Documents/THA/FIM/LeKo
   ```

2. **Virtuelle Umgebung aktivieren** (falls vorhanden)
   ```bash
   source .venv/bin/activate
   ```

3. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

4. **Streamlit-Anwendung ausführen**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Im Browser öffnen**
   - Lokal: http://localhost:8501

## ☁️ In der Streamlit Cloud bereitstellen

### Methode 1: Mit GitHub + Streamlit Cloud (empfohlen)

1. **In GitHub hochladen**
   - Laden Sie das Projekt in ein GitHub-Repository hoch
   - Stellen Sie sicher, dass `streamlit_app.py` und `requirements.txt` enthalten sind

2. **Mit Streamlit Cloud verbinden**
   - Besuchen Sie https://streamlit.io/cloud
   - Melden Sie sich bei/registrieren Sie das Streamlit-Konto
   - Klicken Sie auf "New app"
   - Wählen Sie Ihr GitHub-Repository
   - Wählen Sie Branch und Dateipfad (streamlit_app.py)
   - Klicken Sie auf "Deploy"

3. **Die Anwendung wird in der streamlit.app-Domain ausgeführt**

### Methode 2: Mit Heroku (Alternative)

1. **Procfile erstellen**
   ```bash
   echo "web: streamlit run streamlit_app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile
   ```

2. **.gitignore erstellen**
   ```
   .venv/
   __pycache__/
   .DS_Store
   *.pyc
   ```

3. **Bereitstellen**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku create your-app-name
   git push heroku main
   ```

## 📁 Dateistruktur

```
LeKo/
├── streamlit_app.py          # Streamlit-Anwendungseingangspunkt
├── requirements.txt          # Python-Abhängigkeiten
├── README.md                 # Diese Dokumentation
├── .streamlit/
│   └── config.toml          # Streamlit-Konfiguration
└── GradeFilterApp.py        # Ursprüngliche Tkinter-Version
```

## 🎯 Funktionsmerkmale

✅ PDF-Datei-Upload  
✅ Automatisches Extrahieren von Studenteninformationen mit Noten 1,0 und 1,3  
✅ Echtzeit-Datenvorschau  
✅ Export als Excel- und CSV-Format  
✅ Saubere Web-Oberfläche  
✅ Responsives Design  

## 🔧 Konfiguration

In `.streamlit/config.toml` können Sie ändern:
- Designfarbe
- Hintergrundfarbe
- Schriftarteinstellung

## 📝 Anleitung

1. Laden Sie die PDF-Datei mit Studentennoten hoch
2. Das System verarbeitet automatisch und extrahiert Datensätze, die den Kriterien entsprechen
3. Zeigen Sie die extrahierte Datentabelle an
4. Als Excel- oder CSV-Datei herunterladen

## ⚠️ Fehlerbehebung

**Problem: PDF-Verarbeitung fehlgeschlagen**
- Überprüfen Sie, ob das PDF-Format korrekt ist
- Stellen Sie sicher, dass pdfplumber und verwandte Abhängigkeiten installiert sind

**Problem: Seite kann nicht geöffnet werden**
- Überprüfen Sie, ob Port 8501 belegt ist
- Versuchen Sie, einen anderen Port anzugeben: `streamlit run streamlit_app.py --server.port=8502`

**Problem: Exportfehler**
- Stellen Sie sicher, dass openpyxl installiert ist
- Überprüfen Sie die Dateiberechtigungen

## 🌐 Umgebungsvariablen (bei Bereitstellung)

Wenn andere Konfigurationen erforderlich sind, können Sie Umgebungsvariablen auf der Bereitstellungsplattform festlegen.

## 📞 Unterstützung

Auf Probleme gestoßen? Überprüfen Sie die Abhängigkeitsversionen oder lesen Sie die offizielle Dokumentation:
- Streamlit: https://docs.streamlit.io/
- pdfplumber: https://github.com/jsvine/pdfplumber

---
Version: 2.0 | Basierend auf Streamlit
