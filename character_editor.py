import os
import json

class CharacterEditor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.character = self.load_character()

    def load_character(self):
        with open(self.file_path, "r") as file:
            character_info = json.load(file)
        return character_info

    def edit_equipment(self):
        print("Current Equipment:", self.character["Class Attributes"]["Equipment"])
        action = input("Enter 'A' to add an item, 'R' to remove an item, or 'C' to cancel: ").upper()
        if action == 'A':
            new_item = input("Enter the new item: ")
            self.character["Class Attributes"]["Equipment"].append(new_item)
        elif action == 'R':
            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in self.character["Class Attributes"]["Equipment"]:
                self.character["Class Attributes"]["Equipment"].remove(item_to_remove)
            else:
                print("Item not found in equipment.")
        elif action == 'C':
            return
        else:
            print("Invalid action.")

    def edit_weapons(self):
        print("Current Weapons:", self.character["Class Attributes"]["Weapons"])
        action = input("Enter 'A' to add a weapon, 'R' to remove a weapon, or 'C' to cancel: ").upper()
        if action == 'A':
            new_weapon = input("Enter the new weapon: ")
            self.character["Class Attributes"]["Weapons"].append(new_weapon)
        elif action == 'R':
            weapon_to_remove = input("Enter the weapon to remove: ")
            if weapon_to_remove in self.character["Class Attributes"]["Weapons"]:
                self.character["Class Attributes"]["Weapons"].remove(weapon_to_remove)
            else:
                print("Weapon not found.")
        elif action == 'C':
            return
        else:
            print("Invalid action.")

    def edit_level(self):
        new_level = int(input("Enter new level: "))
        self.character["Level"] = new_level

    def edit_ability_scores(self):
        new_ability_scores = input("Enter new ability scores (in JSON format): ")
        self.character["Ability Scores"] = json.loads(new_ability_scores)

    def save_character(self):
        with open(self.file_path, "w") as file:
            json.dump(self.character, file, indent=4)

# Example usage:
def main():
    character_name = input("Enter the character's name: ")
    file_name = f"{character_name}_character.json"
    file_path = os.path.join("characters", file_name)

    if os.path.exists(file_path):
        editor = CharacterEditor(file_path)

        while True:
            print("\nChoose what to edit:")
            print("1. Equipment")
            print("2. Weapons")
            print("3. Level")
            print("4. Ability Scores")
            print("5. Save and Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                editor.edit_equipment()
            elif choice == '2':
                editor.edit_weapons()
            elif choice == '3':
                editor.edit_level()
            elif choice == '4':
                editor.edit_ability_scores()
            elif choice == '5':
                editor.save_character()
                print(f"Character '{character_name}' updated successfully!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    else:
        print("Character file does not exist.")

if __name__ == "__main__":
    main()
