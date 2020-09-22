"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""
some_str = input("Введите строку: ")
some_word = []
# Для нумерации строк используется enumerate. Строка разбивается по разделителю(пробелу)
for num, el in enumerate(range(some_str.count(' ') + 1)):
    some_word = some_str.split()
    if len(str(some_word)) <= 10:
        print(f" {num} {some_word[el]}")
    else:
        print(f" {num} {some_word[el][0:10]}")


