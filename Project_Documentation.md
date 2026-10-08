
# Student Performance Analytics System

## 1. Project Title and Student Details

### Project Title

**Student Performance Analytics System**

### Student Details

- Degree: B.Tech
- Year of Study: 2nd Year
- Department: Computer Science and Engineering
- Branch: CSE

---

## 2. Objective

The objective of this project is to develop a Python-based Student Performance Analytics System that can store, process, and analyze student academic performance data.

The system uses Python, NumPy, and Pandas to calculate total marks, average marks, grades, pass/fail results, attendance statistics, subject-wise performance, and top-performing students.

The project demonstrates the practical use of Python programming and basic data analysis concepts.

---

## 3. Technologies Used

The following technologies and concepts were used:

- Python
- NumPy
- Pandas
- Matplotlib
- Google Colab
- GitHub

### Python Concepts Used

- Variables
- Data types
- Lists
- Conditional statements
- Loops
- Functions
- User input
- File handling

### Data Analysis Concepts Used

- Pandas DataFrame
- Numerical calculations
- Filtering
- Sorting
- Mean calculation
- CSV file handling
- Basic visualization

---

## 4. Dataset Description

The project contains data for **22 students**.

The dataset includes five subjects:

1. Python
2. Java
3. JavaScript
4. AI/ML
5. C

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

The final dataset contains:

- **22 records**
- **16 columns**
- **0 missing values**

The dataset is stored in the file:

`students.csv`

---

## 5. Implementation

### 5.1 User Input

The program accepts the following information from the user:

- Degree
- Year of Study
- Department
- Branch
- Number of Students

The year input is standardized so that values such as `2`, `2nd`, or `2nd year` are stored as:

`2nd Year`

---

### 5.2 Student Data

The program stores student ID, name, attendance, and marks for five subjects.

The five subjects are:

- Python
- Java
- JavaScript
- AI/ML
- C

---

### 5.3 Pandas DataFrame

The student records are organized into a Pandas DataFrame.

The DataFrame contains 16 columns:

```text
Student_ID
Name
Degree
Year_of_Study
Department
Branch
Python
Java
JavaScript
AI/ML
C
Total_Marks
Average_Marks
Grade
Result
Attendance
