while True:
    try:
        a = float(input("Введите значение A: "))
        break
    except:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")

while True:
    try:
        n = int(input("Введите значение N: "))
        break
    except:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")


def Power(a, n):
    if n > 0:
        return a**n
    elif n < 0:
        return 1/(a**abs(n))

print('Значение функции по введенным данным равно: ', Power(a,n))
