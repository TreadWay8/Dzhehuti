    # Importing The Libraries
from datetime import datetime

    # AVG
def avg(some_list):
    size = len(some_list)
    summa = 0
    for a in range(size):
        summa = summa + some_list[a]
    average = summa / size
    return average

    # MIN
def my_min(a):
    mini = a[0]
    for i in range(1, len(a)):
        if a[i] < mini:
            mini = a[i]
    return mini

    # MAX
def my_max(bb):
    maxi = bb[0]
    for i in range(1, len(bb)):
        if bb[i] > maxi:
            maxi = bb[i]
    return maxi

    # DATE
def my_date():
    current_date = datetime.now().date()
    print(current_date)