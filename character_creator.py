import os
from race import Race, RaceAttribute
from character import Character
from character_class import CharacterClass, CharacterClassAttribute

def create_character_file():
    character_name = input("Enter your character's name: ")
    print("Choose your character's race:")
    for idx, char_race in enumerate(Race, start=1):
        print(f"{idx}. {char_race.value}")
    race_choice = int(input("Enter the number corresponding to your choice: "))
    race = list(Race)[race_choice - 1]

    print("Choose a character class:")
    for idx, char_class in enumerate(CharacterClass, start=1):
        print(f"{idx}. {char_class.value}")
    class_choice = int(input("Enter the number corresponding to your choice: "))
    character_class = list(CharacterClass)[class_choice - 1]

    ability_scores = Character.generate_ability_scores(None)

    race_attributes_map = {
        Race.HUMAN: RaceAttribute.Human,
        Race.ELF: RaceAttribute.Elf,
        Race.DWARF: RaceAttribute.Dwarf,
        Race.HALFLING: RaceAttribute.Halfling,
        Race.DRAGONBORN: RaceAttribute.Dragonborn,
        Race.GNOME: RaceAttribute.Gnome,
        Race.HALF_ELF: RaceAttribute.Half_elf,
        Race.HALF_ORC: RaceAttribute.Half_orc,
        Race.TIEFLING: RaceAttribute.Tiefling
    }

    ability_scores, size, speed, traits = race_attributes_map.get(race)(ability_scores)

    character_class_attributes_map = {
        CharacterClass.CLERIC: CharacterClassAttribute.Cleric,
        CharacterClass.FIGHTER: CharacterClassAttribute.Fighter,
        CharacterClass.ROGUE: CharacterClassAttribute.Rogue,
        CharacterClass.WIZARD: CharacterClassAttribute.Wizard
    }

    class_attributes = character_class_attributes_map.get(character_class)()

    character = Character(character_name, race, character_class, size, speed)

    character_info = f"Name: {character.name}\n"
    character_info += f"Race: {character.race.value}\n"
    character_info += f"Class: {character.character_class.value}\n"
    character_info += f"Level: {character.level}\n"
    character_info += "Ability Scores:\n"
    for ability, score in ability_scores.items():
        character_info += f"{ability}: {score}\n"
    character_info += f"Hit Points: {character.hit_points}\n"
    character_info += f"Size: {character.size}\n"
    character_info += f"Speed: {character.speed}\n"
    character_info += "Class Attributes:\n"
    character_info += f"Armor: {class_attributes.armor}\n"
    character_info += f"Weapons: {', '.join(class_attributes.weapons)}\n"
    character_info += f"Saving Throws: {', '.join(class_attributes.saving_throws)}\n"
    character_info += f"Equipment: {', '.join(class_attributes.equipment)}\n"

    folder_path = "characters"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_name = os.path.join(folder_path, f"{character_name}_character.txt")
    with open(file_name, "w") as file:
        file.write(character_info)
    print(f"Character '{character_name}' saved to {file_name}")

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
        print("Invalid choice. Please enter '1' to make a character or '2' to exit.")
