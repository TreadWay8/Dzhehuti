    # Импорт Библиотек 
import string
import random

    # Функция Которая Открывает Файл И Записывает Его В Консоль
PASSWORD = open("Password Generator/password.txt", "w+")
PASSWORD.truncate()

    # Функция Которая Генерирует Пароль И Записывает Его В Фай
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

    # Вывод В Консоль
password_length = int(input("Enter the desired password length: "))
generated_password = generate_password(password_length)
print("Your generated password:", generated_password)

    # Запись Пароля В Файл
PASSWORD.write(generated_password)
PASSWORD.close()