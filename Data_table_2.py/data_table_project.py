import pandas as pd

def evaluate_grade(grade):
    if grade >= 11:
        return "Passed"
    else: 
        return "Failed"

subjects = ["Math", "Programming", "English", "Physics"]
grades = [18, 20, 10, 15]
final_status = [evaluate_grade(g) for g in grades]
data = {
    "Course" : subjects,
    "Grade" : grades,
    "Status" : final_status
}

df = pd.DataFrame(data)

df.to_excel("Final_report.xlsx", index=False)

print("Report generated successfully! Check your folder.")
print(df)
