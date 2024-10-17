import pandas as pd

# Чтение данных из файла 'titanic.csv'
df = pd.read_csv('titanic.csv', delimiter=',')

# Вывод первых 5 строк данных
# Используйте метод .head()
print (df.head())

print (df.info())

print(df.isna().sum())

# Заполнение пропущенных значений (например, заполним средними значениями в числовых столбцах)
df_filled = df.fillna(df.mean(numeric_only=True))

# Проверка на наличие NaN после заполнения
print(df_filled.isna().sum())

# Удаление строк с NaN
df_dropped = df.dropna()

# Проверка на наличие NaN после удаления строк
print(df_dropped.isna().sum())

# Выбор столбца по метке
name_column = df['Name']

# Выбор нескольких столбцов
sex_age_column = df["Sex", "Age"]

# Выбор строки по индексу,
first_row = df.loc[0]