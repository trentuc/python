#Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

# В функции int_func используется "симметрия" ASCII таблицы (латинских символов):
# 'a' - 'A' == 'b' - 'B'
# 'b' - 'B == 'c' - 'C'
# 'c' - 'C' == 'd' - 'D'
# и т.д.
# по другому: ord('little letter') - ord('a') == ord('big letter') - ord('A')
def int_func(word):
    """
    Первая прописная буква
    :param word: слово из маленьких латинских букв
    :return: возвращает это слово, но с прописной первой буквой
    """
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]

def int_func1(word):
    word = word.title()
    return word

print(int_func('moscow'))
print(int_func1('kemerovo'))


def string_title(string):
    """
    Функция использует функцию int_func(word), возвращает  слово с прописной первой буквой
    :param string: cтрока из слов (латиница) с маленькой буквы каждое слово
    :return: исходная строка, каждое слово с большой буквы
    """
    res = []
    string = string.split()
    for word in string:
        res.append(int_func(word))
    return ' '.join(res)

print(string_title('moscow kemerovo kirov praga'))









