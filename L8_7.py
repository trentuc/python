# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __mul__(self, other):
        real_part = self.real * other.real - (self.imaginary * other.imaginary)
        imaginary_part = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __str__(self):
        if self.imaginary >= 0:
            return "%.1f+%.1fi" % (self.real, self.imaginary)
        return "%.1f%.1fi" % (self.real, self.imaginary)


z_1 = ComplexNumber(-3, -4)
z_2 = ComplexNumber(2, 4)
print(f'Число z_1: {z_1}')
print(f'Число z_2: {z_2}')
print(f'Сумма z_1 + z_2: {z_1 + z_2}')
print(f'Произведение z_1 * z_2: {z_1 * z_2}')
