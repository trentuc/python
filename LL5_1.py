#Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

try:
    fname = input('Название файла: ')
    f = open(fname,'w')
    while True:
        s = input('Введите строку (пустая строка - Выход): ')
        if s == '': break
        f.write(s+'\n')
    f.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")




