def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

        else:
            result += char

    return result


def save_to_file(text):

    file = open("cipher_output.txt", "a")

    file.write(text + "\n")

    file.close()

    print("Saved to cipher_output.txt")


def brute_force(cipher):

    print("\nPossible Decryptions:\n")

    for shift in range(1, 26):

        plain = decrypt(cipher, shift)

        print("Shift", shift, ":", plain)



while True:

    print("\n====== Caesar Cipher Tool ======")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Brute Force Attack")
    print("4. Exit")

    choice = input("Enter choice: ")


    if choice == "1":

        text = input("Enter message: ")

        shift = int(input("Enter shift value: "))

        encrypted = encrypt(text, shift)

        print("\nEncrypted Text:", encrypted)

        print("Characters encrypted:", len(text))

        save = input("Save to file? (y/n): ")

        if save.lower() == "y":

            save_to_file("Encrypted: " + encrypted)



    elif choice == "2":

        text = input("Enter encrypted message: ")

        shift = int(input("Enter shift value: "))

        decrypted = decrypt(text, shift)

        print("\nDecrypted Text:", decrypted)

        save = input("Save to file? (y/n): ")

        if save.lower() == "y":

            save_to_file("Decrypted: " + decrypted)



    elif choice == "3":

        cipher = input("Enter encrypted text: ")

        brute_force(cipher)



    elif choice == "4":

        print("Exiting Program...")

        break


    else:

        print("Invalid Choice!")