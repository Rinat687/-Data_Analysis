import pandas as pd

df = pd.read_csv('dz.csv')
# просматриваем данные
print(df)

# удаляем строки с пропущенными значениями
df.dropna(inplace=True)
print(df)

# группировка данных и вывод средней зарплаты по городу
grouped = df.groupby('City')
print(grouped['Salary'].mean())