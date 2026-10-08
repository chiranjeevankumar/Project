import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Academic Details
degree = input("Enter Degree: ")
year_input = input("Enter Year of Study: ")
year_input = year_input.strip().lower()

if year_input.startswith("1"):
    year_of_study = 1
elif year_input.startswith("2"):
    year_of_study = 2
elif year_input.startswith("3"):
    year_of_study = 3
elif year_input.startswith("4"):
    year_of_study = 4
else:
    year_of_study = int(year_input)

department = input("Enter Department: ")
branch = input("Enter Branch: ")

if year_of_study == 1:
    year_text = "1st Year"
elif year_of_study == 2:
    year_text = "2nd Year"
elif year_of_study == 3:
    year_text = "3rd Year"
elif year_of_study == 4:
    year_text = "4th Year"
else:
    year_text = str(year_of_study) + "th Year"

degree = degree.strip().title()
department = department.strip()
branch = branch.strip().upper()

print("\nAcademic Details")
print("Degree:", degree)
print("Year of Study:", year_text)
print("Department:", department)
print("Branch:", branch)

# Number of Students
number_of_students = int(input("\nEnter number of students: "))

while number_of_students < 15 or number_of_students > 20:
    print("Please enter between 15 and 20 students.")
    number_of_students = int(input("Enter number of students: "))

# Sample Student Records
student_records = [
    {"Student_ID": "S001", "Name": "Rahul", "Attendance": 92, "Marks": [85, 90]},
    {"Student_ID": "S002", "Name": "Priya", "Attendance": 88, "Marks": [78, 82]},
    {"Student_ID": "S003", "Name": "Arjun", "Attendance": 95, "Marks": [92, 96]},
    {"Student_ID": "S004", "Name": "Sneha", "Attendance": 86, "Marks": [72, 75]},
    {"Student_ID": "S005", "Name": "Kiran", "Attendance": 90, "Marks": [88, 84]},
    {"Student_ID": "S006", "Name": "Anjali", "Attendance": 91, "Marks": [95, 91]},
    {"Student_ID": "S007", "Name": "Vijay", "Attendance": 80, "Marks": [65, 70]},
    {"Student_ID": "S008", "Name": "Neha", "Attendance": 94, "Marks": [89, 93]},
    {"Student_ID": "S009", "Name": "Ravi", "Attendance": 85, "Marks": [55, 62]},
    {"Student_ID": "S010", "Name": "Pooja", "Attendance": 97, "Marks": [96, 98]},
    {"Student_ID": "S011", "Name": "Akhil", "Attendance": 89, "Marks": [82, 86]},
    {"Student_ID": "S012", "Name": "Divya", "Attendance": 93, "Marks": [90, 88]},
    {"Student_ID": "S013", "Name": "Manoj", "Attendance": 84, "Marks": [74, 79]},
    {"Student_ID": "S014", "Name": "Kavya", "Attendance": 96, "Marks": [91, 94]},
    {"Student_ID": "S015", "Name": "Suresh", "Attendance": 87, "Marks": [68, 73]}
]

subjects = ["Python", "Data Analysis"]

# Create DataFrame
records = []

for student in student_records:
    record = {
        "Student_ID": student["Student_ID"],
        "Name": student["Name"],
        "Degree": degree,
        "Year_of_Study": year_text,
        "Department": department,
        "Branch": branch,
        "Attendance": student["Attendance"]
    }

    for i in range(len(subjects)):
        record[subjects[i]] = student["Marks"][i]

    records.append(record)

df = pd.DataFrame(records)

# Calculate Total Marks
total_marks = []

for i in range(len(df)):
    marks = []

    for subject in subjects:
        marks.append(df.loc[i, subject])

    total = np.sum(marks)
    total_marks.append(total)

df["Total_Marks"] = total_marks

# Calculate Average Marks
average_marks = []

for i in range(len(df)):
    average = df.loc[i, "Total_Marks"] / len(subjects)
    average_marks.append(average)

df["Average_Marks"] = average_marks

# Grade Function
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

grades = []

for i in range(len(df)):
    grades.append(calculate_grade(df.loc[i, "Average_Marks"]))

df["Grade"] = grades

# Pass/Fail Function
def check_result(marks, average):
    for mark in marks:
        if mark < 35:
            return "Fail"

    if average >= 40:
        return "Pass"
    else:
        return "Fail"

results = []

for i in range(len(df)):
    marks = []

    for subject in subjects:
        marks.append(df.loc[i, subject])

    results.append(check_result(marks, df.loc[i, "Average_Marks"]))

df["Result"] = results

# Display Student Data
print("\nStudent Performance")
print(df)

# Class Performance
highest_average = df["Average_Marks"].max()
lowest_average = df["Average_Marks"].min()
class_average = df["Average_Marks"].mean()

print("\nClass Performance")
print("Highest Average:", highest_average)
print("Lowest Average:", lowest_average)
print("Class Average:", class_average)

# Subject-wise Performance
print("\nSubject-wise Performance")

for subject in subjects:
    print("\nSubject:", subject)
    print("Highest Marks:", df[subject].max())
    print("Lowest Marks:", df[subject].min())
    print("Average Marks:", df[subject].mean())

# Top 3 Students
top_students = df.sort_values(by="Average_Marks", ascending=False)

print("\nTop 3 Students")
print(top_students[["Student_ID", "Name", "Average_Marks", "Grade"]].head(3))

# Attendance Analysis
print("\nAttendance Analysis")
print("Highest Attendance:", df["Attendance"].max())
print("Lowest Attendance:", df["Attendance"].min())
print("Average Attendance:", df["Attendance"].mean())

# Grade Count
grade_counts = df["Grade"].value_counts()

print("\nGrade-wise Student Count")

for grade in ["A", "B", "C", "D", "F"]:
    print("Grade", grade + ":", grade_counts.get(grade, 0))

# Pass/Fail Count
result_counts = df["Result"].value_counts()

print("\nPass/Fail Summary")
print("Pass:", result_counts.get("Pass", 0))
print("Fail:", result_counts.get("Fail", 0))

# Save Data
df.to_csv("students.csv", index=False)

print("\nStudent performance data saved successfully.")

# Student Search
search_id = input("\nEnter Student ID to search: ")

found = False

for i in range(len(df)):
    if df.loc[i, "Student_ID"] == search_id:
        print("\nStudent Found")
        print("Student ID:", df.loc[i, "Student_ID"])
        print("Name:", df.loc[i, "Name"])
        print("Attendance:", df.loc[i, "Attendance"])
        print("Python:", df.loc[i, "Python"])
        print("Data Analysis:", df.loc[i, "Data Analysis"])
        print("Total Marks:", df.loc[i, "Total_Marks"])
        print("Average Marks:", df.loc[i, "Average_Marks"])
        print("Grade:", df.loc[i, "Grade"])
        print("Result:", df.loc[i, "Result"])

        found = True
        break

if found == False:
    print("\nStudent ID not found.")

# Grade Distribution Chart
grades = ["A", "B", "C", "D", "F"]
counts = []

for grade in grades:
    counts.append(grade_counts.get(grade, 0))

plt.bar(grades, counts)
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.show()

# Subject Average Chart
subject_averages = []

for subject in subjects:
    subject_averages.append(df[subject].mean())

plt.bar(subjects, subject_averages)
plt.title("Subject-wise Average Marks")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.show()
