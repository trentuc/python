#Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
#Подсказка: использовать функцию reduce()

from functools import reduce


def my_func(el_p, el):
    return el_p * el

print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

#или

from functools import reduce

items = [el for el in range(99, 1001) if el % 2 == 0]
fact = reduce(lambda el_p,p: el_p * p, items)
print(f'Результат перемножения всех элементов списка: {fact}')