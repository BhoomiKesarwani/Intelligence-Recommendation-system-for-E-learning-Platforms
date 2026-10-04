
import pickle
import pandas as pd
from pathlib import Path

# Get the directory containing config.py
BASE_DIR = Path(__file__).resolve().parent


# Load pickle files safely using relative paths
def load_pickle(filename):
    file_path = BASE_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(
            f"Missing file: {file_path}"
        )

    with file_path.open("rb") as file:
        return pickle.load(file)


# Load models
tfidf = load_pickle("tfidf.pkl")
cosine_sim = load_pickle("cosine_similarity.pkl")
indices = load_pickle("course_indices.pkl")
user_similarity = load_pickle("user_similarity.pkl")

# Load course dataset
courses = pd.read_pickle(BASE_DIR / "courses.pkl")



# import pickle
# import pandas as pd

# # Load models
# tfidf = pickle.load(open("tfidf.pkl", "rb"))
# cosine_sim = pickle.load(open(r"C:\Users\krish\OneDrive\Desktop\IRS for E-Learning Platforms\cosine_similarity.pkl", "rb"))
# indices = pickle.load(open("course_indices.pkl", "rb"))
# user_similarity = pickle.load(open(r"C:\Users\krish\OneDrive\Desktop\IRS for E-Learning Platforms\user_similarity.pkl", "rb"))

# # Load course dataset
# courses = pd.read_pickle("courses.pkl")