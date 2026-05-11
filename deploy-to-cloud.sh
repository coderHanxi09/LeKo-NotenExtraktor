#!/bin/bash

# ============================================
# NotenExtraktor - Streamlit Cloud Bereitstellung
# ============================================

echo "=================================================="
echo "🚀 NotenExtraktor zu Streamlit Cloud bereitstellen"
echo "=================================================="
echo ""

# Schritt 1: Git konfigurieren
echo "📝 Schritt 1: Git-Repository konfigurieren..."
echo ""

if [ -d .git ]; then
    echo "✅ Git-Repository existiert bereits"
else
    git init
    echo "✅ Git-Repository initialisiert"
fi

git config user.name "Hannah"
git config user.email "hannah@example.com"
echo "✅ Git-Konfiguration abgeschlossen"
echo ""

# Schritt 2: Alle Dateien hinzufügen
echo "📦 Schritt 2: Dateien zum Repository hinzufügen..."
git add .
echo "✅ Alle Dateien hinzugefügt"
echo ""

# Schritt 3: Commit erstellen
echo "💾 Schritt 3: Änderungen committen..."
git commit -m "NotenExtraktor v2.0 - Streamlit Web-Anwendung veröffentlicht" --allow-empty
echo "✅ Commit erstellt"
echo ""

# Schritt 4: Instruktionen für GitHub
echo "🌐 Schritt 4: Zu GitHub hochladen"
echo "=================================================="
echo ""
echo "Bitte folgen Sie diesen Schritten:"
echo ""
echo "1️⃣  Erstellen Sie ein neues Repository auf GitHub:"
echo "    → Gehen Sie zu https://github.com/new"
echo "    → Repository-Name: LeKo-NotenExtraktor"
echo "    → Beschreibung: PDF-Notenextraktions-Tool"
echo "    → Öffentlich (Public)"
echo "    → Klicken Sie 'Create repository'"
echo ""
echo "2️⃣  Führen Sie diese Befehle in Ihrem Terminal aus:"
echo ""
echo "    git branch -M main"
echo "    git remote add origin https://github.com/IHR_BENUTZERNAME/LeKo-NotenExtraktor.git"
echo "    git push -u origin main"
echo ""
echo "3️⃣  Ersetzen Sie 'IHR_BENUTZERNAME' mit Ihrem GitHub-Benutzernamen!"
echo ""
echo "=================================================="
echo ""
echo "📚 Nach dem Hochladen zu GitHub:"
echo ""
echo "✨ Streamlit Cloud Bereitstellung:"
echo "    1. Gehen Sie zu https://streamlit.io/cloud"
echo "    2. Klicken Sie auf 'New app'"
echo "    3. Wählen Sie Ihr GitHub-Repository"
echo "    4. Branch: main"
echo "    5. Main file path: streamlit_app.py"
echo "    6. Klicken Sie 'Deploy'"
echo ""
echo "Ihre App wird dann unter dieser URL verfügbar sein:"
echo "   https://lekonoteextraktor.streamlit.app"
echo ""
echo "=================================================="
