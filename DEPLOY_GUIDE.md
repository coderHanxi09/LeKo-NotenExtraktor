# NotenExtraktor in der Cloud bereitstellen

## 🚀 Plattformvergleich

| Plattform | Schwierigkeit | Kosten | Vorteile |
|------|------|------|------|
| **Streamlit Cloud** | ⭐ Sehr einfach | Kostenlos | Offizielle Plattform, sehr einfach |
| **Heroku** | ⭐⭐ Einfach | Kostenlos/kostenpflichtig | Stabil und zuverlässig |
| **Railway** | ⭐⭐ Einfach | Kostenlose Kontingente | Benutzerfreundliche Oberfläche |
| **Replit** | ⭐ Sehr einfach | Kostenlos | Kein GitHub erforderlich |

---

## ✅ Empfohlene Lösung: Streamlit Cloud (am einfachsten)

### 1️⃣ Schritt 1: In GitHub hochladen

```bash
cd /Users/Hannah/Documents/THA/FIM/LeKo
git add .
git commit -m "Initial NotenExtraktor Streamlit app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/LeKo-NotenExtraktor.git
git push -u origin main
```

### 2️⃣ Schritt 2: Auf Streamlit Cloud registrieren

1. Besuchen Sie https://streamlit.io/cloud
2. Klicken Sie auf "Sign up" und melden Sie sich mit Ihrem GitHub-Konto an
3. Autorisieren Sie Streamlit, auf Ihr GitHub zuzugreifen

### 3️⃣ Schritt 3: Anwendung bereitstellen

1. Melden Sie sich bei Streamlit Cloud an
2. Klicken Sie auf "New app"
3. Füllen Sie die Informationen aus:
   - **Repository**: `YOUR_USERNAME/LeKo-NotenExtraktor`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
4. Klicken Sie auf "Deploy"

✨ **Fertig!** Sie erhalten einen öffentlichen Link im Format:
```
https://lekonoteextraktor.streamlit.app
```

---

## 📍 Option 2: Heroku-Bereitstellung

### Voraussetzungen
- Installiert Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
- Heroku-Konto registrieren

### Bereitstellungsschritte

```bash
# 1. Bei Heroku anmelden
heroku login

# 2. Anwendung erstellen
heroku create your-app-name

# 3. Bereitstellen
git push heroku main

# 4. Anwendung anzeigen
heroku open
```

Die Anwendung wird unter `https://your-app-name.herokuapp.com` ausgeführt

---

## 🚂 Option 3: Railway-Bereitstellung

1. Besuchen Sie https://railway.app
2. Melden Sie sich mit GitHub an
3. Klicken Sie auf "New Project"→"Deploy from GitHub repo"
4. Wählen Sie Ihr `LeKo-NotenExtraktor`-Repository
5. Automatische Erkennung und Bereitstellung

---

## 🔑 Konfiguration nach der Bereitstellung

### Domain-Einstellungen (optional)

Wenn Sie eine benutzerdefinierte Domain verwenden möchten (z. B. `notes.yoursite.com`), können Sie:

1. DNS bei Ihrem Domain-Anbieter (GoDaddy, Namecheap usw.) ändern
2. Benutzerdefinierte Domain in Streamlit Cloud/Heroku hinzufügen

### Umwelt- und Leistungsoptimierung

- Streamlit Cloud wird automatisch optimiert
- Keine manuelle Konfiguration erforderlich

---

## 📊 Anwendung freigeben

Nach der Bereitstellung geben Sie einfach den Link an andere Benutzer weiter:
```
https://lekonoteextraktor.streamlit.app
```

Andere Benutzer können direkt zugreifen und die Anwendung nutzen, ohne etwas installieren zu müssen!

---

## 💡 Häufig gestellte Fragen

**F: Geht die Anwendung offline?**
- Streamlit Cloud: Nein, 24/7 online
- Heroku: Die kostenlose Version geht nach 30 Minuten Inaktivität in den Ruhezustand

**F: Gibt es Upload-Größenlimits?**
- PDF-Dateien sind normalerweise < 50 MB, kein Problem

**F: Werden Daten gespeichert?**
- Nein! Jede hochgeladene PDF wird nach der Verarbeitung sofort gelöscht

**F: Wie aktualisiere ich die Anwendung?**
- Ändern Sie den Code lokal und führen Sie `git push` durch. Die Plattform stellt automatisch neu bereit

---

## 🎯 Nächste Schritte

1. Code in GitHub hochladen
2. Bereitstellungsplattform auswählen (Streamlit Cloud empfohlen)
3. Anmelden und Ihr GitHub-Repository verbinden
4. Auf Deploy klicken!

Benötigen Sie Hilfe beim Einrichten von GitHub? Ich kann es für Sie tun.
