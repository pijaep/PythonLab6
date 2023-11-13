while True:
    try:
        n = int(input("Введите количество элементов: "))
        break
    except ValueError:
        print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")

s = []
for _ in range(n):
    while True:
        try:
            x = int(input("Введите элемент списка (целое число): "))
            break
        except ValueError:
            print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")
    s.append(x)

ma = -1000000
ind = -1
for i in s:
    ind += 1
    if i > ma:
        ma = i
        indma = ind

su = 0
for i in range(len(s)):
    if s[i] > 0 and i < indma:
        su += s[i]
    if i >= indma:
        break

sobr = []
for i in range(len(s) - 1, -1, -1):
    sobr.append(s[i])

print('Изначальный список: ', *s)
print('Сумма положительных элементов до максимального элемента:', su)
print('Обратный порядок следования элементов: ', *sobr)
