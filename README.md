
# Student Performance Analytics System

## Project Overview

The Student Performance Analytics System is a Python-based data analysis project developed as part of the EWB Courses | Python with AI project guidelines.

The system manages student academic performance data and uses Python, NumPy, and Pandas to calculate marks, averages, grades, results, attendance statistics, subject-wise performance, and top-performing students.

The project is designed using Python fundamentals such as variables, data types, loops, functions, conditional statements, NumPy calculations, and Pandas DataFrame operations.

---

## Student Details

- Degree: B.Tech
- Year of Study: 2nd Year
- Department: Computer Science and Engineering
- Branch: CSE

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Google Colab
- GitHub

---

## Subjects

The project contains performance data for five subjects:

1. Python
2. Java
3. JavaScript
4. AI/ML
5. C

---

## Dataset

The dataset contains 22 student records.

Each student record contains:

- Student ID
- Name
- Degree
- Year of Study
- Department
- Branch
- Python marks
- Java marks
- JavaScript marks
- AI/ML marks
- C marks
- Total Marks
- Average Marks
- Grade
- Result
- Attendance

The dataset is stored in:

`students.csv`

---

## Grade Rules

Grades are calculated using the student's average marks.

| Average Marks | Grade |
|---|---|
| 90 and above | A |
| 80 - 89 | B |
| 70 - 79 | C |
| 60 - 69 | D |
| Below 60 | F |

---

## Pass / Fail Rule

A student is marked **Pass** when:

- Average marks are 40 or above
- Grade is not F

Otherwise, the student is marked **Fail**.

---

## Main Features

### 1. Student Data Management

The program stores student details, subject marks, and attendance.

### 2. Total Marks

The system calculates the total marks obtained across all five subjects.

### 3. Average Marks

The system calculates the average marks of each student.

### 4. Grade Calculation

The system assigns grades from A to F based on average marks.

### 5. Pass / Fail Analysis

The system determines whether each student has passed or failed.

### 6. Overall Performance

The system calculates:

- Class average marks
- Average attendance
- Number of passed students
- Number of failed students

### 7. Subject-wise Performance

The system calculates the average marks for each subject.

### 8. Top Performing Students

The system displays the top three students according to average marks.

### 9. Grade Distribution

The system counts the number of students in each grade category.

### 10. Student Search

The user can enter a Student ID and view that student's complete performance details.

---

## NumPy Usage

NumPy is used for numerical calculations.

For example, the total marks of a student are calculated using:

`np.sum(marks)`

---

## Pandas Usage

Pandas is used to:

- Create the DataFrame
- Store student records
- Calculate statistics
- Filter students
- Sort students
- Save the final dataset as a CSV file
- Read the saved CSV file

---

## Project Output

The final dataset contains:

- 22 students
- 5 subjects
- 16 columns

### Overall Results

- Class Average Marks: **83.95**
- Average Attendance: **90.0%**
- Passed Students: **21**
- Failed Students: **1**

### Top 3 Students

1. Ayyappa — 97.0
2. Ajay — 94.0
3. Hasini — 93.2

### Subject-wise Average

| Subject | Average Marks |
|---|---:|
| Python | 82.14 |
| Java | 83.95 |
| JavaScript | 84.91 |
| AI/ML | 85.36 |
| C | 83.41 |

### Grade Distribution

| Grade | Students |
|---|---:|
| A | 8 |
| B | 7 |
| C | 5 |
| D | 1 |
| F | 1 |

---

## Visualizations

The project includes two charts:

- Grade Distribution
- Subject-wise Average Marks

The charts are stored in the `screenshots` folder.

---

## Project Files

```text
Project/
│
├── main.py
├── students.csv
├── README.md
├── Project_Documentation.md
│
└── screenshots/
    ├── grade_distribution.png
    └── subject_average.png
