import pandas as pd
import numpy as np

def calculate_final_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def check_final_result(marks):
    average = np.mean(marks)

    for mark in marks:
        if mark < 35:
            return 'Fail'

    if average >= 40:
        return 'Pass'
    else:
        return 'Fail'

student_data = pd.read_csv('students.csv')

subjects = ['Ghh', 'Hhj']

total_marks = []
average_marks = []

for i in range(len(student_data)):
    marks = []

    for subject in subjects:
        marks.append(student_data.loc[i, subject])

    total = np.sum(marks)
    average = total / len(subjects)

    total_marks.append(total)
    average_marks.append(average)

student_data['Total_Marks'] = total_marks
student_data['Average_Marks'] = average_marks

grades = []

for i in range(len(student_data)):
    grade = calculate_final_grade(student_data.loc[i, 'Average_Marks'])
    grades.append(grade)

student_data['Grade'] = grades

results = []

for i in range(len(student_data)):
    marks = []

    for subject in subjects:
        marks.append(student_data.loc[i, subject])

    result = check_final_result(marks)
    results.append(result)

student_data['Result'] = results

print('\nFinal Student Performance Report')
print(student_data)

class_average = np.mean(student_data['Average_Marks'])
highest_average = np.max(student_data['Average_Marks'])
lowest_average = np.min(student_data['Average_Marks'])

print('\nClass Performance')
print('Class Average:', class_average)
print('Highest Average:', highest_average)
print('Lowest Average:', lowest_average)

print('\nSubject-wise Performance')

for subject in subjects:
    subject_average = np.mean(student_data[subject])
    subject_highest = np.max(student_data[subject])
    subject_lowest = np.min(student_data[subject])

    print('\nSubject:', subject)
    print('Average Marks:', subject_average)
    print('Highest Marks:', subject_highest)
    print('Lowest Marks:', subject_lowest)

top_students = student_data.sort_values(by='Average_Marks', ascending=False).head(3)

print('\nTop 3 Performing Students')
print(top_students[['Student_ID', 'Name', 'Branch', 'Average_Marks', 'Grade', 'Result']])

pass_count = 0
fail_count = 0

for result in student_data['Result']:
    if result == 'Pass':
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

total_students = len(student_data)
pass_percentage = (pass_count / total_students) * 100
fail_percentage = (fail_count / total_students) * 100

print('\nPass/Fail Statistics')
print('Total Students:', total_students)
print('Passed Students:', pass_count)
print('Failed Students:', fail_count)
print('Pass Percentage:', pass_percentage)
print('Fail Percentage:', fail_percentage)

attendance_average = np.mean(student_data['Attendance'])
highest_attendance = np.max(student_data['Attendance'])
lowest_attendance = np.min(student_data['Attendance'])

print('\nAttendance Analysis')
print('Average Attendance:', attendance_average)
print('Highest Attendance:', highest_attendance)
print('Lowest Attendance:', lowest_attendance)