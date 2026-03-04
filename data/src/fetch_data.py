import requests
import pandas as pd

url = "https://api.github.com/search/repositories?q=machine+learning&sort=stars"

response = requests.get(url)
data = response.json()

repos = []

for repo in data["items"]:
    repos.append({
        "name": repo["name"],
        "description": repo["description"],
        "language": repo["language"],
        "stars": repo["stargazers_count"]
    })

df = pd.DataFrame(repos)
df.to_csv("data/repos.csv", index=False)

print("Dataset created")
