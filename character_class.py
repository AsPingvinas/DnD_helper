import random
from enum import Enum

class CharacterClass(Enum):
    CLERIC = "Cleric"
    FIGHTER = "Fighter"
    ROGUE = "Rogue"
    WIZARD = "Wizard"

class Hit_die:
    hit_die_map = {
        CharacterClass.CLERIC: 8,
        CharacterClass.FIGHTER: 10,
        CharacterClass.ROGUE: 8,
        CharacterClass.WIZARD: 6,
    }

class CharacterClassAttribute:
    @staticmethod
    def Cleric():
        pass
