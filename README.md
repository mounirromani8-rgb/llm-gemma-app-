# llm-gemma-app-
Une application simple et locale pour discuter avec un modèle de langage Gemma via Ollama, construite avec Streamlit.
# llm-gemma-app-
Une application simple et locale pour discuter avec un modèle de langage Gemma via Ollama, construite avec Streamlit.
💬 Gemma Chat App

# 💬 Gemma Chat App  

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-ff4b4b)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-Model%20Runner-black)](https://ollama.ai/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success)](#)

Une application **Streamlit** qui te permet de discuter avec un modèle de langage **Gemma** local via **Ollama** 🧠  
Aucune clé API, aucun coût, 100 % local et privé.  

---

## 🚀 Fonctionnalités
✅ Interface conversationnelle moderne (type ChatGPT)  
✅ Exécution **locale** sans dépendance cloud  
✅ Compatible avec tous les modèles Ollama (`gemma`, `llama3`, `mistral`, etc.)  
✅ Code Python clair, facilement modifiable  

---

## 🧩 Prérequis

### 1️⃣ Installer Ollama  
Télécharge et installe Ollama ici 👉 [https://ollama.ai/download](https://ollama.ai/download)

Puis télécharge le modèle **Gemma** :
```bash
ollama pull gemma


2️⃣ Installer les dépendances Python

Crée un environnement virtuel (optionnel mais recommandé) :
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows




Puis installe les dépendances :

pip install -r requirements.txt