import joblib
import pandas as pd

# Load your model
model = joblib.load("course_preloader_model.pkl")

# Load your encoders and datasets
mlb_completed = joblib.load("mlb_completed.pkl")
mlb_categories = joblib.load("mlb_categories.pkl")
mlb_next = joblib.load("mlb_next.pkl")
#year_encoded= joblib.load("year_encoder.pkl")
semester_encoded = joblib.load("semester_encoder.pkl")
popularity_encoded = joblib.load("pop_encoded.pkl")
popularity_scores_of_random_student_data = joblib.load("popularity_scores.pkl")
#course_to_category = joblib.load("course_to_category.pkl")

df_courses = pd.read_csv("computer_science_courses.csv")
