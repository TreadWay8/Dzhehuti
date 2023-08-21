import os

print("╔╦╦╦═╦╗╔═╦═╦══╦═╗")
print("║║║║╩╣╚╣═╣║║║║║╩╣")
print("╚══╩═╩═╩═╩═╩╩╩╩═╝")
file = open('Matrix/matrix2d.txt', 'r')
file_int = []

matrix2d = []

for line in file:
    nums = line.split("|")
    ar = []
    for num in nums:
        n = int(num.replace("\n", ""))
        ar.append(n)
    matrix2d.append(ar)

def max_nums(m2d):
    max_i = 0
    max_j = 0
    for i in range(0, len(m2d)):
        for j in range(0, len(m2d[i])):
            if m2d[i][j] > m2d[max_i][max_j]:
                max_i = i
                max_j = j
    return [max_i, max_j]

def min_nums(m2d):
    mix_i = 0
    mix_j = 0
    for i in range(0, len(m2d)):
        for j in range(0, len(m2d[i])):
            if m2d[i][j] < m2d[mix_i][mix_j]:
                mix_i = i
                mix_j = j
    return [mix_i, mix_j]

def modern_array(m2d):
    matrix_finally = []
    for line in m2d:
        time =[]
        for i in line:
            i += 5
            time.append(i)
        matrix_finally.append(time)
    return matrix_finally

def get_max_width(m2d):
    max_width = 0
    for x in m2d:
        for y in x:
            if len(str(y)) > max_width:
                max_width = len(str(y))
    return max_width + 2

def out(m2d):
    width = get_max_width(m2d)
    column_count = len(m2d[0])
    print("╔" + (column_count - 1) * (width*"═" + "╦") + width*"═" + "╗")

    for i in range(0, len(m2d)):
        u = "║"
        for col in m2d[i]:
            u += ("%" + str(width) +"d║")%(col)
        print(u)
        if (i < len(m2d) - 1):
            print("╠" + (column_count - 1) * (width*"═" + "╬") + width*"═" + "╣")

    print("╚" + (column_count - 1) * (width*"═" + "╩") + width*"═" + "╝")


#Выводим Все Данные
x = max_nums(matrix2d)
print("Максимальное число: ",  matrix2d[x[0]][x[1]], "Индекс максимального числа: ", x)

y = min_nums(matrix2d)
print("Минимальное число: ", matrix2d[y[0]][y[1]], "Индекс минимального числа", y)

print
out(modern_array(matrix2d))
