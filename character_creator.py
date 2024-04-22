import os
import json
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

    character_info = {
        "Name": character.name,
        "Race": character.race.value,
        "Class": character.character_class.value,
        "Level": character.level,
        "Ability Scores": ability_scores,
        "Hit Points": character.hit_points,
        "Size": character.size,
        "Speed": character.speed,
        "Class Attributes": {
            "Armor": class_attributes.armor,
            "Weapons": class_attributes.weapons,
            "Saving Throws": class_attributes.saving_throws,
            "Equipment": class_attributes.equipment
        }
    }

    folder_path = "characters"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_name = os.path.join(folder_path, f"{character_name}_character.json")
    with open(file_name, "w") as file:
        json.dump(character_info, file, indent=4)
    print(f"Character '{character_name}' saved to {file_name}")

create_character_file()
