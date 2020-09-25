"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""

#1Вариант:

def make_anketa(**kwargs):
     return ' '.join(list(kwargs.values()))


print(make_anketa(name='Василий', surname='Иванов', year='1967',city='Москва', email='wer@mail.ru', telephone='8-903-343-34-34'))
print(make_anketa(name='Иван', surname='Петров'))


#2Вариант
def person_info(name=None, surname=None, year=None, city=None, email=None, telephone=None):
     return f'{name} {surname},{year},{city},{email},{telephone}'

print(person_info(name='Вася',surname='Пупкин'))