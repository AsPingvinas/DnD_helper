import random
from character_class import Hit_die
class Character:
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
        hit_die = Hit_die.hit_die_map[self.character_class]
        constitution = self.ability_scores['Constitution']
        hp = random.randint(1, hit_die)
        return hp + constitution
