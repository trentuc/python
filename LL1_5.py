"""	Запросите у пользователя значения выручки и издержек фирмы.
    Определите, с каким финансовым результатом работает фирма
    (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
     Выведите соответствующее сообщение.
    Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
    Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
revenue = float(input('Введите значение выручки фирмы:  '))
expense = float(input('Введите расходы фирмы:  '))
fin_result = revenue - expense
print(fin_result)
if fin_result > 0:
    print('Фирма работает с прибылью. Выручка больше издержек.')
    print(f"Рентабельность выручки: {fin_result / expense:.2f}")
    number_employees = int(input('Введите число сотрудиков фирмы:  '))
    print(f"Прибыль на одного сотрудника: {fin_result / number_employees:.2f}")
elif fin_result == 0:
        print('Издержки равны выручке.')
else:
    print('Фирма работает в убыток. Издержки больше выручки.')

