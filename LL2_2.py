"""
Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
el_number = int(input("Введите количество элементов списка: "))
some_list = []
el = 0
for i in range(el_number):
    some_list.append((input(f"Введите значение списка {i}: ")))
print(f"Исходный список: {some_list}")
#Обмен значениями через кортежи
for elem in range(int(len(some_list) / 2)):
    some_list[el], some_list[el + 1] = some_list [el + 1], some_list[el]
    el += 2
print(f"Преобразованный список: {some_list}")