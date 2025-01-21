import array
import numpy as np


## 1. Какие еще существуют коды типов?
print('Задание 1')
print(list(array.typecodes))
print('b - char')
print('B - unsigned char')
print('h - short')
print('H - unsigned short')
print('i - int')
print('I - unsigned int')
print('l - long')
print('L - unsigned long')
print('f - float')
print('d - double')
print('u - unicode symbol')


## 2. Напишите код, подобный приведенному выше, но с другим типом
print('Задание 2')
print('Примеры:')
b = array.array('d', [2.5, 3.2, 3.3]) # float
print(b)
c = array.array('L', [1, 2, 3, 4]) # unsigned long
print(c)
d = array.array('u', 'hello') # unicode
print(d)

## 3. Напишите код для создания массива с 5 значениями, располагающимися через равные интервалы в диапазоне от 0 до 1
print('Задание 3')
equal_array = np.linspace(0, 1, 5)
print(equal_array)

## 4. Напишите код для создания массива с 5 равномерно распределенными случайными значениями в диапазоне от 0 до 1
print('Задание 4')
np.random.seed(42)
uniform_array = np.random.uniform(size=5)
print(uniform_array)

## 5. Напишите код для создания массива с 5 нормально распределенными случайными значениями с мат. ожиданием = 0 и дисперсией 1
print('Задание 5')
normal_array = np.random.normal(size=5)
print(normal_array)

## 6. Напишите код для создания массива с 5 случайными целыми числами в от [0, 10)
print('Задание 6')
rand_array = np.random.randint(0, 10, 5)
print(rand_array)

## 7. Написать код для создания срезов массива 3 на 4
## - первые две строки и три столбца
## - первые три строки и второй столбец
## - все строки и столбцы в обратном порядке
## - второй столбец
## - третья строка

print('Задание 7')
source = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print('-', source)

print('-', source[:2, :3])

print('-', source[:3, 1])

print('-', source[::-1, ::-1])

print('-', source[:, 1])

print('-', source[2, :])

## 8. Продемонстрируйте, как сделать срез-копию
print('Задание 8')
origin = np.array([1, 2, 3, 4, 5])
copy_origin = origin[1:5].copy()
copy_origin[0] = -1
assert origin[0] != -1
print('origin', origin)
print('copy', copy_origin)
assert len(origin) != len(copy_origin)

## 9. Продемонстрируйте использование newaxis для получения вектора-столбца и вектора-строки
print('Задание 9')
source = np.array([1, 2, 3, 4, 5])
print(f'Вектор-столбец: {source[:, np.newaxis]}')
print(f'Вектор-строка: {source[np.newaxis, :]}')

## 10. Разберитесь, как работает метод dstack
print('Задание 10')
top = np.array([[1, 2], [3, 4]])
bottom = np.array([[5, 6], [7, 8]])
dstacked = np.dstack((top, bottom))
print(f'Dstack: {dstacked}')
print(f'Vstack: {np.vstack([top, bottom])}')
print(f'HStack: {np.hstack([top, bottom])}')

## 11. Разберитесь, как работают методы split, vsplit, hsplit, dsplit
print('Задание 11')
source = np.array([1, 2, 3, 4, 5, 6])
print('Split - Разделяет массив на несколько подмассивов:', np.split(source, 3))
print('Vsplit - Разделяет массив на несколько подмассивов по вертикали (по строкам):', 
    np.vsplit(np.array([[1, 2], [3, 4], [5, 6]]), 3))
print('Hsplit - Разделяет массив на несколько подмассивов по горизонтали (по столбцам):', 
    np.hsplit(source, 2))
x = np.arange(16.0).reshape(2, 2, 4)
print(x)
print('DSplit - Разбивает массив на несколько подмассивов по 3-й оси (глубине):', 
    np.dsplit(x, 2))

## 12. Привести пример использования всех универсальных функций, которые я привел
print('Задание 12')
x = np.random.randint(0, 50, 5)
y = np.random.randint(0, 50, 5, dtype=int)
print(x)
print(y)

print(x - y)
print(np.subtract(x, y))

print(-x)
print(np.negative(x))

print(x / 2)
print(np.divide(x, 2))

print(y // 2)
print(np.floor_divide(y, 2))

print(x ** 2)
print(np.power(x, 2))

print(y % 3)
print(np.remainder(y, 3))
