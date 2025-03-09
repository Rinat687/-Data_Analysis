import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из CSV-файла

df = pd.read_csv('prices.csv')

# Вычисление средней цены
average_price = df['Price'].mean()

# Вывод результата
print(f"Средняя цена: {average_price:.2f} руб.")

file_path = 'prices.csv'  # Укажите путь к файлу
data = pd.read_csv(file_path)



# Построение гистограммы
plt.figure(figsize=(10, 6))  # Размер графика
plt.hist(data['Price'], bins=10, color='blue', edgecolor='black')  # Гистограмма
plt.title('Гистограмма цен на диваны и кресла')  # Заголовок
plt.xlabel('Цена (₽)')  # Подпись оси X
plt.ylabel('Количество предложений')  # Подпись оси Y
plt.grid(axis='y', alpha=0.75)  # Сетка

# Показать график
plt.show()