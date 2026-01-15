import pandas as pd


data = {
    'Course': ['Math', 'Programming', 'English', 'Physics'],
    'Grade': [18, 20, 17, 15],
    'Status': ['Passed', 'Passed', 'Passed', 'Passed']
}

df = pd.DataFrame(data)

print("My first Data Table:")
print(df)

df.to_excel('grades.xlsx', index=False)
