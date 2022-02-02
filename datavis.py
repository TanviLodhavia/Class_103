from numpy import size
import pandas as pd
import plotly.express as px

#LINE
#storing file in df variable
df = pd.read_csv("line_chart.csv")
#displaying chart
fig = px.line(df, x="Year", y="Per capita income", color="Country", title="Per Capita Income")
fig.show()

#BAR
#reading csv file
df = pd.read_csv("data.csv")
fig=px.bar(df, x="Country", y="InternetUsers")
fig.show()

#SCATTER
df=pd.read_csv("data.csv")
fig=px.scatter(df, x="Population", y="Per capita", size="Percentage", color="Country", size_max=60)
fig.show()