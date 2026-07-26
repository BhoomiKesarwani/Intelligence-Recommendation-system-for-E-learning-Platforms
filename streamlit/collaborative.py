# collaborative.py

from unittest import result

from config import courses, user_similarity
import pandas as pd

# Load interactions dataset
interactions = pd.read_csv("research_interactions.csv")

# Convert similarity matrix to DataFrame if needed
if not isinstance(user_similarity, pd.DataFrame):
    user_similarity_df = pd.DataFrame(
        user_similarity,
        index=interactions["user_id"].unique(),
        columns=interactions["user_id"].unique()
    )
else:
    user_similarity_df = user_similarity

# Create lookup table
course_lookup = courses.set_index("course_id")


missing = set(interactions["course_id"]) - set(courses["course_id"])

print("Missing course IDs:", len(missing))
print(list(missing)[:20])

def collaborative_recommend(user_id, top_n=10):
    """
    Recommend courses for a user using User-User Collaborative Filtering.
    """

    # Check if user exists
    if user_id not in user_similarity_df.index:
        return []

    # Find top 10 similar users
    similar_users = (
        user_similarity_df[user_id]
        .sort_values(ascending=False)
        .index[1:11]
    )

    # Courses already rated by the user
    watched = interactions[
        interactions["user_id"] == user_id
    ]["course_id"].tolist()

    # Ratings from similar users
    recommendations = interactions[
        interactions["user_id"].isin(similar_users)
    ]

    recommendations = (
        recommendations
        .groupby("course_id")["rating"]
        .mean()
        .sort_values(ascending=False)
    )

    # Remove courses already seen
    recommendations = recommendations[
        ~recommendations.index.isin(watched)
    ]

    # Top recommendations
    recommendations = recommendations.head(top_n)
    # valid_ids = recommendations.index.intersection(course_lookup.index)

    # Get course details
    valid_ids = recommendations.index.intersection(course_lookup.index)

    result = course_lookup.loc[valid_ids][
    [
        "course_name",
        "platform",
        "category",
        "level",
        "rating"
    ]
   ].copy()

    result["predicted_rating"] = recommendations.loc[valid_ids].values

    return result.reset_index(drop=True)