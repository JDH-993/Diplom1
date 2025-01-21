import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
arr = [(-11475), (-18548), (-12027), (-8809), (-9494)]
data = {"year":['2020', '2021','2022','2023','2024'],
        "Prirost":[-11475, -18548, -12027, -8809, -9494]}
data = pd.DataFrame(data=data)
sns.barplot(x = 'year', y = 'Prirost',data=data)
plt.show()