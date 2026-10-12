
import numpy as np
import pandas as pd

print(" STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# User inputs
degree = input("Enter Degree: ")

year_input = input("Enter Year of Study: ")

if year_input.strip().lower() in ["2", "2nd", "2nd year"]:
    year = "2nd Year"
else:
    year = year_input.strip().title()

department = input("Enter Department: ")
branch = input("Enter Branch: ")

number_of_students = int(input("Enter Number of Students: "))

# Subjects
subjects = ["Python", "Java", "JavaScript", "AI/ML", "C"]

# Student records
student_records = [
    ["S001", "Chiru", 92, 85, 82, 88, 90, 84],
    ["S002", "Tarun", 88, 78, 81, 85, 79, 76],
    ["S003", "Vijay", 95, 92, 94, 96, 91, 93],
    ["S004", "Pavan", 86, 72, 75, 78, 80, 74],
    ["S005", "Gulshan", 90, 88, 84, 86, 89, 87],
    ["S006", "Ajay", 91, 95, 92, 94, 96, 93],
    ["S007", "Madav", 80, 65, 68, 72, 70, 66],
    ["S008", "Chandan", 94, 89, 93, 91, 95, 90],
    ["S009", "Manoj", 85, 55, 62, 58, 60, 57],
    ["S010", "Ayyappa", 97, 96, 98, 97, 99, 95],
    ["S011", "Satish", 89, 82, 86, 84, 81, 85],
    ["S012", "Charan", 93, 90, 88, 91, 89, 92],
    ["S013", "Anjan", 84, 74, 79, 76, 72, 78],
    ["S014", "Hasini", 96, 91, 94, 93, 92, 96],
    ["S015", "Yaswanth", 87, 68, 73, 70, 75, 71],
    ["S016", "Vikas", 90, 86, 88, 85, 87, 89],
    ["S017", "Vesilee", 92, 84, 90, 88, 91, 86],
    ["S018", "Narayana", 83, 70, 72, 75, 78, 73],
    ["S019", "Vijaya", 95, 93, 91, 94, 96, 92],
    ["S020", "Siva", 88, 77, 80, 83, 85, 79],
    ["S021", "Kumar", 91, 87, 85, 89, 90, 88],
    ["S022", "Varshika", 94, 90, 92, 95, 93, 91]
]

# Limit records according to user input
student_records = student_records[:number_of_students]

# DataFrame columns
columns = [
    "Student_ID",
    "Name",
    "Degree",
    "Year_of_Study",
    "Department",
    "Branch",
    "Python",
    "Java",
    "JavaScript",
    "AI/ML",
    "C",
    "Total_Marks",
    "Average_Marks",
    "Grade",
    "Result",
    "Attendance"
]

data = []

# Create rows
for record in student_records:

    student_id = record[0]
    name = record[1]
    attendance = record[2]
    marks = record[3:]

    total = np.sum(marks)
    average = total / len(subjects)

    row = [
        student_id,
        name,
        degree,
        year,
        department,
        branch
    ]

    # Add subject marks
    for mark in marks:
        row.append(mark)

    # Add total and average
    row.append(total)
    row.append(average)

    # Temporary grade and result
    row.append("")
    row.append("")

    # Attendance as last column
    row.append(attendance)

    data.append(row)

# Create DataFrame
new_df = pd.DataFrame(data, columns=columns)


# Grade function
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


# Result function
def calculate_result(grade, average):

    if average >= 40 and grade != "F":
        return "Pass"

    else:
        return "Fail"


# Calculate grade and result
for i in range(len(new_df)):

    average = new_df.loc[i, "Average_Marks"]

    grade = calculate_grade(average)
    result = calculate_result(grade, average)

    new_df.loc[i, "Grade"] = grade
    new_df.loc[i, "Result"] = result


# Save dataset
new_df.to_csv("students.csv", index=False)


# Display dataset
print("\nDataset Created Successfully")
print("                               ")
print("Number of Students:", len(new_df))
print("Number of Subjects:", len(subjects))

print("\nStudent Performance Data")
print("                           ")
print(new_df.to_string(index=False))


# Overall performance
print("\nOverall Performance")
print("                      ")

class_average = new_df["Average_Marks"].mean()
average_attendance = new_df["Attendance"].mean()

print("Class Average Marks:", round(class_average, 2))
print("Average Attendance:", round(average_attendance, 2), "%")


# Result summary
passed_students = len(new_df[new_df["Result"] == "Pass"])
failed_students = len(new_df[new_df["Result"] == "Fail"])

print("\nResult Summary")
print("                 ")
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)


# Subject-wise averages
print("\nSubject-wise Average Marks")
print("                             ")

for subject in subjects:

    average = new_df[subject].mean()

    print(subject, ":", round(average, 2))


# Top 3 students
print("\nTop 3 Students")
print("                 ")

top_students = new_df.sort_values(
    by="Average_Marks",
    ascending=False
).head(3)

print(
    top_students[
        ["Student_ID", "Name", "Average_Marks", "Grade", "Result"]
    ].to_string(index=False)
)


# Grade distribution
print("\nGrade Distribution")
print("                      ")

grade_order = ["A", "B", "C", "D", "F"]

for grade in grade_order:

    count = len(new_df[new_df["Grade"] == grade])

    print(grade, ":", count)


# Student search
print("\nStudent Search")
print("                  ")

search_id = input("Enter Student ID to search: ")

student = new_df[new_df["Student_ID"] == search_id]

if len(student) > 0:

    print("\nStudent Found")
    print("                 ")
    print(student.to_string(index=False))

else:

    print("\nStudent ID not found.")


print("\n...........................................")
print(" Project execution completed successfully.")
print(".............................................")
