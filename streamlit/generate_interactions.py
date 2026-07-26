import pandas as pd
import numpy as np

# -------------------------
# Load datasets
# -------------------------
courses = pd.read_csv(
    "clean_courses.csv"
)

users = pd.read_csv(
    "research_users.csv"
)

# -------------------------
# Configuration
# -------------------------
NUM_INTERACTIONS = 100000

np.random.seed(42)

# -------------------------
# Generate interactions
# -------------------------
interactions = pd.DataFrame({
    "user_id": np.random.choice(users["user_id"], NUM_INTERACTIONS),

    "course_id": np.random.choice(courses["course_id"], NUM_INTERACTIONS),

    "rating": np.random.randint(1, 6, NUM_INTERACTIONS),

    "completion_status": np.random.choice(
        ["Completed", "In Progress", "Dropped"],
        NUM_INTERACTIONS,
        p=[0.5, 0.4, 0.1]
    ),

    "watch_time_hours": np.random.randint(1, 101, NUM_INTERACTIONS),

    "timestamp": pd.to_datetime(
        np.random.randint(
            pd.Timestamp("2024-01-01").value // 10**9,
            pd.Timestamp("2025-12-31").value // 10**9,
            NUM_INTERACTIONS
        ),
        unit="s"
    )
})

# -------------------------
# Save
# -------------------------
output_path = r"research_interactions.csv"

interactions.to_csv(output_path, index=False)

print("Dataset Generated Successfully!")
print(interactions.head())

print("\nTotal Interactions:", len(interactions))
print("Unique Users:", interactions["user_id"].nunique())
print("Unique Courses:", interactions["course_id"].nunique())