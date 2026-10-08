# Student Performance Analytics System - Project Documentation

## 1. Project Title and Student Details

Project Title: Student Performance Analytics System
Student Name: Chiranjeevankumar Raavi

## 2. Objective

The objective of this project is to build a Python-based Student Performance Analytics System.
The system organizes student academic data and analyzes marks and attendance.
It calculates total marks, average marks, grades, pass/fail status, subject-wise performance, attendance statistics, and top-performing students.

## 3. Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Google Colab
- GitHub

## 4. Dataset Description

The project uses a dataset containing 15 student records.
The common academic details are B.Tech, 2nd Year, Computer Science and Engineering, and CSE.

The dataset contains the following fields:

- Student ID
- Name
- Degree
- Year of Study
- Department
- Branch
- Attendance
- Python marks
- Data Analysis marks
- Total Marks
- Average Marks
- Grade
- Result

The student records contain realistic marks and attendance values.

## 5. Implementation

### Step 1 - Academic Details

The program accepts the degree, year of study, department, and branch from the user.
The year input can be entered as a number or in a format such as 2nd year.

### Step 2 - Prepare Student Data

The project contains 15 student records with student IDs, names, attendance, and marks for Python and Data Analysis.

### Step 3 - Create Pandas DataFrame

The student records are organized into a Pandas DataFrame.
The DataFrame makes it easier to process and analyze the student data.

### Step 4 - Calculate Total Marks

A loop collects the subject marks for each student.
NumPy is used with np.sum() to calculate the total marks.

### Step 5 - Calculate Average Marks

The average marks are calculated by dividing the total marks by the number of subjects.

### Step 6 - Calculate Grades

A reusable function named calculate_grade() assigns grades based on average marks.

The grading rules are:

- 90 and above: A
- 80 to 89: B
- 70 to 79: C
- 60 to 69: D
- Below 60: F

### Step 7 - Determine Pass or Fail

A reusable function named check_result() checks each subject mark and the average.
A student passes when every subject mark is at least 35 and the average is at least 40.

### Step 8 - Perform Data Analysis

Pandas operations are used to find the highest, lowest, and average performance.
Subject-wise performance is also calculated.
The students are sorted by average marks to identify the top-performing students.

### Step 9 - Attendance Analysis

The project calculates the highest attendance, lowest attendance, and average attendance.

### Step 10 - Student Search

The program accepts a Student ID and searches the DataFrame using a loop.
If the Student ID exists, the student's details and performance are displayed.
If the ID does not exist, the program displays a Student ID not found message.

### Step 11 - Save the Dataset

The final DataFrame is saved as students.csv using Pandas to_csv().

### Step 12 - Data Visualization

Matplotlib is used to display a grade distribution chart and a subject-wise average marks chart.

## 6. Key Features

- User input for academic details
- Student dataset management
- Pandas DataFrame
- NumPy numerical calculations
- Reusable functions
- Loops and conditions
- Total marks calculation
- Average marks calculation
- Grade calculation
- Pass/Fail analysis
- Class performance analysis
- Subject-wise performance analysis
- Top 3 student identification
- Attendance analysis
- Grade distribution
- Student ID search
- CSV file creation
- Basic data visualization

## 7. Output and Screenshots

The final program successfully produced the following results:

- Total students: 15
- Class average: 82.7
- Average attendance: 89.8%
- Pass students: 15
- Fail students: 0
- Highest performer: Pooja with an average of 97.0
- Lowest performer: Ravi with an average of 58.5
- Python subject average: 81.33
- Data Analysis subject average: 84.07

The project also generates:

1. Grade Distribution chart
2. Subject-wise Average Marks chart

Screenshots of the important outputs and charts should be added to the project repository.

## 8. Final Outcome

The Student Performance Analytics System successfully processes and analyzes student academic data.
It provides useful information about individual students, class performance, subject performance, attendance, grades, and top performers.
The final dataset is stored in students.csv and the complete program is available in main.py.

## 9. Challenges and Learning

One challenge was organizing the student information and calculated results into a single DataFrame.
Another challenge was handling user input for the year of study in different formats.
The project was tested and the input handling was corrected so that values such as 2 and 2nd year can be accepted.

Through this project, I learned how to use Python loops, conditions, functions, NumPy calculations, Pandas DataFrames, CSV files, and basic data visualization.
I also learned how to test a Python project and maintain the project files using Git and GitHub.

## 10. GitHub Repository

GitHub Repository:
https://github.com/chiranjeevankumar/Project

The repository contains the main Python program, student dataset, README file, and project documentation.

## Conclusion

This project demonstrates the practical use of Python, NumPy, Pandas, and basic visualization for student performance analysis.
The project meets the main requirements of the Python with AI project guidelines.