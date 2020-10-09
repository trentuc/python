# Реализовать проект расчета суммарного расхода ткани на
# производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто)
# и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать
# формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на
# практике полученные на этом уроке знания: реализовать абстрактные
# классы для основных классов проекта, проверить на практике
# работу декоратора @property.
class Dress:
    default_clothing ='None'
    default_numb = 0
    def __init__(self, clothing=default_clothing, numb=default_numb,V=None,H=None):
        self.clothing = clothing
        self.numb = numb


    def info(self):
        print(f'Вид одежды: {self.clothing}')
        print(f'Количество эземпляров одежды {self.clothing}: {self.numb}')

class Suit(Dress):
    default_clothing = 'Костюм'

    def __init__(self, numb, H,clothing = default_clothing,V=None):
        super().__init__(clothing,numb,H)
        self.clothing = clothing
        self.numb = numb
        self.H = H

    @property
    def get_square_s(self):
        self.square_s = round((self.H * 2 + 0.3) * self.numb)
        return self.square_s

class Coat(Dress):
    default_clothing = 'Пальто'
    def __init__(self,numb,V,clothing=default_clothing,H=None):
        super().__init__(clothing, numb, V)
        self.clothing = clothing
        self.numb = numb
        self.V = V
    @property
    def get_square_c(self):
        self.square_c = round((self.V / 6.5 + 0.5) * self.numb)
        return self.square_c

# Здесь попытался из класса вызвать другой класс - не "докрутил"
class F_square:
    def __init__(self):
        self.square_rez = []

    def adde(self, numb, V, H):
        self.square_rez.append(Coat(numb, V))
        self.square_rez.append(Suit(numb, H))

    def sguare(self):
        main_square = 0
        for el in self.square_rez:
            main_square += el
        return main_square


coat = Coat(3, 50)
suit = Suit(4, 1.82)
print(f'Площадь ткани на пальто: {coat.get_square_c}')
print(f'Площадь ткани на костюм: {suit.get_square_s}')
print(f'Общий расход ткани: {coat.get_square_c + suit.get_square_s}')
coat.info()
suit.info()
