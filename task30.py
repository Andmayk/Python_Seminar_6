# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def input_int(massage="Введите целое значение: "):
    return int(input(massage))

def an(a1: int, n: int, d: int):
    return a1 + n * d 

def fill_progression(progression):
    for i in range(count_n):
        progression.append(an(start, i, step))

start = input_int("Введите первый элемент арифметической прогрессии: ")
step = input_int("Введите разность (шаг арифметической прогрессии): ")
count_n = input_int("Введите количество элементов арифметической прогрессии: ")

arithmetic_progression = []
fill_progression(arithmetic_progression)
print(*arithmetic_progression)

# ну или одной строкой используя range()
print(*list(range(start, (start+count_n*step), step)))

