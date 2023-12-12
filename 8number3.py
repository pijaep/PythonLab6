while True:
    try:
        n = int(input("Введите значение N: "))
        break
    except:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")


def print_digits(n):
    if n < 10:
        print(n)
    else:
        print(n % 10, end=' ')
        print_digits(n // 10)


print('Цифры в обратном порядке числа N:')

print_digits(n)
