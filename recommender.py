import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    df = pd.read_csv("data.csv")
    return df

def prepare_data(df):
    df['combined_text'] = df['job_title'] + " " + df['job_description']
    return df

def vectorize_data(df):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['combined_text'])
    return vectorizer, tfidf_matrix

def recommend_jobs(user_input, df, vectorizer, vectors, top_n=3):
    user_vectors = vectorizer.transform([user_input])
    scores = cosine_similarity(user_vectors, vectors).flatten()
    indices = np.argsort(scores)[-top_n:][::-1]
    results = df.iloc[indices].copy()
    results['score'] = scores[indices]
    return results['job_title'].tolist()

if __name__ == "__main__":
    df = load_data()
    df = prepare_data(df)
    vectorizer, vectors = vectorize_data(df)
    results = recommend_jobs(["python data analyst"], df, vectorizer, vectors)
    print(results)


