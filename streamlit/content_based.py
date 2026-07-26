from config import courses, cosine_sim, indices
import pandas as pd
import builtins

def recommend_courses(course_name, top_n=10):

    if course_name not in indices:
        return pd.DataFrame()

    idx = indices[course_name]

    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores = builtins.sorted(
         similarity_scores,
         key=lambda x: x[1],
         reverse=True
    )[1:top_n+1]


    course_indices_list = [i[0] for i in similarity_scores]

    recommendations = courses.iloc[course_indices_list][
        [
            "course_name",
            "platform",
            "category",
            "level",
            "rating"
        ]
    ]

    return recommendations.reset_index(drop=True)