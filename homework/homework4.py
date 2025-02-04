import numpy as np
import pandas as pd


# # 1. Разобраться как использовать мультииндексные ключи в данном примере

print('Задание 1')
index = [
    ('city_1', 2010),
    ('city_1', 2020),
    ('city_2', 2010),
    ('city_2', 2020),
    ('city_3', 2010),
    ('city_3', 2020),
]

population = [
    101,
    201,
    102,
    202,
    103,
    203,
]

pop = pd.Series(population, index=index)
pop_df = pd.DataFrame(
    {
        'total': pop,
        'something': [
            10,
            11,
            12,
            13,
            14,
            15,
        ]
    }
)

pop_df = pop_df.reindex(pd.MultiIndex.from_tuples(index))
print(pop_df)

print(pop_df.loc[('city_1',), 'something'])
print(pop_df.loc[['city_1', 'city_3'], ['total', 'something']])
print(pop_df.loc[['city_1', 'city_3'], 'something'])

# ???? ## pop_df_1 = pop_df.loc???['city_1', 'something']
# ???? ## pop_df_1 = pop_df.loc???[['city_1', 'city_3'], ['total', 'something']]
# ???? ## pop_df_1 = pop_df.loc???[['city_1', 'city_3'], 'something']

# 2. Из получившихся данных выбрать данные по 
# - 2020 году (для всех столбцов)
# - job_1 (для всех строк)
# - для city_1 и job_2

print('Задание 2')

index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)
columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)
rng = np.random.default_rng(1)
data = rng.random((4, 6))
data_df = pd.DataFrame(data, index=index, columns=columns)
print(data_df)

print(data_df.loc[(slice(None), 2020), :])
print(data_df.loc[:, (slice(None), 'job_1')])
print(data_df.loc[('city_1',), (slice(None), 'job_2')])

# 3. Взять за основу DataFrame со следующей структурой

print('Задание 3')

index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)
columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

# Выполнить запрос на получение следующих данных
# - все данные по person_1 и person_3
# - все данные по первому городу и первым двум person-ам (с использование срезов)
#
# Приведите пример (самостоятельно) с использованием pd.IndexSlice

rng = np.random.default_rng(1)
data = rng.random((4, 6))
data_df = pd.DataFrame(data, index=index, columns=columns)
print(data_df)

print(data_df[['person_1', 'person_3']])
print(data_df.loc['city_1', 'person_1':'person_2'])

print('Пример pd.IndexSlice: выбор city_1 и job_2')
print(data_df.loc['city_1', pd.IndexSlice[:, 'job_2']])

#4. Привести пример использования inner и outer джойнов для Series (данные примера скорее всего нужно изменить)

print('Задание 4')

"""
join='outer' объединяет с использованием всех колонок, а join='inner'
оставляет только колонки, которые есть в обоих DataFrame
"""
df_1 = pd.DataFrame([
    ['apple', 3, 'sweet'],
    ['lemon', 2, 'sour'],
    ['tomato', 5, 'umami']
], columns=['food', 'amount', 'taste'])

df_2 = pd.DataFrame([
    ['apple', 2, 'small'],
    ['watermelon', 3, 'big']
], columns=['food', 'amount', 'size'])
print(df_1)
print(df_2)

print(pd.concat([df_1, df_2], join='outer'))
print(pd.concat([df_1, df_2], join='inner'))
# ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
# ser2 = pd.Series(['b', 'c', 'f'], index=[4,5,6])

# print (pd.concat([ser1, ser2], join='outer'))
# print (pd.concat([ser1, ser2], join='inner'))