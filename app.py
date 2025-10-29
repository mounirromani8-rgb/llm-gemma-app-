import streamlit as st
import ollama

# --- Configuration de l'app ---
st.set_page_config(page_title="💬 Gemma Chat App", page_icon="🤖", layout="centered")

# --- CSS pour le style ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f5f5;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Historique des messages ---
if 'messages' not in st.session_state:
    st.session_state.messages = []

# --- Titre ---
st.title("💬 Gemma Chat App")
st.markdown("Une interface moderne pour discuter avec le modèle **Gemma** (via Ollama)")

# --- Saisie utilisateur ---
prompt = st.chat_input("Pose ta question à Gemma...")

if prompt:
    # Ajoute le message utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Affiche le spinner pendant la réponse
    with st.spinner("Gemma réfléchit... 🤖"):
        try:
            result = ollama.chat(model="gemma", messages=[{"role": "user", "content": prompt}])
            response = result["message"]["content"]
        except Exception as e:
            response = f"⚠️ Erreur : {e}"

        # Ajoute la réponse de Gemma
        st.session_state.messages.append({"role": "assistant", "content": response})

# --- Affichage de l'historique sous forme de bulles ---
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(f"🧑 {msg['content']}")
    else:
        with st.chat_message("assistant"):
            st.markdown(f"🤖 {msg['content']}")
