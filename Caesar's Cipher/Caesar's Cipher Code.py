    #Creating Variables
Alphabet_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
Alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
Bias = int(input('Encryption step: '))
Message = input("Message to encrypt: ").upper()
Total = ''
Language = input('Choose language RU/EU: ')
if Language == 'RU':
    for i in Message:
        Place = Alphabet_RU.find(i)   # Algorithm For Encrypting A Message In Russian 
        New_Place = Place + Bias
        if i in Alphabet_RU:
            Total += Alphabet_RU[New_Place]
        else:
            Total += i
else:
    for i in Message:
        Place = Alphabet_EU.find(i)		# Algorithm For Encrypting A Message In English 
        New_Place = Place + Bias
        if i in Alphabet_EU:
            Total += Alphabet_EU[New_Place]
        else:
            Total += i
print(Total)