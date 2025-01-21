import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
sns.boxplot(df)
plt.show()