print("╔╦╦╦═╦╗╔═╦═╦══╦═╗")
print("║║║║╩╣╚╣═╣║║║║║╩╣")
print("╚══╩═╩═╩═╩═╩╩╩╩═╝")
PASSWORD = open("Password_Generator/password2.txt", "w+")
PASSWORD.truncate()
str_to_conv = input("Enter the string to convert: ")
print("The string that we have taken is ",str_to_conv) 

bin_result = ''.join(format(ord(x), '08b') for x in str_to_conv) 
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    """Convert a string of bits to text."""
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


print("The string that we obtain binary conversion is ",bin_result) 

PASSWORD.write(bin_result)
PASSWORD.write(" word : ")
PASSWORD.write(text_from_bits((bin_result)))
PASSWORD.close()

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    """Convert a string of bits to text."""
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

# ╗ ═ ╔ ║ ╠ ╚ ╝ ═

leni = len(bin_result)
leno = len(str_to_conv)


print(f"╔" + leno * "═" + "╗")
print("║" + str_to_conv + "║")
print(f"╚" + leno * "═" + "╝")


print(f"╔" + leni * "═" + "╗")
print("║" + bin_result + "║")
print(f"╚" + leni * "═" + "╝")

