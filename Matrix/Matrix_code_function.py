    # Функция Которая Октрывает Файл И Делает Из Него Двумерный Массив
# def open_int(open_int):

    # Функция Которая В Масиве Разбирает Файл И К Каждому Отдельному Числу Плюсует 1 
# def plus_one(file_int):

f = open('Matrix/matrix.txt', '+w')
file = f.read()
print(file)
# file_int = []
# for line in f:
#     t =[]
#     for i in line:
#         if i == "\n":
#             continue
#         else:
#             i = int(i)
#             t.append(int(i))
#     file_int.append(t)

# print(file_int)

#     # Версия 3 
# file = open('Matrix/matrix.txt', 'r')
# file_int = []
#     # Работа С Масивом
# for line in file:
#     t = []
#     for i in line:
#         if i == "\n":
#             continue
#         i_int = int(i)
#         i_int += 1
#         t.append(i_int)
#     file_int.append(t)
#     # Плюсуем 1
# for i in file_int:
#     u = ""
#     for g in i:
#         u += str(g) + " "
#     print(u)

# print(file_int)