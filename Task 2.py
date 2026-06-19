import random
import string
import getpass


def check_password(password):

    upper = False
    lower = False
    digit = False
    special = False

    for ch in password:

        if ch.isupper():
            upper = True

        elif ch.islower():
            lower = True

        elif ch.isdigit():
            digit = True

        else:
            special = True


    score = 0

    if len(password) >= 8:
        score += 1

    if upper:
        score += 1

    if lower:
        score += 1

    if digit:
        score += 1

    if special:
        score += 1


    print("\n------ Password Report ------")

    print("Length:", len(password))
    print("Uppercase:", upper)
    print("Lowercase:", lower)
    print("Numbers:", digit)
    print("Special Characters:", special)


    if score <= 2:

        print("\nPassword Strength: Weak ❌")

    elif score <= 4:

        print("\nPassword Strength: Medium ⚠️")

    else:

        print("\nPassword Strength: Strong ✅")


    print("\nSuggestions:")

    if len(password) < 8:
        print("- Increase password length to at least 8 characters")

    if not upper:
        print("- Add uppercase letters")

    if not lower:
        print("- Add lowercase letters")

    if not digit:
        print("- Add numbers")

    if not special:
        print("- Add special characters")


def generate_password(length=12):

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for i in range(length):

        password += random.choice(characters)

    return password



while True:

    print("\n====== Password Strength Checker ======")

    print("1. Check Password")
    print("2. Generate Strong Password")
    print("3. Exit")


    choice = input("Enter choice: ")


    if choice == "1":

        password = getpass.getpass("Enter Password: ")

        check_password(password)


    elif choice == "2":

        strong_pass = generate_password()

        print("\nGenerated Password:")

        print(strong_pass)


    elif choice == "3":

        print("Thank You!")

        break


    else:

        print("Invalid Choice")