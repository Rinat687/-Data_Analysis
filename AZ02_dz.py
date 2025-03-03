import pandas as pd
import matplotlib.pyplot as plt
#  создаем датофрейм
data = {
    'name' : ['Андрей','Василий','Михаил','Евгений','Олег','Марина','Анжела','Светлана','Екатерина','Анна'],
    'Mathematics' : [3,4,5,2,3,4,4,5,3,4],
    'Geography' : [4,4,4,4,5,5,5,5,3,3],
    'Literature': [3,4,5,3,4,5,3,4,5,4],
    'Biology' : [3,3,3,3,4,5,5,5,5,4],
    'Physics' : [3,4,5,3,4,5,3,4,5,3]
}
# выводим первые 2 строки
df = pd.DataFrame(data)
print(df.head(2))
# выводим среднюю оценку
print(f'Средняя оценка по Математики - {df["Mathematics"].mean()}')
print(f'Средняя оценка по Географии - {df["Geography"].mean()}')
print(f'Средняя оценка по Литературе - {df["Literature"].mean()}')
print(f'Средняя оценка по Биологии - {df["Biology"].mean()}')
print(f'Средняя оценка по Физике - {df["Physics"].mean()}')
# выводим медеанную оценку
print(f"Медианная оценка по Математики - {df['Mathematics'].median()}")
print(f"Медианная оценка по Географии - {df['Geography'].median()}")
print(f"Медианная оценка по Литературе - {df['Literature'].median()}")
print(f"Медианная оценка по Биологии - {df['Biology'].median()}")
print(f"Медианная оценка по Физике - {df['Physics'].median()}")


Q1_math = df['Mathematics'].quantile(0.25)
Q3_math = df['Mathematics'].quantile(0.75)
IQR = Q3_math - Q1_math

print(f'IQR по Математике = {IQR}')
# Вычисляем стандартное отклонение по Математике

std_deviation = df['Mathematics'].std()
print(f"Стандартное отклонение по Математике: {std_deviation}")


df.boxplot(column='Mathematics')
plt.show()