import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Performance Analytics System")
st.write(
    "An interactive dashboard for analyzing student marks, "
    "grades, attendance, and academic performance."
)

data_file = Path(__file__).parent / "students.csv"

if not data_file.exists():
    st.error("students.csv was not found in the project repository.")
    st.stop()

df = pd.read_csv(data_file)

subjects = ["Python", "Java", "JavaScript", "AI/ML", "C"]

if not all(subject in df.columns for subject in subjects):
    st.error("The dataset is missing one or more subject columns.")
    st.stop()

# Calculate metrics from the dataset
df["Total_Marks"] = df[subjects].sum(axis=1)
df["Average_Marks"] = df[subjects].mean(axis=1)

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    return "F"

df["Grade"] = df["Average_Marks"].apply(calculate_grade)
df["Result"] = np.where(
    (df["Average_Marks"] >= 40) & (df["Grade"] != "F"),
    "Pass",
    "Fail"
)

st.subheader("📊 Class Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", len(df))
col2.metric("Class Average", f"{df['Average_Marks'].mean():.2f}")
col3.metric("Passed", int((df["Result"] == "Pass").sum()))
col4.metric("Failed", int((df["Result"] == "Fail").sum()))

st.divider()

st.subheader("🔎 Search Students")
search = st.text_input("Search by student name or ID")

filtered_df = df.copy()

if search:
    filtered_df = df[
        df["Name"].astype(str).str.contains(search, case=False, na=False)
        | df["Student_ID"].astype(str).str.contains(
            search, case=False, na=False
        )
    ]

st.subheader("👩‍🎓 Student Records")
st.dataframe(filtered_df, use_container_width=True, hide_index=True)

st.download_button(
    "Download Student Results CSV",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="student_results.csv",
    mime="text/csv"
)

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("📚 Average by Subject")
    subject_averages = df[subjects].mean().round(2)
    st.bar_chart(subject_averages)

with right:
    st.subheader("🏅 Grade Distribution")
    grade_counts = (
        df["Grade"]
        .value_counts()
        .reindex(["A", "B", "C", "D", "F"], fill_value=0)
    )
    st.bar_chart(grade_counts)

st.subheader("🏆 Top 3 Performers")
top_students = df.nlargest(3, "Average_Marks")

st.dataframe(
    top_students[
        ["Student_ID", "Name", "Total_Marks", "Average_Marks", "Grade", "Result"]
    ],
    use_container_width=True,
    hide_index=True
)

st.caption("Built with Python, Streamlit, NumPy, and Pandas.")
