# 🚀 Schnellstart-Bereitstellung

## Streamlit Cloud (推荐 - 最简单)

### 1. GitHub-Repository erstellen

1. Gehen Sie zu https://github.com/new
2. Füllen Sie aus:
   - **Repository name**: `LeKo-NotenExtraktor`
   - **Description**: `PDF-Notenextraktions-Tool mit Streamlit`
   - **Public** auswählen
3. Klicken Sie **"Create repository"**

### 2. Code hochladen

```bash
cd /Users/Hannah/Documents/THA/FIM/LeKo
git branch -M main
git remote add origin https://github.com/IHR_BENUTZERNAME/LeKo-NotenExtraktor.git
git push -u origin main
```

**Ersetzen Sie `IHR_BENUTZERNAME` mit Ihrem GitHub-Benutzernamen!**

### 3. In Streamlit Cloud bereitstellen

1. Gehen Sie zu https://streamlit.io/cloud
2. Klicken Sie auf **"New app"**
3. Wählen Sie:
   - **Repository**: `IHR_BENUTZERNAME/LeKo-NotenExtraktor`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
4. Klicken Sie **"Deploy"**

### ✨ Fertig!

Ihre Anwendung wird automatisch bereitgestellt unter:
```
https://lekonoteextraktor.streamlit.app
```

---

## Lokales Testen vor der Bereitstellung

```bash
# Virtuelle Umgebung aktivieren
source .venv/bin/activate

# Abhängigkeiten installieren (falls nötig)
pip install -r requirements.txt

# App starten
streamlit run streamlit_app.py
```

Öffnen Sie dann http://localhost:8501 in Ihrem Browser.

---

## 🔗 Wichtige Links

- **Streamlit Cloud**: https://streamlit.io/cloud
- **GitHub**: https://github.com
- **Streamlit Dokumentation**: https://docs.streamlit.io

---

## 💡 Tipps

- **Kostenlos**: Streamlit Cloud ist völlig kostenlos
- **Schnell**: Automatische Bereitstellung nach dem Hochladen
- **Einfach**: Keine komplizierte Konfiguration erforderlich
- **Skalierbar**: Perfekt für kleine bis mittlere Anwendungen

---

**Version**: 2.0 | Powered by Streamlit
