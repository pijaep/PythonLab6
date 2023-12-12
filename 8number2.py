def chek_digitx():
    while True:
        try:
            a = float(input("Введите значение x: "))
            return a
        except:
            print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")


def chek_digity():
    while True:
        try:
            a = float(input("Введите значение y: "))
            return a
        except:
            print("Вы ввели некорректное значение. Пожалуйста, введите целое число.")


def Quarter(x, y):
    if x > 0 and y > 0:
        return 'I'
    if x < 0 and y > 0:
        return 'II'
    if x < 0 and y < 0:
        return 'III'
    if x > 0 and y < 0:
        return 'IV'


x1, y1, x2, y2, x3, y3 = chek_digitx(), chek_digity(), chek_digitx(), chek_digity(), chek_digitx(), chek_digity()

print('Номер координатной четверти с коодинатами', '(' + str(x1), str(y1) + '):', Quarter(x1, y1))
print('Номер координатной четверти с коодинатами', '(' + str(x2), str(y2) + '):', Quarter(x2, y2))
print('Номер координатной четверти с коодинатами', '(' + str(x3), str(y3) + '):', Quarter(x3, y3))
