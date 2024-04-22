import os
import json
from character import Character

class CharacterEditor:
    ability_mapping = {
        "STR": "Strength",
        "DEX": "Dexterity",
        "CON": "Constitution",
        "INT": "Intelligence",
        "WIS": "Wisdom",
        "CHA": "Charisma"
    }

    def __init__(self, file_path):
        self.file_path = file_path
        self.character = self.load_character()

    def load_character(self):
        with open(self.file_path, "r") as file:
            character_info = json.load(file)
        return character_info

    def edit_ability_scores(self):
        print("Current Ability Scores:", self.character["Ability Scores"])
        for _ in range(2):
            ability = input("Enter ability to increase (e.g., STR, DEX, CON, INT, WIS, CHA): ").upper()
            full_ability = self.ability_mapping.get(ability)
            if full_ability:
                try:
                    increase_by = int(input("Enter the amount to increase by: "))
                    self.character["Ability Scores"][full_ability] += increase_by
                except ValueError:
                    print("Please enter a valid integer for the amount to increase by.")
            else:
                print("Invalid ability.")

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

    def level_up(self):
        if self.character["Level"] < 20:
            self.character["Level"] += 1
            print("Level Up!")
            print("You gained 2 points to allocate to ability scores.")
            self.allocate_ability_scores()
        else:
            print("You are already at the maximum level (20).")

    def allocate_ability_scores(self):
        valid_abilities = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        print("Current Ability Scores:", self.character["Ability Scores"])

        remaining_points = 2
        for _ in range(2):
            if remaining_points == 0:
                break

            ability = input("Enter ability to increase (e.g., STR, DEX, CON, INT, WIS, CHA): ").upper()
            full_ability = self.ability_mapping.get(ability)
            if full_ability:
                try:
                    current_score = self.character["Ability Scores"][full_ability]
                    increase_by = min(int(input(f"Enter the amount to increase by (up to {20 - current_score}): ")),
                                      remaining_points, 20 - current_score)
                    if current_score + increase_by > 20:
                        print(f"The {full_ability} score cannot exceed 20.")
                        continue
                    self.character["Ability Scores"][full_ability] += increase_by
                    remaining_points -= increase_by
                except ValueError:
                    print("Please enter a valid integer for the amount to increase by.")
            else:
                print("Invalid ability.")

    def save_character(self):
        with open(self.file_path, "w") as file:
            json.dump(self.character, file, indent=4)

def main():
    character_name = input("Enter the character's name: ")
    file_name = f"{character_name}_character.json"
    file_path = os.path.join("characters", file_name)

    if os.path.exists(file_path):
        editor = CharacterEditor(file_path)

        while True:
            print("\nChoose what to do:")
            print("1. Edit Equipment")
            print("2. Edit Weapons")
            print("3. Level Up")
            print("4. Edit Ability Scores")
            print("5. Save and Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                editor.edit_equipment()
            elif choice == '2':
                editor.edit_weapons()
            elif choice == '3':
                editor.level_up()
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
