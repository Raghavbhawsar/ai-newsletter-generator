from src.fetch_articles import fetch_articles
from src.categorize import categorize_articles
from src.personalize import personalize_articles
from src.generate_newsletter import generate_newsletter

def main():
    print("Starting newsletter generation...")
    fetch_articles()
    categorize_articles()
    user_articles = personalize_articles()
    generate_newsletter(user_articles)
    print("Newsletters generated in output/ folder!")

if __name__ == "__main__":
    main()
