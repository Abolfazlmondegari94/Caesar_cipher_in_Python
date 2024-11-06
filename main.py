def cesar(message, shift, mode=1):
    temp = ""
    for char in message:
        n = ord(char)
        n += shift * mode
        temp += chr(n)
    return temp

message = input("Enter your text: ")
shift = int(input("Enter your shift: "))
encrypt = cesar(message, shift, 1)
decrypt = cesar(encrypt, shift, -1)
print("Encrypted text:", encrypt)
print("Decrypted text:", decrypt)
