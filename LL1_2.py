"""	Пользователь вводит время в секундах.
    Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
    Используйте форматирование строк.
"""
time = int(input('Введите время в секундах: '))
hours = str(time // 3600)
minutes = (time // 60) % 60
seconds = time % 60
if minutes < 10:
    minutes = str('0' + str(minutes))
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = str('0' + str(seconds))
else:
    seconds = str(seconds)
print(f"Время в формате чч:мм:сс {hours} : {minutes} : {seconds}")



