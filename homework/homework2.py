import numpy as np


# Вопрос 1: Что надо изменить в последнем примере, чтобы он заработал без ошибок 
# (транслирование)?
print('Задание 1')
"""
Ответ: Необходимо изменить размерность второго массива. Это можно сделать либо
с помощью newaxis, либо при помощи reshape
"""
# a = np.ones((3, 2))
# b = np.arange(3)

a = np.ones((3, 2))
print('a = ', a)
b = np.arange(3)
print('b = ', b)

b1 = b[:, np.newaxis]
print('b1 = ', b1)
print('a + b1 = ', a + b1)

b2 = np.reshape(b, (3, 1))
print('b2 = ', b2)
print('a + b2 = ', a + b2)

#      a: (3, 2) -> (3, 2)
# b1, b2: (3, 1) -> (3, 2)

# Вопрос 2. Пример для y. Вычислить количество элементов (по обоим размерностям),
# значения которых больше 3 и меньше 9
print('Задание 2')

y = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
print(f'y = {y}')

inds = (y > 3) & (y < 9)
print(inds)

print(f'axis=0:\n {(np.sum(inds , axis=0))}')
print(f'axis=1:\n {(np.sum(inds , axis=1))}')
print('Элементы:')
print(y[inds])
