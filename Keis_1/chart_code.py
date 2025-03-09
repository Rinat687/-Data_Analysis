import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из CSV-файла
file_path = 'prices_processed.csv'  # Укажите путь к файлу
data = pd.read_csv(file_path)

# Построение гистограммы
plt.figure(figsize=(10, 6))  # Размер графика
plt.hist(data['Price'], bins=10, color='blue', edgecolor='black')  # Гистограмма
plt.title('Гистограмма цен на аренду квартир')  # Заголовок
plt.xlabel('Цена (₽)')  # Подпись оси X
plt.ylabel('Количество предложений')  # Подпись оси Y
plt.grid(axis='y', alpha=0.75)  # Сетка

# Показать график
plt.show()