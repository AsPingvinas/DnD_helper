from enum import Enum
class Race(Enum):
    DRAGONBORN = "Dragonborn"
    DWARF = "Dwarf"
    ELF = "Elf"
    GNOME = "Gnome"
    HALF_ELF = "Half-Elf"
    HALFLING = "Halfling"
    HALF_ORC = "Half-Orc"
    HUMAN = "Human"
    TIEFLING = "Tiefling"

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
