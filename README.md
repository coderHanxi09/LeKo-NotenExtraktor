# 📊 NotenExtraktor - Streamlit Web-Anwendung

Ein elegantes und leistungsstarkes PDF-Noten-Extraktions-Werkzeug, das automatisch spezifische Noten von Studierenden aus PDF-Abschriften extrahiert.

🌐 **Online-Zugriff**: [https://lekonoteextraktor.streamlit.app](https://lekonoteextraktor.streamlit.app)

---

## ✨ Funktionsmerkmale

✅ **PDF-Upload und -Verarbeitung** - Ein-Klick-Upload, automatische Datenextraktion  
✅ **Intelligente Filterung** - Extrahiert nur Studierende mit Noten 1,0 und 1,3  
✅ **Echtzeit-Vorschau** - Sofortiges Anzeigen der Extraktionsergebnisse  
✅ **Multi-Format-Export** - Unterstützt Excel- und CSV-Downloads  
✅ **Responsives Design** - Funktioniert auf Desktop, Tablet und Smartphone  
✅ **Datensicherheit** - Hochgeladene Dateien werden sofort gelöscht, keine Datenspeicherung  

---

## 🚀 Schnellstart

### Lokal ausführen

```bash
# 1. Repository klonen
git clone https://github.com/YOUR_USERNAME/LeKo-NotenExtraktor.git
cd LeKo-NotenExtraktor

# 2. Virtuelle Umgebung erstellen
python -m venv venv
source venv/bin/activate  # macOS/Linux
# oder
venv\Scripts\activate  # Windows

# 3. Abhängigkeiten installieren
pip install -r requirements.txt

# 4. Anwendung ausführen
streamlit run streamlit_app.py
```

Der Browser wird automatisch auf `http://localhost:8501` geöffnet

---

## 📋 Anleitung

1. **PDF hochladen** - Klicken Sie auf "PDF-Datei auswählen", um eine Datei hochzuladen
2. **Automatische Verarbeitung** - System extrahiert automatisch Noten, die den Kriterien entsprechen
3. **Ergebnisse anzeigen** - Zeigen Sie die extrahierten Daten in der Tabelle in der Vorschau an
4. **Datei herunterladen** - Wählen Sie das Excel- oder CSV-Format zum Download

### Unterstützte PDF-Formate

- Standard-Abschrift-PDF
- Dokumente mit Matrikelnummer-, Name und Noten-Informationen
- Maximale Dateigröße: 50 MB

---

## 📋 Projektstruktur

```
LeKo-NotenExtraktor/
├── streamlit_app.py          # Hauptanwendungseingangspunkt
├── requirements.txt          # Python-Abhängigkeiten
├── .streamlit/
│   └── config.toml          # Streamlit-Konfiguration
├── .gitignore               # Git-Ignorierungsdatei
├── README.md                # Diese Dokumentation
└── GradeFilterApp.py        # Ursprüngliche Tkinter-Version
```

---

## 🛠️ Technologie-Stack

- **Frontend-Framework**: Streamlit
- **PDF-Verarbeitung**: pdfplumber
- **Datenverarbeitung**: pandas
- **Excel-Export**: openpyxl
- **Python**: 3.8+

---

## 📊 Abhängigkeitsversionen

```
streamlit>=1.28.0
pdfplumber>=0.10.0
pandas>=2.2.0
openpyxl>=3.0.0
```

---

## ⚙️ Umgebungsvariablen (optional)

Für die erweiterte Bereitstellung können die folgenden Umgebungsvariablen gesetzt werden:

```
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=8501
```

---

## 🔐 Datenschutz und Sicherheit

- ✅ Hochgeladene PDF-Dateien werden **nicht gespeichert**
- ✅ Daten werden **nur temporär im Browser verarbeitet**
- ✅ Unterstützt HTTPS-verschlüsselte Übertragung
- ✅ Vollständig Open Source, selbst zu überprüfen

---

## 🐛 Fehlerbehebung

### PDF-Verarbeitung fehlgeschlagen

```
Stellen Sie sicher, dass die PDF die folgenden Informationen enthält:
- Matrikelnummer (beginnend mit einer Ziffer)
- Studentenname
- Noten-Information (1,0 oder 1,3)
```

### Seite kann nicht geöffnet werden

```bash
# Überprüfen Sie, ob Abhängigkeiten vollständig sind
pip install -r requirements.txt

# Versuchen Sie, neu zu starten
streamlit run streamlit_app.py --logger.level=debug
```

### Dateiexportfehler

```bash
# Upgrade openpyxl
pip install --upgrade openpyxl
```

---

## 📍 Leistungsoptimierung

- Unterstützt große Dateien (< 100 MB)
- Automatische Zwischenspeicherung, schnelle Reaktion
- Leichte Bereitstellung mit geringem Ressourcenverbrauch

---

## 🤝 Mitwirkung

Pull Requests und Issues werden gerne akzeptiert!

---

## 📄 Lizenz

MIT-Lizenz - Siehe LICENSE-Datei

---

## 📁 Unterstützung

- Streamlit-Dokumentation: https://docs.streamlit.io/
- pdfplumber GitHub: https://github.com/jsvine/pdfplumber
- Fehlerbericht: Senden Sie einen GitHub Issue

---

## 🎯 Versionsverlauf

- **v2.0** (2025-05-11) - Veröffentlichung der Streamlit-Web-Anwendung
- **v1.1** (2024-XX-XX) - Tkinter-Desktop-Version

---

**Gemacht mit ❤️ von Hannah | Mit Streamlit betrieben**
