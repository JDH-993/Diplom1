import pandas as pd
import plotly.express as px
data = {'Баллы по математике': [100, 100, 98, 98, 92, 92, 90, 90, 88, 88, 88, 88, 86, 82, 80, 80, 80, 80, 80, 76, 76, 48, 48, 52, 58, 58, 58, 58, 64, 64, 68, 34, 6, 6, 11, 22, 27, 27, 34, 0],
        "Номер ученика":[1, 2, 3, 4,5 ,6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]}
df = pd.DataFrame(data=data)
fig = px.scatter(df, x='Баллы по математике', y = 'Номер ученика')
fig.show()