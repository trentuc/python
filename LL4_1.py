#	Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#	В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
#	Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

script_name, working_hours, salary, bonus = argv
res = float(working_hours) * float(salary) + float(bonus)
print(f'заработная плата сотрудника:  {res}')

#Вызов с параметрами:
# (venv) C:\Users\aut\Documents\geek\python\pythonproject\Osnov\L4>python LL4_1.py 45.4 50.5 300
# заработная плата сотрудника:  2592.7
#
# (venv) C:\Users\aut\Documents\geek\python\pythonproject\Osnov\L4>python LL4_1.py 45 5 60
# заработная плата сотрудника:  285.0
#
# (venv) C:\Users\aut\Documents\geek\python\pythonproject\Osnov\L4>


