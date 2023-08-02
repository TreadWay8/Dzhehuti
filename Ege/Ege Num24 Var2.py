    #version 1
file = open("24.txt", "r")

line = file.readline()

note = {}

for i in range(0, len(line)):
    if line[i] == 'A':
        # проверяем что буква содержится в словаре
        if line[i + 1] in note:
            # если да, то увеличиваем кол-во на один
            note[line[i + 1]] = note[line[i + 1]] + 1
        else:
            # если нет, то добавляем букву в словарь и даем значение 1
            note[line[i + 1]] = 1

let = '' # изначально мы не знаем какая буква имеет максимальное значение

for i in note:
    if let == '':
        let = i
    else:
        # если кол-во букв больше чем максимальное вычисляемое
        if note[i] > note[let]:
            # то оно становится максимальным
            let = i

print(note)
# в конце мы получаем в переменно let букву, которая встречается наибольшее кол-во раз
# ответ
print(let)


    #version 2

from collections import Counter
f=open('24.txt').readline()
t=''
for i in range(len(f)-1):
    if f[i]=='A':
        t+=f[i+1]
print(Counter(t).most_common()[0][0])