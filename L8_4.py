# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# '''
#
# # ----------------------------------- 5 ----------------------------------------
#
# '''
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании. Для хранения данных
# о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
# любую подходящую структуру, например словарь.
# '''
#
# # ----------------------------------- 6 ----------------------------------------
# '''
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных
# на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.

class Office:

    def __init__(self, name, price, quantity, numb):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = numb
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.my_unit}'



class Printer(Office):

    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Office):

    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Office):

    def to_copier(self):
        return f'to copier smth  {self.numb} times'

class Stock:

    def __init__(self):
        self.my_store = []

    def add(self, kls):
        self.my_store.append(kls)
        return self.my_store

    def transfer(self, kls):
        self.my_store.remove(kls)
        return self.my_store


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 6, 7)
unit_3 = Copier('Xerox', 1500, 1, 3)
print(unit_3)
stock1 = Stock()
stock1.add(unit_1)
stock1.add(unit_2)
stock1.add(unit_3)
print(stock1.my_store[0])
print(stock1.my_store[1])
stock1.transfer(unit_1)
print((stock1.my_store[0]))
print(unit_3.to_copier())
