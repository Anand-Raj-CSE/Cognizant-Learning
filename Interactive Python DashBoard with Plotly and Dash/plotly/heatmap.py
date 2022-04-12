from matplotlib.pyplot import title
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go

df = pd.read_csv('Data/2010SantaBarbaraCA.csv')

print(df.head())

# z always take a list in python not a dataframe column
data = [go.Heatmap(x=df['DAY'],y=df['LST_TIME'],z=df['T_HR_AVG'].values.tolist())]

layout = go.Layout(title='SB CA Temps')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Heatmap.html')