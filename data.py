import pandas as pd
import csv 
import plotly.express as px

df=pd.read_csv("data.csv")
result=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
print(result)
fig=px.scatter(
    result,
    x="student_id",
    y="level",
    size="attempt",
    color="attempt"
)
fig.show()