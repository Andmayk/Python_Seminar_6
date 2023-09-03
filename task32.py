# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

def input_int(massage="Введите целое значение: "):
    return int(input(massage))

def fill_index(array):
    list_index = list()
    for i in range(len(array)):
        if  min_volume <= array[i] <= max_volume:
            list_index.append(i)
    return list_index


min_volume = input_int("Введите минимальное значение диапозона:")
max_volume = input_int("Введите максимальное значение диапозона:")

array_index = fill_index(array)

print(array_index)
