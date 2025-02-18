# Prototyp zur automatisierten Themenerfassung von Zeitschriftentitelseiten mittels multimodaler Modelle

Dieses Repository wurde wurde im Rahmen einer IU-Hausarbeit im Modul **"Programmieren mit Python"** erstellt.  

---

## 🚀 Projektbeschreibung

Das Ziel dieses Projekts ist die **automatisierte Themenerfassung** von Zeitschriftentitelseiten mithilfe multimodaler Modelle.  
Hierbei wird **LLaMA 3.2 Vision** über **Ollama** verwendet und die Ergebnisse anschließend **evaluiert**.

---

## 🛠️ Installation & Setup

### **1. Voraussetzungen**
- **Python 3.8+** installiert
- **[Ollama](https://ollama.com)** muss lokal installiert und ausgeführt werden
- Modell vorab laden:
  ```bash
  ollama pull llama3.2-vision
  ```

### **2. Repository klonen und hinterlegte Abhängigkeiten installieren**
  ```bash
  git clone https://github.com/younesfilali234/poc-multimodal-models-for-topic-extraction-on-covers.git
  cd poc-multimodal-models-for-topic-extraction-on-covers
  pip install -r requirements.txt
  ```

---

## ▶️ Nutzung

1️⃣ **Bilder für die Verarbeitung in den Ordner `data/covers/` Ordner legen**  
2️⃣ **Pipeline starten**  
  ```bash
  python main.py
  ```
3️⃣ **Ergebnisse werden gespeichert in `data/evaluation/results.csv`**  

---

📌 **Weitere Details sind in der Hausarbeit enthalten.**  
