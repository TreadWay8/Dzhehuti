    # Версия 3 
file = open('Matrix/matrix.txt', 'r')
file_int = []
print("╔╦╦╦═╦╗╔═╦═╦══╦═╗")
print("║║║║╩╣╚╣═╣║║║║║╩╣")
print("╚══╩═╩═╩═╩═╩╩╩╩═╝")
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

def get_max_width(matrix):
    return 5

def out(matrix):
    width = get_max_width(matrix)

    column_count = len(matrix[0])
    print("╔" + (column_count - 1) * (width*"═" + "╦") + width*"═" + "╗")

    for i in range(0, len(matrix)):
        u = "║"
        for col in matrix[i]:
            u += ("%" + str(width) +"d║")%(col)
        print(u)
        if (i < len(matrix) - 1):
            print("╠" + (column_count - 1) * (width*"═" + "╬") + width*"═" + "╣")

    print("╚" + (column_count - 1) * (width*"═" + "╩") + width*"═" + "╝")

print(file_int)
out(file_int)
