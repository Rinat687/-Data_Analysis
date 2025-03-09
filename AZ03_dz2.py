import matplotlib.pyplot as plt
import numpy as np


x = np.random.rand(5)  # массив координаты х из 5 случайных чисел
y = np.random.rand(5)  # массив координаты у из 5 случайных чисел

plt.title('Диаграмма рассеяния \n для двух наборов случайных данных')
plt.xlabel('Ось Х')
plt.ylabel('Ось Y')
plt.scatter(x,y)    # Диаграмма рассеивания
plt.show()