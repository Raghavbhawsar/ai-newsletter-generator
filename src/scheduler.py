import schedule, time
from fetch_articles import fetch_articles
from categorize import categorize_articles
from personalize import personalize_articles
from generate_newsletter import generate_newsletter

def job():
    print("Running newsletter generation...")
    fetch_articles()
    categorize_articles()
    user_articles = personalize_articles()
    generate_newsletter(user_articles)
    print("Done!")

schedule.every().day.at("08:00").do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)
