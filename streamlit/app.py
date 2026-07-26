import streamlit as st
import pandas as pd
from content_based import recommend_courses
from collaborative import collaborative_recommend



# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="E-Learning Recommendation System",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------
courses = pd.read_csv("clean_courses.csv")
users = pd.read_csv("research_users.csv")
interactions = pd.read_csv("research_interactions.csv")


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🎓 E-Learning Platform")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📚 Recommend Courses",
        "📊 Analytics", 
        "ℹ About"
    ]
)


# -----------------------------
# Home Page
# -----------------------------
if page == "🏠 Home":

    st.title("🎓 Intelligent E-Learning Recommendation System")

    st.markdown("""
    Welcome to the **AI-powered E-Learning Recommendation System**.
 """)
   
    

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📚 Courses",
        len(courses)
    )

    col2.metric(
        "👤 Users",
        len(users)
    )

    col3.metric(
        "⭐ Interactions",
        len(interactions)
    )

    col4.metric(
        "🏆 Categories",
        courses["category"].nunique()
    )

    st.divider()

    st.subheader("🔥 Top Rated Courses")

    top_courses = courses.sort_values(
        "rating",
        ascending=False
    ).head(5)

    st.dataframe(
        top_courses[
            [
                "course_name",
                "platform",
                "category",
                "rating"
            ]
        ],
        use_container_width=True
    )

    st.divider()

    st.subheader("📌 Features")

    c1, c2 = st.columns(2)

    with c1:
        st.success("✅ Content-Based Recommendation")
        st.success("✅ Collaborative Filtering")
        st.success("✅ Search Courses")

    with c2:
        st.success("✅ Analytics Dashboard")
        st.success("✅ Download Recommendations")
        st.success("✅ Interactive UI")

# -----------------------------
# Recommendation Page
# -----------------------------
elif page == "📚 Recommend Courses":

    st.title("🎓 Course Recommendation")
   

    recommendation_type = st.radio(
        "Choose Recommendation Type",
        ["Content-Based", "Collaborative"],
        horizontal=True
    )


    # -------------------------------
    # Content-Based Recommendation
    # -------------------------------
    if recommendation_type == "Content-Based":

        st.subheader("📖 Content-Based Recommendation")

        course_name = st.selectbox(
            "Select a Course",
            sorted(courses["course_name"].unique())
        )

        top_n = st.slider(
            "Number of Recommendations",
            1,
            5,
            3,
            key="content_slider"
        )

        platform = st.selectbox(
                   "Platform",
                   ["All"] + sorted(courses["platform"].unique().tolist())
        )
        level = st.selectbox(
                   "Level",
                   ["All"] + sorted(courses["level"].unique().tolist())
        )
        
        category = st.selectbox(
                   "Category",
                   ["All"] + sorted(courses["category"].unique().tolist())
        ) 

        if st.button("Recommend Courses"):

            recommendations = recommend_courses(course_name, top_n)

            if recommendations.empty:
                st.warning("No recommendations found.")
            else:
                st.success(f"Top {top_n} recommendations for '{course_name}'")

                for _, row in recommendations.iterrows():

                    with st.container():

                        st.markdown("---")

                        col1, col2 = st.columns([5, 1])

                        with col1:

                            st.subheader(f"📚 {row['course_name']}")
                            st.write(f"🏢 Platform: {row['platform']}")
                            st.write(f"📂 Category: {row['category']}")
                            st.write(f"🎯 Level: {row['level']}")

                        with col2:

                            st.metric("⭐ Rating", row["rating"])


    # -------------------------------
    # Collaborative Recommendation
    # -------------------------------
    else:

        st.subheader("👥 Collaborative Recommendation")

        user_id = st.selectbox(
            "Select User",
            sorted(interactions["user_id"].unique())
        )

        top_n = st.slider(
            "Number of Recommendations",
            1,
            5,
            3,
            key="collab_slider"
        )

        # Add Filters

        platform = st.selectbox(
           "Platform",
           ["All"] + sorted(courses["platform"].unique().tolist())
)

        level = st.selectbox(
           "Level",
           ["All"] + sorted(courses["level"].unique().tolist())
)

        category = st.selectbox(
           "Category",
           ["All"] + sorted(courses["category"].unique().tolist())
) 
        
        if st.button("Recommend for User"):

            recommendations = collaborative_recommend(user_id, top_n)

            if recommendations.empty:
                st.warning("No recommendations found.")
            else:
                st.success(f"Top {top_n} recommendations for {user_id}")
                
                for _, row in recommendations.iterrows():

                   with st.container():

                      st.markdown("---")

                      col1, col2 = st.columns([5,1])

                      with col1:

                         st.markdown(f"### 📚 {row['course_name']}")

                         st.write(f"🏢 **Platform:** {row['platform']}")

                         st.write(f"📂 **Category:** {row['category']}")

                         st.write(f"🎯 **Level:** {row['level']}")

                      with col2:

                         st.metric("⭐ Rating", row["rating"])

                         if "predicted_rating" in row:
                             st.metric("🤖 Score", round(row["predicted_rating"],2))


# -----------------------------
# Analytics
# -----------------------------
elif page == "📊 Analytics":

    st.title("📊 Analytics Dashboard")

    st.subheader("Platform Distribution")
    st.bar_chart(courses["platform"].value_counts())

    st.subheader("Category Distribution")
    st.bar_chart(courses["category"].value_counts())

    st.subheader("Course Levels")
    st.bar_chart(courses["level"].value_counts())

    st.subheader("Language Distribution")
    st.bar_chart(courses["language"].value_counts())
# -----------------------------
# About
# -----------------------------
elif page == "ℹ About":

    st.title("ℹ About")

    st.write("""
Project Name:
Intelligent Recommendation System for E-Learning Platforms

Developed using:

• Python

• Scikit-learn

• Streamlit

• Pandas
""")

    #py -m streamlit run app.py