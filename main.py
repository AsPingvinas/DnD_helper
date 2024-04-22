from character_creator import create_character_file

while True:
    print("What would you like to do?")
    print("1. Make character")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        create_character_file()
    elif choice == "2":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter '1' to make a character or '2' to exit.\n")