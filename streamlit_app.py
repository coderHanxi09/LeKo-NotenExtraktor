import streamlit as st
import pdfplumber
import pandas as pd
import io
from datetime import datetime

st.set_page_config(page_title="NotenExtraktor", layout="centered", initial_sidebar_state="expanded")

# --- Stileinstellungen ---
st.markdown("""
    <style>
    .main { max-width: 800px; margin: 0 auto; }
    .success { color: #00aa00; font-weight: bold; }
    .error { color: #ff0000; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- Kopfzeile ---
st.title("📊 NotenExtraktor")
st.markdown("**Werkzeug zum Extrahieren spezifischer Noten aus PDF** (Noten: 1,0 & 1,3)")

# --- Seitenleisten-Informationen ---
with st.sidebar:
    st.markdown("### 📖 Über dieses Werkzeug")
    st.info("""
    Dieses Werkzeug dient zum automatischen Extrahieren aus PDF-Abschriften:
    - Matrikelnummer
    - Studentenname
    - Note
    
    Extrahiert nur Studenteninformationen mit Noten **1,0** und **1,3**.
    """)
    """)
    
    st.markdown("### ⚙️ Anleitung")
    st.markdown("""
    1. PDF-Datei hochladen
    2. System verarbeitet automatisch
    3. Ergebnis als Excel-Datei herunterladen
    """)

# --- Kernlogik ---
def process_pdf(pdf_file, target_grades=["1,0", "1,3"]):
    """Extrahiert Noten aus PDF, die den Bedingungen entsprechen"""
    extracted_data = []
    stop_signal = "Diesen Ausdruck bitte unterschreiben"
    
    try:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if not text:
                    continue
                
                lines = text.split('\n')
                for line in lines:
                    if stop_signal in line:
                        return extracted_data
                    
                    if any(grade in line for grade in target_grades):
                        parts = line.split()
                        
                        if parts and parts[0].isdigit():
                            matrikel = parts[0]
                            grade = next((p for p in parts if p in target_grades), None)
                            
                            name_parts = []
                            for p in parts[1:]:
                                if p == grade:
                                    break
                                if "/" not in p and not p.isdigit():
                                    name_parts.append(p)
                            
                            full_name = " ".join(name_parts)
                            extracted_data.append({
                                "Matrikel Nr.": matrikel,
                                "Name": full_name,
                                "Note": grade
                            })
        return extracted_data
    except Exception as e:
        raise e

# --- Hauptprogramm ---
st.markdown("---")

# Dateiupload
uploaded_file = st.file_uploader(
    "📁 PDF-Datei auswählen", 
    type="pdf",
    help="Laden Sie eine PDF-Datei mit Studentennoten hoch"
)

if uploaded_file is not None:
    st.markdown("---")
    
    with st.spinner("⏳ Wird verarbeitet..."):
        try:
            # Verarbeite PDF
            data = process_pdf(uploaded_file)
            
            if data:
                # DataFrame erstellen
                df = pd.DataFrame(data)
                
                # Ergebnis anzeigen
                st.success(f"✅ Erfolgreich {len(df)} Datensätze extrahiert!")
                
                # Tabelle anzeigen
                st.markdown("### 📋 Extrahierte Daten")
                st.dataframe(df, use_container_width=True)
                
                # Statistikinformationen
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Gesamtzahl der Datensätze", len(df))
                with col2:
                    st.metric("Schüler mit Note 1,0", len(df[df['Note'] == '1,0']))
                
                # Download-Schaltflächen
                st.markdown("### 💾 Daten exportieren")
                
                # Excel exportieren
                excel_buffer = io.BytesIO()
                with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False, sheet_name='Noten')
                excel_buffer.seek(0)
                
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                st.download_button(
                    label="📥 Excel-Datei herunterladen",
                    data=excel_buffer,
                    file_name=f"Gefilterte_Noten_{timestamp}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )
                
                # CSV exportieren
                csv_buffer = io.StringIO()
                df.to_csv(csv_buffer, index=False, encoding='utf-8-sig')
                csv_data = csv_buffer.getvalue().encode('utf-8-sig')
                
                st.download_button(
                    label="📥 CSV-Datei herunterladen",
                    data=csv_data,
                    file_name=f"Gefilterte_Noten_{timestamp}.csv",
                    mime="text/csv",
                    use_container_width=True
                )
                
            else:
                st.warning("⚠️ Keine Noten gefunden, die den Kriterien entsprechen (1,0 oder 1,3)")
                
        except Exception as e:
            st.error(f"❌ Verarbeitungsfehler: {str(e)}")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 0.85em;'>NotenExtraktor v2.0 | Entwickelt mit Streamlit</p>", unsafe_allow_html=True)
