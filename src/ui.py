import streamlit as st
import pandas as pd
import os
from personas import personas  # 👈 Import personas

st.set_page_config(page_title="📰 Personalized Newsletter", layout="wide")

st.title("🧠 AI-Powered Personalized Newsletter")
st.subheader("Curated news based on your interests")

# --- Sidebar: Choose User Persona or Custom Interests ---
persona_names = list(personas.keys())
selected_persona = st.sidebar.selectbox("Choose a User Persona:", ["Custom"] + persona_names)

# --- If persona is selected, auto-select their interests ---
if selected_persona != "Custom":
    selected = personas[selected_persona]["interests"]
    st.sidebar.markdown(f"**Interests of {selected_persona}:** {', '.join(selected)}")
else:
    categories = ["AI", "Blockchain", "Movies", "Football", "Space"]
    selected = st.sidebar.multiselect("Choose your interests:", categories, default=["AI"])

# --- Load & Display Articles ---
if selected:
    for cat in selected:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(BASE_DIR, "data", f"{cat}.csv")

        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            if not df.empty:
                st.markdown(f"### 🗂️ {cat} News")
                for _, row in df.iterrows():
                    st.markdown(f"**{row['title']}**  \n{row['summary']}  \n[Read More]({row['link']})", unsafe_allow_html=True)
                    st.markdown("---")
            else:
                st.info(f"No articles found for {cat}.")
        else:
            st.warning(f"No data available for {cat}.")
else:
    st.info("Select at least one category from the sidebar.")
