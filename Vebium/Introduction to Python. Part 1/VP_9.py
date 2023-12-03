numb = 56754376
if numb % 2 == 0:
    numb = ((numb * 4) // 100000) // 42
else:
    numb = (((numb * 3) // 10000) % 1000) // 42
if numb > 146:
    print(numb // 2)
else:
    print(numb // 3)