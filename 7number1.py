import random

while True:
    try:
        number_elements = int(input("Введите количество строк: "))
        if number_elements >= 0:
            break
        else:
            print("Ошибка: Введено отрицательное число. Попробуйте снова.")
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
        break
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")


matrix = [[random.randint(-100, 100) for j in range(number_of_rows)] for i in range(number_elements)]
print()
print('Изначальная матрица: ')
print(*matrix, sep='\n')

def row_characteristic(row):
    sum = 0
    for num in row:
        if num < 0 and num % 2 == 0:
            sum += num
    return sum


def sort_matrix_characteristic(matrix):
    sort_matrix = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if row_characteristic(matrix[i]) <= row_characteristic(matrix[j]):
                matrix[i], matrix[j] = matrix[j], matrix[i]

    return matrix


print()
result = sort_matrix_characteristic(matrix)
print('Отсортированая матрица: ')
print(*result, sep='\n')
