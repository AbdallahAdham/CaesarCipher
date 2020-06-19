print("------------------------------------------------")
print("Welcome to Caesar Cipher Encryptor/Decryptor !")
print("Made by Abdallah Adham")
print("------------------------------------------------")


def Encrypt (plain, key):
    Alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    plainSize = len(plain)
    cipher = list()
    for i in range(plainSize):
        char = plain[i]
        for j in range(len(Alphabet)):
            if char == Alphabet[j]:
                if (j + 2 * key) > len(Alphabet):
                    cipheredChar = Alphabet[(j + 2 * key) - len(Alphabet)]
                else:
                    cipheredChar = Alphabet[j + 2 * key]
                cipher.append(cipheredChar)
    cipher = ''.join(cipher)
    return cipher
def DecryptKey (cipher, key):
    Alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    cipherSize = len(cipher)
    plain = list()
    for i in range(cipherSize):
        char = cipher[i]
        for j in range (len(Alphabet)):
            if char == Alphabet[j]:
                if (j - 2 * key) < 0:
                    plainChar = Alphabet[len(Alphabet) + (j - 2 * key)]
                else:
                    plainChar = Alphabet[j - 2 * key]
                plain.append (plainChar)
    plain = ''.join (plain)
    return plain
def BruteForce (cipher):
    Alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    cipherSize = len(cipher)
    for i in range(13):
        plain = list ()
        for j in range(cipherSize):
            char = cipher[j]
            for k in range(len(Alphabet)):
                if char == Alphabet[k]:
                    plainChar = Alphabet[k - 2 * i]
                    plain.append(plainChar)
        plain = ''.join (plain)
        print("Decrypted Text #" + str(i+1) + " : " + plain)

print("What do you want ? ")
print("1) Encrypt a Plain Text 2) Decrypt a Cipher Text")
choice = int(input())
if choice == 1:
    print("Enter the Plain Text ?")
    plain = str(input())
    print("Enter the key for Encryption ?")
    key = int(input())
    print("The Plain Text : " + plain)
    print("The Cipher Text : " + Encrypt(plain, key))
elif choice == 2:
    print("What do you want ?")
    print("1) Decrypt by Specific key ? 2) Brute Force the Cipher Text")
    choice2 = int(input())
    if choice2 == 1:
        print ("Enter the Cipher Text ?")
        cipher = str(input())
        print ("Enter the key for Decryption ?")
        key = int (input ())
        print ("The Cipher Text : " + cipher)
        print ("The Plain Text : " + DecryptKey(cipher, key))
    elif choice2 == 2:
        print ("Enter the Cipher Text ?")
        cipher = str(input())
        print("Brute Forcing Completed !")
        BruteForce(cipher)