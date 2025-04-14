import json, pandas as pd
from collections import defaultdict

def load_users():
    with open("data/users.json", "r") as f:
        return json.load(f)

def personalize_articles():
    users = load_users()
    user_articles = defaultdict(list)
    for user in users:
        name = user["name"]
        interests = set(user["interests"])
        for interest in interests:
            interest_file = interest.replace(" ", "_")
            try:
                df = pd.read_csv(f"data/{interest_file}.csv")
                user_articles[name].extend(df.to_dict("records"))
            except FileNotFoundError:
                continue
        user_articles[name] = user_articles[name][:5]
    return user_articles

if __name__ == "__main__":
    personalize_articles()
