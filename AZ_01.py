import pandas as pd

# data = [1, 2, 3, 4, 5]
# series = pd.Series(data)
# print(series)

data = {
    'Name': ['Alice', 'Bob', 'Roma', 'Anna'],
    'Age': [23, 45, 17, 24],
    'City': ['New York', 'LA', 'Chicago', 'Moscow']
}
# сохранение в файл
df = pd.DataFrame(data)
df.to_csv('test.csv', index=False)


# просмотр данных
df = pd.read_csv('Refugee_Asylum_data.csv')
print(df.head())

print(df.info())

print(df.describe())

print(df.loc[5])

# редоктирование данных
#добовление столбца
df = pd.read_csv('hh.csv')
df['Test'] = [new for new in range(39)]
print(df)

#удаление столбца
df.drop('Test', axis=1, inplace=True)
print(df)

#удаление строки
df.drop(38, axis=0, inplace=True)
print(df)