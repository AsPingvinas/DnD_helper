import random
import os
from enum import Enum
from race import Race

class CharacterClass(Enum):
    CLERIC = "Cleric"
    FIGHTER = "Fighter"
    ROGUE = "Rogue"
    WIZARD = "Wizard"

class Character:
    hit_die_map = {
        CharacterClass.CLERIC: 8,
        CharacterClass.FIGHTER: 10,
        CharacterClass.ROGUE: 8,
        CharacterClass.WIZARD: 6,
    }

    def __init__(self, name, race, character_class, size, speed):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = 1
        self.ability_scores = self.generate_ability_scores()
        self.hit_points = self.generate_hit_points()
        self.size = size
        self.speed = speed

    def generate_ability_scores(self):
        ability_scores = {
            'Strength': random.randint(1, 18),
            'Dexterity': random.randint(1, 18),
            'Constitution': random.randint(1, 18),
            'Intelligence': random.randint(1, 18),
            'Wisdom': random.randint(1, 18),
            'Charisma': random.randint(1, 18)
        }
        return ability_scores

    def generate_hit_points(self):
        hit_die = self.hit_die_map[self.character_class]
        constitution = self.ability_scores['Constitution']
        hp = random.randint(1, hit_die)
        return hp + constitution

class RaceAttribute(Character):
    @staticmethod
    def Human(ability_scores):
        speed = "Base walking speed is 30 feet"
        size = "Medium"
        for ability in ability_scores:
            ability_scores[ability] += 1
        traits = {
            "Extra language\n"
        }
        return ability_scores, size, speed, traits

    @staticmethod
    def Elf(ability_scores):
        speed = "Base walking speed is 30 feet"
        size = "Medium"
        ability_scores['Dexterity'] += 2
        traits = {
            "Darkvision\n"
            "Keen Senses\n"
            "Fey Ancestry\n"
            "Trance\n"
        }
        return ability_scores, size, speed, traits
    @staticmethod
    def Dwarf(ability_scores):
        speed = "Base walking speed is 25 feet"
        size = "Medium"
        ability_scores['Constitution'] += 2
        traits = {
            "Darkvision\n"
            "Dwarven resilience\n"
            "Dwarven combat training\n"
            "Stonecunning\n"
        }
        return ability_scores, size, speed, traits

    @staticmethod
    def Halfling(ability_scores):
        speed = "Base walking speed is 25 feet"
        size = "Small"
        ability_scores['Dexterity'] += 2
        traits = {
            "Lucky\n"
            "Brave\n"
            "Halfling nimbleness\n"
        }
        return ability_scores, size, speed, traits

    @staticmethod
    def Dragonborn(ability_scores):
        speed = "Base walking speed is 30 feet"
        size = "Medium"
        ability_scores['Strength'] += 2
        ability_scores['Charisma'] += 1
        traits = {
            "Draconic ancestry\n"
            "Breath weapon\n"
            "Damage resistance\n"
        }
        return ability_scores, size, speed, traits

    @staticmethod
    def Gnome(ability_scores):
        speed = "Base walking speed is 25 feet"
        size = "Small"
        ability_scores['Intelligence'] += 2
        traits = {
            "Darkvision\n"
            "Gnome Cunning\n"
        }
        return ability_scores, size, speed, traits

    @staticmethod
    def Half_elf(ability_scores):
        speed = "Base walking speed is 30 feet"
        size = "Medium"
        ability_scores['Charisma'] += 2
        traits = {
            "Darkvision\n"
            "Fey ancestry\n"
            "Skill versatility\n"
        }
        return ability_scores, size, speed, traits

    @staticmethod
    def Half_orc(ability_scores):
        speed = "Base walking speed is 30 feet"
        size = "Medium"
        ability_scores['Strength'] += 2
        ability_scores['Constitution'] += 1
        traits = {
            "Darkvision\n"
            "Menacing\n"
            "Relentless endurance\n"
            "Savage attacks\n"
        }
        return ability_scores, size, speed, traits

    @staticmethod
    def Tiefling(ability_scores):
        speed = "Base walking speed is 30 feet"
        size = "Medium"
        ability_scores['Charisma'] += 2
        ability_scores['Intelligence'] += 1
        traits = {
            "Darkvision\n"
            "Hellish resistance\n"
            "Infernal legacy\n"
        }
        return ability_scores, size, speed, traits

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
    character_info += "Traits:\n"
    for trait in traits:
        character_info += f"{trait}\n"

    folder_path = "characters"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_name = os.path.join(folder_path, f"{character_name}_character.txt")
    with open(file_name, "w") as file:
        file.write(character_info)
    print(f"Character '{character_name}' saved to {file_name}")

create_character_file()
