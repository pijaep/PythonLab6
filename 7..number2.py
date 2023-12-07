import random


def min_element_row(row):
    min_element = 10000000

    for element in row:

        if min_element > element:
            min_element = element


    return min_element


def max_element_col(col):
    max_element = -10000000

    for element in col:

        if max_element < element:
            max_element = element

    return max_element


def saddle_points(matrix):
    points = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            element = matrix[i][j]
            if element == min_element_row(matrix[i]) and element == max_element_col(row[j] for row in matrix):
                points.append((i + 1, j + 1))
    return points


while True:
    try:
        number_elements = int(input("Введите количество строк: "))
        if number_elements >= 0:
            break
        else:
            print("Ошибка: Введено отрицательное число. Попробуйте снова.")
            number_elements = int(input("Введите количество строк: "))
        break
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")

while True:
    try:
        number_of_rows = int(input("Введите количество элементов в строке: "))
        if number_of_rows >= 0:
            break
        else:
            print("Ошибка: Введено отрицательное число. Попробуйте снова.")
            number_of_rows = int(input("Введите количество элементов в строке: "))
        break
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")

matrix = [[random.randint(1, 100) for j in range(number_of_rows)] for i in range(number_elements)]

print('Матрица:')
print(*matrix, sep='\n')

if saddle_points(matrix) != []:
    print('Номер строки и столбца седловой точки матрицы: ', *saddle_points(matrix))
else:
    print('В матрице отсутствует седловая точка.')
