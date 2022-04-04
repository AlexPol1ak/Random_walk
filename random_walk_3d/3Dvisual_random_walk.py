from random_walk_3d import RandomPoints3D
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly import offline
import numpy as np


my_points = RandomPoints3D(5000)
my_points.random_walk()
#my_points.write_data()

x =  my_points.list_value('x')
y =  my_points.list_value('y')
z =  my_points.list_value('z')


fig = make_subplots(
    rows=2, cols=2,
    specs=[[None, None],
           [{"type": "scene"}, {"type": "scatter3d"}]], start_cell='bottom-left')
fig.add_trace(go.Scatter3d(x=x, y=y,
                           z=z, mode='lines'),
              row=2, col=2)

fig.update_layout(autosize = True, width=1500, height=1500, showlegend=False, template="plotly_dark",)

#paper_bgcolor="darkgray"
offline.plot({'data': fig}, filename='R.html') 
#fig.show()