import pandas as pd

def create_grader(branch, passing_grade):
    def evaluate(grade):
        if grade >= passing_grade:
            return f"Passed ({branch})"
        else:
            return f"Failed ({branch})"
    return evaluate
lima_grader = create_grader("Lima Branch", 11)
vip_grader = create_grader("VIP Branch", 14)
data = {
    "Student": ['Elizabeth', 'Luis', 'Brenda', 'Marco', 'Lily'],
    "Grade": [12, 10, 15, 18, 20]
}
df = pd.DataFrame(data)
df['Lima_Result'] = df['Grade'].apply(lima_grader)
df['VIP_Result'] = df['Grade'].apply(vip_grader)
print(df)

df.to_excel("Multi_Branch_Report.xlsx", index=False)
