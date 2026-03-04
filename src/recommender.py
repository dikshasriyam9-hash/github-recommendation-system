import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("data/repos.csv")

data["description"] = data["description"].fillna("")

vectorizer = TfidfVectorizer(stop_words="english")
vectors = vectorizer.fit_transform(data["description"])

similarity = cosine_similarity(vectors)

def recommend(repo_name):
    repo_index = data[data["name"] == repo_name].index[0]
    distances = similarity[repo_index]

    repos_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    for i in repos_list:
        print(data.iloc[i[0]]["name"])
