import pandas as pd

df = pd.read_csv('Refugee_Asylum_data.csv')
print(df.head())

print(df.info())

print(df.describe())

print(df.loc[5])