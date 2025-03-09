import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)

plt.hist(data,bins = 100)
plt.title('Гистограмма случайных чисел,\n распределенных по нормальному распределению')
plt.xlabel('Диапазон')
plt.ylabel('Количество совпадений')
plt.grid(True)  # Включение сетки для конкретных осей
plt.show()
