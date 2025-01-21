import pandas as pd
import plotly.graph_objs as go
arr = [(-11475), (-18548), (-12027), (-8809), (-9494)]
data = {"year":['2020', '2021','2022','2023','2024'],
        "Prirost":[-11475, -18548, -12027, -8809, -9494]}
data = pd.DataFrame(data=data)
fig = go.Figure(data=[go.Bar(x = data["year"], y = data["Prirost"])])
fig.show()