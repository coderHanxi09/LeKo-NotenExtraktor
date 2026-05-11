import pdfplumber
import pandas as pd
import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# --- Kernlogik (Backend) ---
def process_pdf(pdf_path, target_grades=["1,0", "1,3"]):
    extracted_data = []
    stop_signal = "Diesen Ausdruck bitte unterschreiben"

    try:
        with pdfplumber.open(pdf_path) as pdf:
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

# --- Grafische Benutzeroberfläche (Frontend) ---
class GradeFilterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NotenExtraktor v1.1")
        self.root.geometry("450x250")
        
        self.label = tk.Label(root, text="PDF auswählen, um Noten (1,0 & 1,3) zu extrahieren", pady=20)
        self.label.pack()

        self.btn = tk.Button(root, text="Schritt 1: PDF Datei auswählen", 
                            command=self.select_file, 
                            width=30, height=2)
        self.btn.pack(pady=10)

        self.status = tk.Label(root, text="Status: Bereit", fg="gray")
        self.status.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Noten-PDF öffnen",
            filetypes=[("PDF Dateien", "*.pdf")]
        )
        if file_path:
            self.run_task(file_path)

    def run_task(self, file_path):
        try:
            self.status.config(text="Status: Verarbeitung...", fg="blue")
            self.root.update()
            
            data = process_pdf(file_path)
            
            if data:
                df = pd.DataFrame(data)
                output_file = os.path.join(os.path.dirname(file_path), "Gefilterte_Noten.xlsx")
                df.to_excel(output_file, index=False)
                
                messagebox.showinfo("Erfolg", f"Extraktion abgeschlossen!\nDatei: {output_file}")
                self.status.config(text="Status: Abgeschlossen", fg="green")
            else:
                messagebox.showwarning("Hinweis", "Keine passenden Noten gefunden.")
                self.status.config(text="Status: Keine Daten", fg="orange")
                
        except Exception as e:
            messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten:\n{str(e)}")
            self.status.config(text="Status: Fehlgeschlagen", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeFilterGUI(root)
    root.mainloop()