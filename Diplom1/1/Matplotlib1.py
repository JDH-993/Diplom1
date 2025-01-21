import matplotlib.pyplot as plt
vals = [37, 26, 11, 21, 5]
labels = ["Аренда земли", "Остальные неналоговые доходы", "Продажа земли", "Аренда имущества", "Продажа имущества"]
fig, ax = plt.subplots()
ax.pie(vals, labels=labels)
plt.show()