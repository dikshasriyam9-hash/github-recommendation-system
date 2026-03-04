from recommender import recommend
import pandas as pd

data = pd.read_csv("data/repos.csv")

print("Available repositories:")
print(data["name"])

repo_name = input("Enter repository name: ")

recommend(repo_name)
