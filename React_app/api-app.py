from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np
import joblib

# === Load model and encoders ===
model = joblib.load("course_preloader_model.pkl")
mlb_completed = joblib.load("mlb_completed.pkl")
mlb_categories = joblib.load("mlb_categories.pkl")
mlb_next = joblib.load("mlb_next.pkl")
#year_encoder = np.array([[int(input_data.year)]])
semester_encoder = joblib.load("semester_encoder.pkl")
popularity_scores = joblib.load("popularity_scores.pkl")
popularity_encoded= joblib.load("pop_encoded.pkl")
# === FastAPI setup ===
app = FastAPI()

# === Request schema ===
class StudentInput(BaseModel):
    completed_courses: List[str]
    year: str
    semester: str
    elective_categories: List[str]

# === Helper functions ===
def calculate_avg_popularity(courses):
    scores = [popularity_scores.get(course, 0) for course in courses]
    return np.mean(scores) if scores else 0.0

# === Prediction endpoint ===
@app.post("/predict")
def recommend_courses(input_data: StudentInput):
    try:
        # Encode features
        completed_encoded = mlb_completed.transform([input_data.completed_courses])
        print(f"Completed Encoded Shape: {completed_encoded.shape}")

        # Directly use the year as input
        year_encoded = np.array([[int(input_data.year)]])
        print(f"Year Encoded Shape: {year_encoded.shape}")

        # Encode the semester
        semester_encoded = semester_encoder.transform([input_data.semester.lower()]).reshape(-1, 1)
        print(f"Semester Encoded Shape: {semester_encoded.shape}")

        # Calculate average popularity
        popularity_encoded = np.array([[calculate_avg_popularity(input_data.completed_courses)]])
        print(f"Popularity Encoded Shape: {popularity_encoded.shape}")

        # Encode elective categories
        category_encoded = mlb_categories.transform([input_data.elective_categories])
        print(f"Category Encoded Shape: {category_encoded.shape}")

        # Combine all features into X
        X = np.hstack([completed_encoded, semester_encoded, year_encoded, popularity_encoded, category_encoded])
        print(f"Total Input Features Shape: {X.shape}")

        # Predict recommended courses
        y_pred = model.predict(X)
        predicted_courses = mlb_next.inverse_transform(y_pred)

        return {"recommended_courses": predicted_courses[0]}

    except Exception as e:
        print(e)
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    print(f"Training feature names: {list(df_courses.columns)}")
    print(f"Prediction input features: {list(X.columns)}")
