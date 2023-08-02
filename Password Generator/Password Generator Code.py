    # Importing The Libraries 
import string
import random

    # Function To Open The File
PASSWORD = open("Password Generator/password.txt", "w+")
PASSWORD.truncate()

    # Function To Generate Password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

    # Main Function
password_length = int(input("Enter the desired password length: "))
generated_password = generate_password(password_length)
print("Your generated password:", generated_password)

    # Writing The Password To The File And Closing The File
PASSWORD.write(generated_password)
PASSWORD.close()