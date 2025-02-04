import numpy as np
import pandas as pd


# 1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать
# - списки Python или массивы NumPy
# - скалярные значение
# - словари

print('Задание 1')

a = pd.Series([1, 2, 3, 4, 5])
print(a)

b = pd.Series(np.array([6, 7, 8, 9, 0]))
print(b)

c = pd.Series(5)
print(c)

score_dict = {"a": 10, "b": 20, "c": 30, "d": 0, "e": 60}
d = pd.Series(score_dict)
print(d)


# 2. Привести различные способы создания объектов типа DataFrame
# DataFrame. Способы создания
# - через объекты Series
# - списки словарей
# - словари объектов Series
# - двумерный массив NumPy
# - структурированный массив Numpy

print('Задание 2')

df = pd.DataFrame(pd.Series([5, 6, 7, 8], index=["a", "b", "c", "d"]))
print(df)

age_dict = {"a": 13, "b": 18, "c": 15, "d": 24}

height_dict = {"a": 157, "b": 186, "c": 178, "d": 180}

age = pd.Series(age_dict)
height = pd.Series(height_dict)

students = pd.DataFrame([age_dict, height_dict])
print(students)

students = pd.DataFrame({"age": age, "height": height})
print(students)

df2 = pd.DataFrame(
    np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    ),
    columns=["a", "b", "c"]
)
print(df2)

data = np.array(
    [(1, 2, 3), (4, 5, 6), (7, 8, 9)],
    dtype=[("a", "i4"), ("b", "i4"), ("c", "i4")]
)
df3 = pd.DataFrame(data)
print(df3)


# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, 
# чтобы вместо NaN было установлено значение 1

print('Задание 3')

pop = pd.Series(
    {
        "city_1": 1001,
        "city_2": 1002,
        "city_3": 1003,
        "city_41": 1004,
        "city_51": 1005,
    }
)

area = pd.Series(
    {
        "city_1": 9991,
        "city_2": 9992,
        "city_3": 9993,
        "city_42": 9994,
        "city_52": 9995,
    }
)

data = pd.DataFrame({'area1': area, 'pop1': pop}).fillna(1)
print(data)

# 4. Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ

print('Задание 4')

rng = np.random.default_rng(1)

A = rng.integers(0, 10, (3, 4))
print(A)

df = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])
print(df)

print(df.iloc[:, 0].values[:, np.newaxis])

print(df - df.iloc[:, 0].values[:, np.newaxis])


# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()

print('Задание 5')

df = pd.DataFrame(
    [
        [1, 2, 3, 4, np.nan, np.nan],
        [1, 2, 3, np.nan, 5, 6],
        [1, np.nan, 3, np.nan, np.nan, 6],
    ],
)
print(df)

"""
ffill() заполняет NA-значения предыдущим валидным значением.
"""
print('ffill:\n', df.ffill())

"""
bfill() заполняет NA-значения следующим валидным значением.
"""
print('bfill:\n', df.bfill())