import pandas as pd
courses = [
    ["CSCI151", "Intro to Computer Science I", 4, "", "Core", 100, "fall", 1 ],
    ["CSCI152", "Intro to Computer Science II", 4, "CSCI151", "Core", 100, "spring", 1 ],
    ["CSCI257", "Object-Oriented Programming", 4, "CSCI152", "Core", 100, "fall", 2 ],
    ["CSCI258", "Data Structures and Algorithms", 4, "CSCI257", "Core", 100, "spring",2 ],
    ["CSCI264", "Comp. Structure & Assembly Language", 4, "", "Core", 100, "spring",2 ],
    ["CSCI347", "Computer Architecture I", 3, "CSCI258,CSCI264", "Core", 100, "spring",3 ],
    ["CSCI344", "Programming Languages", 3, "CSCI258", "Core", 100, "spring",3],
    ["CSCI373", "Software Engineering", 3, "CSCI258", "Core", 100, "spring",3],
    ["CSCI398", "Research Topics", 1, "", "Core", 100, "spring",3],
    ["CSCI451", "Operating Systems I", 3, "CSCI258", "Core",100, "fall",4],
    ["CSCI408", "Senior Project I", 2, "CSCI398", "Core",100, "fall",4],
    ["CSCI409", "Senior Project II", 2, "CSCI408", "Core",100, "spring",4],
    ["MATH151", "Elementary Discrete Mathematics I", 3, "", "Math",100, "both",1],
    ["MATH152", "Elementary Discrete Mathematics II", 3, "MATH151", "Math",100, "both",1],
    ["MATH141", "Calculus I", 4, "", "Math",100, "both",1],#pre-req: score on placement test or MATH-120
    ["MATH142", "Calculus II", 4, "MATH141", "Math",100, "both",1],
    ["MATH273", "Introduction to Probability", 3, "MATH142", "Math",100, "both",4],
    ["PHYS111", "Physics of Digital Circuits", 2, "", "Physics",100, "fall",2],
    ["PHYS141", "College Physics I", 4, "", "Physics",100, "fall",3],
    ["PHYS143", "College Physics I Lab", 1, "PHYS141", "Physics",100, "fall",3],
    ["PHYS142", "College Physics II", 4, "PHYS141", "Physics",100, "spring",3],
    ["PHYS144", "College Physics II Lab", 1, "PHYS142", "Physics",100, "spring",3],
    ["PHIL120", "Symbolic Logic", 3, "", "Philosophy",100, "both",2],
    ["ASC101", "Thinking Through", 3, "", "Gen Ed",100, "both",1],
    ["ASC401", "Transformations Capstone", 3, "", "Gen Ed",100, "both",4], #need at least 90 completed credits/dean approval
    ["ENGL101", "Reading, Thinking and Writing", 3, "", "Gen Ed",100, "fall",1],
    # (CS) Electives with prerequisites
    ["CSCI391", "Practical Cryptology", 3, "CSCI151, MATH151, PHIL120", " Security Elective",66, "spring",2],
    ["CSCI392", "Network and Computer Security", 3, "CSCI391, CSCI257", "Security Elective",57, "fall",3],
    ["CSCI348", "Computer Architecture II", 3, "CSCI347", "Systems/Theory Elective",5,"fall",3],
    ["CSCI452", "OSs II", 3, "CSCI451", "Systems/Theory Elective",1, "spring",4],
    ["CSCI355", "Artificial Intelligence I", 3, "CSCI258, PHIL120", "AI Elective",55, "fall",4],
    ["CSCI381", "Computer Network I", 3, "CSCI152", "Systems/Theory Elective",18, "fall",2],
    ["CSCI356", "Artificial Intelligence II", 3, "CSCI355", "AI Elective",13,"spring",4],
    ["CSCI382", "Computer Networking II", 3, "CSCI381", "Systems/Theory Elective",9,"spring",2],
    ["CSCI311", "Mobile App Development", 3, "CSCI258", "Development Elective",43.75,"spring",3],
    ["CSCI434", "Database Systems I", 3, "CSCI258", "Data Elective",77, "fall",3],
    ["CSCI435", "Database Systems II", 3, "CSCI434", " Data Elective",74, "spring",3],
    ["CSCI349", "Parallel Computing", 3, "CSCI258", "Systems/Theory based Elective",60,"fall",3],
    ["CSCI350", "Parallel Computing II", 3, "CSCI349", "Systems/Theory Elective",50,"spring",3],
    ["CSCI371", "Computer Graphics (I)", 3, "CSCI258", "Development Elective",72,"fall",3],
    ["CSCI372", "Computer Graphics 2", 3, "CSCI371","Development Elective", 70, "spring",3],
    ["CSCI375", "Game Design & Programming",3,"CSCI257","Gaming Elective", 74,"fall",3],
    ["CSCI376", "Game Design & Programming 2",3, "CSCI375", "Gaming Elective", 71,"spring",3],
    ["CSCI393", "Computer Forensics",3,"MATH151, PHIL120", "Security Elective", 75,"spring",2]
]

# Convert to DataFrame
df = pd.DataFrame(courses, columns=["CourseID", "Course Name", "Credits", "Prerequisites/Concurrent PHYS Lab/Possible CS257 (or 58) Co-req for CS392", "Category", "Popularity Score", "Semester Offered", "Typical Year Recommended"])
df["Prerequisites/Concurrent PHYS Lab/Possible CS257 (or 58) Co-req for CS392"] = df["Prerequisites/Concurrent PHYS Lab/Possible CS257 (or 58) Co-req for CS392"].fillna("")
df.to_csv("computer_science_courses.csv", index=False)
#df
# Save as CSV file
csv_filename = "computer_science_courses.csv"
df.to_csv(csv_filename, index=False)

# Return the file path for downloading
csv_filename
df = pd.read_csv("computer_science_courses.csv")
df["Prerequisites/Concurrent PHYS Lab/Possible CS257 (or 58) Co-req for CS392"] = df["Prerequisites/Concurrent PHYS Lab/Possible CS257 (or 58) Co-req for CS392"].fillna("")  # Replace NaN with empty string
df["Prerequisites/Concurrent PHYS Lab/Possible CS257 (or 58) Co-req for CS392"] = df["Prerequisites/Concurrent PHYS Lab/Possible CS257 (or 58) Co-req for CS392"].apply(lambda x: x.strip() if isinstance(x, str) else "")
import networkx as nx
import matplotlib.pyplot as plt
import sklearn as sk
import graphviz
course_dag = nx.DiGraph() #initialized a Directed Graph
#df
# Add nodes (Courses)
for course in df["CourseID"]:
    course_dag.add_node(course)

# Add edges (Prerequisite relationships)
for _, row in df.iterrows():
    course = row["CourseID"]
    prerequisites = (row["Prerequisites/Concurrent PHYS Lab/Possible CS257 (or 58) Co-req for CS392"]).split(",")  # Handle multiple prereqs
    
    #debug
    print(f"Course: {course} | Prerequisites: {prerequisites}") 

    for prereq in prerequisites:
        prereq = prereq.strip()
        print(f"Checking prerequisite: '{prereq}'")
        if prereq and prereq in course_dag.nodes:  # Ensure valid prereq
            course_dag.add_edge(prereq, course)
            print(f"Added edge: {prereq} -> {course}")
        elif not prereq:
            print(f"No prerequisites for {course}, skipping edge creation.")
        else:
            # Debug: Print invalid prerequisites that are not in the DAG
            #if prereq:
                #print(f"Skipping invalid prereq: {prereq} for course: {course}")
            # Debug: Print the issue if prereq doesn't match an existing course
            print(f"Skipping invalid prereq: {prereq} for course: {course}")
            # Print all course nodes to verify if prereq matches
            print(f"Available courses: {list(course_dag.nodes)}")
# DAG visual
plt.figure(figsize=(18, 11))
pos = nx.spring_layout(course_dag, k=1, seed=42, scale=2)  # Layout for better spacing
nx.draw(course_dag, pos, with_labels=True, node_color="gold", edge_color="lightblue", node_size=1500, font_size=10)
plt.title(" CS's Student Course Pre-requisite DAG")
plt.show()

# Debug: Print all edges
print(f"Edges in the DAG: {list(course_dag.edges())}")

import random
import numpy as np
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
semester_encoder = LabelEncoder()
year_encoder = LabelEncoder()
semester_encoded = semester_encoder.fit_transform(["spring", "fall"])

# Set display options
pd.set_option('display.max_colwidth', None)

# Assuming 'courses' is defined and loaded as before
df_courses = pd.DataFrame(courses, columns=[
    "CourseID", "Course Name", "Credits", 
    "Prerequisites/Concurrent PHYS Lab/Possible CS257 (or 58) Co-req for CS392", 
    "Category", "Popularity Score", "Semester Offered", "Typical Year Recommended"
])
# Map CourseID to Category
course_to_category = df_courses.set_index("CourseID")["Category"].to_dict()

# Generate random student data
def generate_student_data(num_students, courses_df):
    student_data = []
    course_ids = courses_df["CourseID"].tolist()
    semesters = ["fall", "spring"]
    years = [1, 2, 3, 4]
    
    for student_id in range(num_students):
        completed_courses = random.sample(course_ids, random.randint(5, 10))
        current_year = random.choice(years)
        current_semester = random.choice(semesters)
        
        student_data.append({
            "StudentID": f"S{student_id+1}",
            "CompletedCourses": completed_courses,
            "CurrentYear": current_year,
            "CurrentSemester": current_semester
        })
    
    return pd.DataFrame(student_data)

students_df = generate_student_data(num_students=250, courses_df=df_courses)

# Course recommendation logic
def recommend_courses(student_row, df_courses):
    completed_courses = student_row["CompletedCourses"]
    current_year = student_row["CurrentYear"]
    current_semester = student_row["CurrentSemester"]
    
    available_courses = []
    
    for _, row in df_courses.iterrows():
        course = row["CourseID"]
        prerequisites = row["Prerequisites/Concurrent PHYS Lab/Possible CS257 (or 58) Co-req for CS392"]
        prerequisites = prerequisites.split(",") if prerequisites else []
        prerequisites = [prereq.strip() for prereq in prerequisites]
        semester_offered = row["Semester Offered"]
        typical_year = row["Typical Year Recommended"]
        
        if all(prereq in completed_courses for prereq in prerequisites):
            if (typical_year == current_year or typical_year == "both") and \
               (semester_offered == student_row["CurrentSemester"] or semester_offered == "both"):
                available_courses.append(course)
    
    return available_courses

students_df["RecommendedCourses"] = students_df.apply(lambda row: recommend_courses(row, df_courses), axis=1)

# Simulate which of the recommended courses the student might take next
def simulate_next_courses(row):
    if len(row["RecommendedCourses"]) > 0:
        return random.sample(row["RecommendedCourses"], min(3, len(row["RecommendedCourses"])))
    else:
        return []

students_df["NextCourses"] = students_df.apply(simulate_next_courses, axis=1)
# Print simulated next courses for each student
print("\n=== Simulated Next Courses ===")
for i, row in students_df.iterrows():
    print(f"Student {row['StudentID']}: {row['NextCourses']}")

# Get categories from completed courses
def extract_categories(completed_courses):
    return [course_to_category[course] for course in completed_courses if course in course_to_category]

students_df["CompletedCategories"] = students_df["CompletedCourses"].apply(extract_categories)

# === Feature Engineering ===

# Encode completed courses
mlb_completed = MultiLabelBinarizer()
completed_encoded = mlb_completed.fit_transform(students_df["CompletedCourses"])

# Encode semester/year
semester_encoded = pd.get_dummies(students_df["CurrentSemester"], prefix="Sem")
year_encoded = pd.get_dummies(students_df["CurrentYear"], prefix="Year")

# Add popularity score of completed courses as feature
def avg_popularity(completed_list):
    if not completed_list:
        return 0
    scores = df_courses[df_courses["CourseID"].isin(completed_list)]["Popularity Score"].astype(float)
    return scores.mean() if not scores.empty else 0

students_df["AvgPopularity"] = students_df["CompletedCourses"].apply(avg_popularity)
popularity_encoded = students_df["AvgPopularity"].values.reshape(-1, 1)

mlb_categories = MultiLabelBinarizer()
category_encoded = mlb_categories.fit_transform(students_df["CompletedCategories"])

# Final features
X = np.hstack([completed_encoded, semester_encoded.values, year_encoded.values, popularity_encoded, category_encoded])

# Encode targets (next courses)
mlb_next = MultiLabelBinarizer()
y = mlb_next.fit_transform(students_df["NextCourses"])

# === Train/Test Split ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === Train Model ===
rf = RandomForestClassifier(n_estimators=200, random_state=42, max_depth=None, min_samples_split=2,class_weight='balanced',)
model = MultiOutputClassifier(rf)
model.fit(X_train, y_train)

# === Predictions ===
y_pred = model.predict(X_test)
predicted_courses = mlb_next.inverse_transform(y_pred)
actual_courses = mlb_next.inverse_transform(y_test)

# Get predicted probabilities
#y_probs = np.array([estimator.predict_proba(X_test) for estimator in model.estimators_])
#y_probs_avg = np.mean(y_probs, axis=0)  # average across trees

# Predict with lower threshold (e.g., 0.3 instead of 0.5)
#y_pred_custom = (y_probs_avg >= 0.3).astype(int)

# Re-evaluate
#print("\n=== Classification Report (Threshold = 0.3) ===")
#print(classification_report(y_test, y_pred_custom, target_names=mlb_next.classes_, zero_division=0))

# === Evaluation ===
print("\n=== Sample Predictions vs Actual ===")
for i in range(len(predicted_courses)):
    print(f"Student {i+1}:")
    print(f"  Predicted: {predicted_courses[i]}")
    print(f"  Actual   : {actual_courses[i]}")
    print("")

print("\n=== Classification Report (Macro Avg, Micro Avg) ===")
print(classification_report(y_test, y_pred, target_names=mlb_next.classes_, zero_division=0))

# Safely get class 1 probabilities or fallback to zeros
#y_probs = []
#for estimator in model.estimators_:
 #   proba = estimator.predict_proba(X_test)
    
    # If only one class seen during training, it might return shape (n_samples, 1)
  #  if proba.shape[1] == 2:
       # class1_probs = proba[:, 1]
   # else:
        # Only class 0 exists, so probability of class 1 is 0
    #    class1_probs = np.zeros(proba.shape[0])
    
    #y_probs.append(class1_probs)

# Convert to (num_samples, num_labels)
#y_probs = np.array(y_probs).T

# Apply threshold
#threshold = 0.2
#y_pred_custom = (y_probs >= threshold).astype(int)

# Evaluate
#print(f"\n=== Classification Report (Threshold = {threshold}) ===")
#print(classification_report(y_test, y_pred_custom, target_names=mlb_next.classes_, zero_division=0))
# === Train and Evaluate ===

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize a Random Forest model for multi-label classification
model = MultiOutputClassifier(RandomForestClassifier(n_estimators=100, random_state=42))
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluation
print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=mlb_next.classes_))
import joblib
joblib.dump(model, 'course_preloader_model.pkl')
joblib.dump(mlb_completed, 'mlb_completed.pkl')         # for CompletedCourses
joblib.dump(mlb_categories, 'mlb_categories.pkl')   # for CompletedCategories
joblib.dump(mlb_next, 'mlb_next.pkl')               # for NextCourses

joblib.dump(semester_encoder, 'semester_encoder.pkl')
joblib.dump(year_encoded, 'year_encoder.pkl')
joblib.dump(popularity_encoded, 'pop_encoded.pkl')

print("Model saved as course_preloader_model.pkl")
from collections import Counter

# Flatten the list of all completed courses
all_courses = [
    course
    for course_list in students_df["CompletedCourses"]
    for course in (course_list if isinstance(course_list, list) else eval(course_list))
]

# Count frequency of each course
course_counts = Counter(all_courses)

# Normalize the counts
max_count = max(course_counts.values())
popularity_scores = {course: count / max_count for course, count in course_counts.items()}

# Save to pickle
joblib.dump(popularity_scores, "popularity_scores.pkl")
print("Saved popularity_scores.pkl")