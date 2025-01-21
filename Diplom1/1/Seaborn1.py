import seaborn as sns
import matplotlib.pyplot as plt
vals = [37, 26, 11, 21, 5]
labels = ["Аренда земли", "Остальные неналоговые доходы", "Продажа земли", "Аренда имущества", "Продажа имущества"]
sns.set_style("whitegrid")
plt.pie(vals, labels=labels)
plt.show()