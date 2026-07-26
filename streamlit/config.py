import pickle
import pandas as pd

# Load models
tfidf = pickle.load(open("tfidf.pkl", "rb"))
cosine_sim = pickle.load(open(r"C:\Users\krish\OneDrive\Desktop\IRS for E-Learning Platforms\cosine_similarity.pkl", "rb"))
indices = pickle.load(open("course_indices.pkl", "rb"))
user_similarity = pickle.load(open(r"C:\Users\krish\OneDrive\Desktop\IRS for E-Learning Platforms\user_similarity.pkl", "rb"))

# Load course dataset
courses = pd.read_pickle("courses.pkl")