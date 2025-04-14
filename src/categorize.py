import spacy, pandas as pd
from collections import defaultdict

nlp = spacy.load("en_core_web_sm")

def categorize_articles():
    df = pd.read_csv("data/articles.csv")
    categories = defaultdict(list)
    
    for _, row in df.iterrows():
        # Ensure both title and summary are converted to strings
        doc = nlp(str(row["title"]) + " " + str(row["summary"]))

        keywords = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
        
        if any(k in keywords for k in ["ai", "machine learning", "deep learning"]):
            categories["AI"].append(row.to_dict())
        if any(k in keywords for k in ["blockchain", "crypto", "bitcoin"]):
            categories["Blockchain"].append(row.to_dict())
        if any(k in keywords for k in ["football", "soccer"]):
            categories["Football"].append(row.to_dict())
        if any(k in keywords for k in ["movie", "film", "cinema"]):
            categories["Movies"].append(row.to_dict())
        if any(k in keywords for k in ["space", "nasa", "astronomy"]):
            categories["Space"].append(row.to_dict())

    for cat, items in categories.items():
        pd.DataFrame(items).to_csv(f"data/{cat}.csv", index=False)
    
    return categories

if __name__ == "__main__":
    categorize_articles()
