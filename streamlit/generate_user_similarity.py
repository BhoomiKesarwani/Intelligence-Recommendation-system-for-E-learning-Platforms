import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load interactions
interactions = pd.read_csv(
    r"research_interactions.csv"
)

# Create user-course matrix
user_course_matrix = interactions.pivot_table(
    index="user_id",
    columns="course_id",
    values="rating",
    fill_value=0
)

# Calculate similarity
user_similarity = cosine_similarity(user_course_matrix)

# Save similarity matrix
with open(
    r"C:\Users\krish\OneDrive\Desktop\IRS for E-Learning Platforms\user_similarity.pkl",
    "wb"
) as f:
    pickle.dump(user_similarity, f)

print("✅ user_similarity.pkl regenerated successfully!")
print("Shape:", user_similarity.shape)