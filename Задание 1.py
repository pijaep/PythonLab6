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
                    k+=1
            if k == len(newS): flag = True

ans = []
for i in s:
    k = 0
    for j in i:
        if j == 'а' or j == 'a':
            k+=1
    if k>=2: ans.append(i)

print('Изначальный текст: ', *m)
print('Измененный список: ', *s)
print('Слова которые содержат не менее 2-х букв "а":')
print(*ans)
