from character_creator import create_character_file
from character_editor import main as character_editor_main

class Menu:
    def main(self):
        while True:
            print("What would you like to do?")
            print("1. Create a character")
            print("2. Edit a character")
            print("3. Exit the program")
            choice = input("Enter your choice: ")

            if choice == "1":
                create_character_file()
            elif choice == "2":
                character_editor_main()
            elif choice == "3":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter '1' to create a character, '2' to edit a character, or '3' to exit.\n")

if __name__ == "__main__":
    start = Menu()
    start.main()

#Test