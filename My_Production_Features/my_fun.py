    # Импорт Библиотек
from datetime import datetime
import time
    # Среднее значение
def avg(some_list):
    size = len(some_list)
    summa = 0
    for a in range(size):
        summa = summa + some_list[a]
    average = summa / size
    return average

    # Минимальное значение
def my_min(a):
    mini = a[0]
    for i in range(1, len(a)):
        if a[i] < mini:
            mini = a[i]
    return mini

    # Максимально значение
def my_max(bb):
    maxi = bb[0]
    for i in range(1, len(bb)):
        if bb[i] > maxi:
            maxi = bb[i]
    return maxi

    # Дата 
def my_date():
    current_date = datetime.now().date()
    print(current_date)

    # Время Выполнения Кода
def timer():
    start_time= time.time()
    def fun():
        a=2
        b=3
        c=a+b
    end_time= time.time()
    fun()
    timetaken = end_time - start_time
    print("Your program takes: ", timetaken) 