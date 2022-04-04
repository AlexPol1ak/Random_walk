from random_points import RandomPoints
import plotly.graph_objects as go
from plotly import offline

my_points = RandomPoints(10000)
my_points.random_walk()
x = my_points.return_list_walk('x')
y = my_points.return_list_walk('y')
color = list(range(10000))

scatter = go.Scatter(x=x, y=y, mode='markers', name='Random Walk 10000 points',marker=dict(
	color=color,size=7,colorscale='Blues',showscale=True))
fig = go.Figure(data=scatter)
fig.update_layout(yaxis_range=[-1, 1])
offline.plot({'data': scatter}, filename='Random Walk 10000 points.html') 
