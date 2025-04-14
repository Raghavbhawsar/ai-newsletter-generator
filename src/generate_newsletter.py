from datetime import datetime
import os

def generate_newsletter(user_articles):
    os.makedirs("output", exist_ok=True)
    for user, articles in user_articles.items():
        md = f"# {user}'s Personalized Newsletter\n"
        md += f"*Generated on {datetime.now().strftime('%Y-%m-%d')}*\n\n"
        md += "## Top Stories\n"
        md += f"Here are {len(articles)} articles tailored to your interests:\n\n"
        for i, article in enumerate(articles, 1):
            md += f"### {i}. {article['title']}\n"
            md += f"- **Source**: {article['source']}\n"
            md += f"- **Summary**: {article['summary'][:200]}...\n"
            md += f"- [Read More]({article['link']})\n\n"
        with open(f"output/{user.replace(' ', '_')}_newsletter.md", "w", encoding="utf-8") as f:
            f.write(md)

if __name__ == "__main__":
    sample = {
        "Alex Parker": [{
            "title": "AI Breakthrough",
            "source": "TechCrunch",
            "summary": "New AI model achieves major milestone...",
            "link": "http://example.com"
        }]
    }
    generate_newsletter(sample)
