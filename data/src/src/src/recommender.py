import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("data/repos.csv")

# Replace missing descriptions
data["description"] = data["description"].fillna("")

# Convert text into vectors
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(data["description"])

# Calculate similarity between repositories
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend(repo_name):
    repo_index = data[data["name"] == repo_name].index[0]
    scores = list(enumerate(similarity[repo_index]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    for i in scores:
        print(data.iloc[i[0]]["name"])
