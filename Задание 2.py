m = input('Введите текст:').split()
s = m.copy()
for i in range(len(s)):
    flag = True
    if not s[i][-1].isalpha() and not s[i][-1].isdigit():
        s[i] = s[i][0:-1]
    for j in range(len(s[i])):
        if not s[i][j].isalpha():
            flag = False
    if flag == False:
        while flag == False:
            print('Слово', s[i], 'введено не правильно.')
            s[i] = input('Введите данное слово без ошибок: ')
            newS = s[i]
            k = 0
            for x in range(len(newS)):
                if newS[x].isalpha():
                    k += 1
            if k == len(newS): flag = True

ans = []
for i in s:
    if i[0] in 'ауоыиэяюёеaeiouy':
        ans.append(i)

print('Изначальный текст: ', *m)
print('Измененный список: ', *s)
print('Количество слов теста начинающихся с главной буквы: ', len(ans))
