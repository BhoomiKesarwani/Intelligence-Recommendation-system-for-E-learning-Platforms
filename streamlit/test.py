import pandas as pd

# courses = pd.read_csv(r"C:\Users\krish\OneDrive\Desktop\IRS for E-Learning Platforms\clean_courses.csv")
# print(courses.columns.tolist())

# users = pd.read_csv(r"C:\Users\krish\OneDrive\Desktop\IRS for E-Learning Platforms\research_users.csv")
# print(users.columns.tolist())

import pandas as pd

courses = pd.read_csv(
    r"C:\Users\krish\OneDrive\Desktop\IRS for E-Learning Platforms\clean_courses.csv"
)

interactions = pd.read_csv(
    r"C:\Users\krish\OneDrive\Desktop\IRS for E-Learning Platforms\research_interactions.csv"
)

missing = set(interactions["course_id"]) - set(courses["course_id"])

print("Missing IDs:", len(missing))