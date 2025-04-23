import joblib
import pandas as pd
import numpy as np

def load_assets():
    model = joblib.load("course_preloader_model.pkl")
    mlb_completed = joblib.load("mlb_completed.pkl")
    mlb_categories = joblib.load("mlb_categories.pkl")
    mlb_next = joblib.load("mlb_next.pkl")
    year_encoder = joblib.load("year_encoder.pkl")
    semester_encoder = joblib.load("semester_encoder.pkl")
    course_popularity = joblib.load("pop_encoded.pkl")  # Optional unless used in real-time
    df_courses = pd.read_csv("computer_science_courses.csv")
    return model, mlb_completed, mlb_categories, mlb_next, year_encoder, semester_encoder, df_courses

def avg_popularity(completed, popularity_dict):
    scores = [popularity_dict.get(course, 0) for course in completed]
    return np.mean(scores) if scores else 0

def encode_input(profile, mlb_completed, mlb_categories, year_encoder, semester_encoder, popularity_dict):
    completed_encoded = mlb_completed.transform([profile["CompletedCourses"]])
    category_encoded = mlb_categories.transform([profile["CompletedCategories"]])
    
    semester_encoded = semester_encoder.transform([[profile["Semester"]]])
    year_encoded = year_encoder.transform([[profile["Year"]]])
    
    popularity_score = avg_popularity(profile["CompletedCourses"], popularity_dict)
    popularity_encoded = np.array([[popularity_score]])
    
    final_input = np.hstack([completed_encoded, semester_encoded, year_encoded, popularity_encoded, category_encoded])
    return final_input

def predict_courses(profile):
    (model, mlb_completed, mlb_categories, mlb_next, 
     year_encoder, semester_encoder, df_courses) = load_assets()

    # Create popularity lookup dictionary from training data
    popularity_dict = joblib.load("popularity_scores.pkl")  # Precomputed popularity scores per course

    X_input = encode_input(profile, mlb_completed, mlb_categories, year_encoder, semester_encoder, popularity_dict)
    y_pred = model.predict(X_input)
    recommended_courses = mlb_next.inverse_transform(y_pred)[0]
    return recommended_courses

#if __name__ == "__main__":
    # Example student profile
    #student_profile = {
        #"CompletedCourses": ["CSCI151", "MATH151"],
       # "CompletedCategories": ["core", "math"],
        #"Semester": "fall",
       # "Year": 2
 #   }

  #  recommendations = predict_courses(student_profile)
   # print("Recommended Courses:", recommendations)

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List
# import numpy as np

# # Assuming you already have your model, encoders, and df_courses loaded here
# # from your existing code logic
# # You should move model training and loading outside the API logic if possible (to avoid retraining)

# app = FastAPI()

# # Input model for POST requests
# class StudentInput(BaseModel):
#     current_year: int
#     current_semester: str
#     completed_courses: List[str]

# @app.post("/recommend")
# def recommend_courses(input: StudentInput):
#     try:
#         # Transform inputs like you did in your training pipeline
#         semester_encoded = np.array([
#             1 if input.current_semester.lower() == "fall" else 0,
#             1 if input.current_semester.lower() == "spring" else 0
#         ]).reshape(1, -1)

#         year_encoded = np.array([
#             1 if input.current_year == 1 else 0,
#             1 if input.current_year == 2 else 0,
#             1 if input.current_year == 3 else 0,
#             1 if input.current_year == 4 else 0
#         ]).reshape(1, -1)

#         completed_encoded = mlb_completed.transform([input.completed_courses])
#         avg_popularity = np.array([[df_courses[df_courses["CourseID"].isin(input.completed_courses)]["Popularity Score"].astype(float).mean() or 0]])

#         completed_categories = [course_to_category[course] for course in input.completed_courses if course in course_to_category]
#         category_encoded_input = mlb_categories.transform([completed_categories])

#         # Final input vector
#         X_input = np.hstack([
#             completed_encoded,
#             semester_encoded,
#             year_encoded,
#             avg_popularity,
#             category_encoded_input
#         ])

#         # Predict
#         prediction = model.predict(X_input)
#         recommended_courses = mlb_next.inverse_transform(prediction)[0]

#         return {"recommended_courses": recommended_courses}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
