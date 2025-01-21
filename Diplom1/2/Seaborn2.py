import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0, 10, 100)
sns.lineplot(x=np.linspace(0, 10, 100),y=[float(i**2) for i in x])
plt.show()