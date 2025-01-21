import plotly.graph_objs as go
vals = [37, 26, 11, 21, 5]
labels = ["Аренда земли", "Остальные неналоговые доходы", "Продажа земли", "Аренда имущества", "Продажа имущества"]
fig = go.Figure()
fig.add_trace(go.Pie(values=vals, labels=labels))
fig.show()