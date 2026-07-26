# Intelligence Recommendation System for E-Learning Platforms

An AI-powered course recommendation system built using **Python, Streamlit, Scikit-learn, and Pandas**. The application recommends relevant e-learning courses using both **Content-Based Filtering** and **Collaborative Filtering** techniques.

## Features
- Content-Based Course Recommendation
- Collaborative Filtering Recommendation
- Simple and Interactive Streamlit UI
- Fast course search and personalized suggestions

## Tech Stack
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Pickle

## Project Structure
```
streamlit/
│── app.py
│── config.py
│── content_based.py
│── collaborative.py
│── generate_interactions.py
│── clean_courses.csv
│── courses.pkl
│── course_indices.pkl
│── cosine_similarity.pkl
│── user_similarity.pkl
```

## Installation

```bash
git clone https://github.com/<your-username>/intelligence-recommendation-system-for-e-learning-platforms.git

cd intelligence-recommendation-system-for-e-learning-platforms

pip install -r requirements.txt

streamlit run streamlit/app.py
```

## Demo

Open the Streamlit app in your browser after running the above command.

## Author

**Krishna Vansh**
