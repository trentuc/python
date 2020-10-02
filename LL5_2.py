#Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


try:
    with open(r"file_2.txt", "r") as f:
        print(f'Содержимое файла: \n {f.read()} \n')
        f.seek(0)
        num_line = 1
        for line in f:
            content = line.split()
            print(f"Количество слов в {num_line} стр.: {len(content)}")
            num_line += 1
        print(f'Количество строк в файле - {num_line-1}')
except IOError:
    print("Произошла ошибка ввода-вывода!")

