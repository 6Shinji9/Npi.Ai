import matplotlib.pyplot as plt
import numpy as np

# Данные для графика
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Построение графика
plt.plot(x, y)
plt.title("График функции y = sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
