# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
# нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.
class DivNull:
    def __init__(self, numerator, denominator):
        self.divider = numerator
        self.denominator = denominator

    @staticmethod
    def div_null(numerator, denominator):
        try:
            return (numerator / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = DivNull(10, 100)
print(DivNull.div_null(50, 0))
print(DivNull.div_null(10, 0.5))
print(div.div_null(100, 0))
