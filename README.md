
# 🧠 AI-Powered Personalized Newsletter Generator

A smart and personalized newsletter generation system that curates news articles based on individual user interests. Built with Python, NLP, and Streamlit for an elegant UI experience.

---

## 🚀 Features

- 📰 Categorizes articles using NLP (spaCy)
- 📊 Supports user personas with unique interests and sources
- 📁 Outputs curated CSVs for each category
- 🎨 Beautiful Streamlit UI for personalized newsletter viewing
- ✅ Modular structure and easy to extend

---

## 👥 User Personas

1. **Alex Parker** – Tech Enthusiast (AI, Cybersecurity, Blockchain, Startups, Programming)  
   **Sources:** TechCrunch, MIT Tech Review, Wired, Ars Technica

2. **Priya Sharma** – Finance & Business Guru (Markets, Fintech, Crypto, Startups)  
   **Sources:** Bloomberg, Forbes, CoinDesk, Financial Times

3. **Marco Rossi** – Sports Journalist (Football, F1, NBA, Olympic Sports)  
   **Sources:** ESPN, BBC Sport, Sky Sports, The Athletic

4. **Lisa Thompson** – Entertainment Buff (Movies, Music, TV Shows, Celebrities)  
   **Sources:** Rolling Stone, Billboard, Variety, Hollywood Reporter

5. **David Martinez** – Science & Space Nerd (Space, Biotech, AI, Renewable Energy)  
   **Sources:** NASA, Nature, Science Daily, Ars Technica

---

## 🗂️ Project Structure

. ├── data/ # Curated articles by category (CSV) ├── src/ │ ├── categorize.py # NLP-based article categorization │ ├── ui.py # Streamlit-based UI ├── README.md └── requirements.txt

---

## 💻 How to Run

1. Clone the repo:
git clone https://github.com/your-username/ai-newsletter-generator.git cd ai-newsletter-generator

2. Create virtual environment (optional):
python -m venv venv venv\Scripts\activate # On Windows

3. Install dependencies:
pip install -r requirements.txt

4. Run the newsletter UI:
streamlit run src/ui.py

---

## 📌 Future Enhancements

- Add live web scraping from real sources
- Enable user login with preferences
- Email newsletter generation and scheduling
- Dark/light UI themes

---

## 📜 License

MIT License – feel free to use, modify, and share.
