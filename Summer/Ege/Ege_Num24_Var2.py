    # 3 Версия
file = open("24.txt", "r")

line = file.readline()

note = {}

for i in range(0, len(line)):
    if line[i] == 'A':
        # Проверяем Что Буква Содержится В Словаре
        if line[i + 1] in note:
            # Если Да, То Увеличиваем Кол-Во На Один
            note[line[i + 1]] = note[line[i + 1]] + 1
        else:
            # Если Нет, То Добавляем Букву В Словарь И Даем Значение 1
            note[line[i + 1]] = 1

let = '' # Изначально Мы Не Знаем Какая Буква Имеет Максимальное Значение

for i in note:
    if let == '':
        let = i
    else:
        # Если Кол-Во Букв Больше Чем Максимальное Вычисляемое
        if note[i] > note[let]:
            # То Оно Становится Максимальным
            let = i

print(note)
# В Конце Мы Получаем В Переменно Let Букву, Которая Встречается Наибольшее Кол-Во Раз
# Ответ
print(let)


    #version 2

from collections import Counter
f=open('24.txt').readline()
t=''
for i in range(len(f)-1):
    if f[i]=='A':
        t+=f[i+1]
print(Counter(t).most_common()[0][0])