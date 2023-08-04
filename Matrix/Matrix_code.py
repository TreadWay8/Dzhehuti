    # Версия 3 
file = open('Matrix/matrix.txt', 'r')
file_int = []
    # Работа С Масивом
for line in file:
    t = []
    for i in line:
        if i == "\n":
            continue
        i_int = int(i)
        i_int += 1
        t.append(i_int)
    file_int.append(t)
    # Формировка Таблицы
for i in file_int:
    u = ""
    for g in i:
        u += str(g) + " "
    print(u)

print(file_int)
