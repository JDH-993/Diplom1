import numpy as np
import pandas as pd
import plotly.graph_objs as go
arr = np.array([[3, 5, 5, 5],
                [3, 5, 4, 3],
                [3, 4, 5, 5],
                [4, 4 ,3, 3],
                [4, 4, 3, 3],
                [4, 4, 3, 4],
                [5, 4, 3, 4],
                [5, 3, 4, 4],
                [5, 3, 4, 4],
                [5, 3, 4, 4]])

df = pd.DataFrame(arr, columns=['Русский язык', 'Математика', 'Английский', 'Обществознание'])
fig = go.Figure()
fig.add_trace(go.Box(y=df['Русский язык']))
fig.add_trace(go.Box(y=df['Математика']))
fig.add_trace(go.Box(y=df['Английский']))
fig.add_trace(go.Box(y=df['Обществознание']))
fig.show()