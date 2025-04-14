import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="📰 Personalized Newsletter", layout="wide")

st.title("🧠 AI-Powered Personalized Newsletter")
st.subheader("Curated news based on your interests")

# --- Sidebar for Category Selection ---
categories = ["AI", "Blockchain", "Movies", "Football", "Space"]
selected = st.sidebar.multiselect("Choose your interests:", categories, default=["AI"])

# --- Get Base Directory ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # one level above /app
DATA_DIR = os.path.join(BASE_DIR, "data")  # path to /data folder

# --- Load & Display Articles ---
if selected:
    for cat in selected:
        file_path = os.path.join(DATA_DIR, f"{cat}.csv")  # Safe and absolute path

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
