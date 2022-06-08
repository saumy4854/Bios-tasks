def encrypt(key, message):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for i in message:
        if i in alpha:
            letter_index = (alpha.find(i) + key) % 26

            result = result + alpha[letter_index]
        else:
            result = result + i

    return result

def decrypt(key, message):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for i in message:
        if i in alpha:
            letter_index = (alpha.find(i) - key) % 26

            result = result + alpha[letter_index]
        else:
            result = result + i

    return result

key = int(input("Shift Key : "))
choice = int(input("Enter 0 to ENCRYPT and 1 to DECRYPT : "))
message = input("Input : ")
if choice == 0:
    print(encrypt(key, message))
elif choice == 1:
    print(decrypt(key, message))
else:
    print("Wrong Choice")