import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

# Give me random integers for plotting
random_X = np.random.randint(1,101,100)
random_Y = np.random.randint(1,101,100)

# Plotly takes all the inputs then plots
data = [go.Scatter(x=random_X,
                    y=random_Y,
                    mode='markers',
                    marker = dict(size=12 ,
                                    color='rgb(51,204,153)',
                                    symbol = 'pentagon'
                                    ,line={'width':2}
                                    ))]
layout = go.Layout(title='Hello First Plot',
                    xaxis = {'title':'MY X AXIS'},
                    yaxis = dict(title='MY Y AXIS'),
                    hovermode = 'closest')

fig = go.Figure(data = data,layout = layout)
pyo.plot(fig,filename='scatter.html')
