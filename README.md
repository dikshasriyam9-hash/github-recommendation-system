# GitHub Project Recommendation System

This project recommends GitHub repositories based on their description similarity.

## How it works

1. The system loads repository data from `repos.csv`.
2. It converts repository descriptions into numerical vectors using TF-IDF.
3. Cosine similarity is used to measure how similar repositories are.
4. When a user selects a repository, the system recommends similar repositories.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

## Project Structure

github-recommendation-system
│
├── data
│   └ repos.csv
│
├── src
│   ├ fetch_data.py
│   ├ recommender.py
│   └ recommend.py
│
├── requirements.txt
│
└ README.md

## How to Run

1. Install dependencies

pip install -r requirements.txt

2. Run the program

python src/recommend.py
