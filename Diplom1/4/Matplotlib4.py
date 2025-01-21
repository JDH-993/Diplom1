import pandas as pd
import matplotlib.pyplot as plt
data = {"year":['2020', '2021','2022','2023','2024'],"Prirost":[-11475, -18548, -12027, -8809, -9494]}
fig = plt.figure(figsize=(6, 4))
data = pd.DataFrame(data=data)
ax = fig.add_subplot()
ax.bar(data["year"],data["Prirost"])
plt.show()