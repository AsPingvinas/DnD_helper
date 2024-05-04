# DnD_helper


## Introduction

### What is the application

<p>"Dungeon's and dragons" is a role playing game where players use their imagination to create character's and defeat medievel/futuristic and fantasy themed campaigns.
So the goal of my coursework was to make a simplified "Dungeon's and dragon's" character sheet creator, which can also edit the inventory, level up and edit stats of character's.</p>

<p>I tried to follow the official rulebook as best as possible while at the same not overcomplicating the program. This program is most useful to begginer's of the game, because most of the information is very nieche and not needed for first time player's.
The game has a variety of character races to choose from and all races have specific abbilities that help them in the game. I'll use the "Dragonborn" race as an example, in the official rulebook their are about 8 diffrent variations of the "Dragornborn" and for new players
these varietys are very confusing and would overwhelm new players. So I have chosen to keep the key features of a race to keep the game begginer friendly while also still keeping ther characters competitive.</p>

### How to run the program

<p>To run the program we open the "main.py" file using a program that is able to run pythn code. Some examples are "Microsoft visual code" and "PyCharm"</p>

### How to use the program

<p>The program will prompt us to either create a character or to edit a chasracter. Assuming it's the first time we are the program, we choose the create a new character. The program will prompt us to choose a name, race,
class and items that come with the specif class we have chosen.</p>

<p>Then we can choose to edit a character that we have just created. There are options to add/remove equipment/weapons in our inventory as well as level up. When leveling up, we a choice to put 2 skill points into 1 stat or 1 skill point into 2 diffrent stats.
There is also an option to display everything about our character.</p>

## Body/Analysis

### The main OOP pillars

#### Encapsulation

```python
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
```
``` python
class CharacterClassAttribute:
    def __init__(self, armor, weapons, saving_throws, equipment):
        self.armor = armor  
        self.weapons = weapons 
        self.saving_throws = saving_throws 
        self.equipment = equipment 

    # Other methods...

```

### Polymorphism

<p>I had an oopurtunity to use polymorphism in the "character_class.py" file like this: </p>

```python
class CharacterClassAttribute:
    # Method definitions...
    
class Cleric(CharacterClassAttribute):
    @staticmethod
    def Cleric():
        # Method implementation...
    
class Fighter(CharacterClassAttribute):
    @staticmethod
    def Fighter():
        # Method implementation...
```

<p>However I didn't use inheritance becasuse while building a character, there are multiple choices on what items a character class will have. If I were to use poymorphism, there would have been too many diffrent classes and methods which would have been difficult to keep track of. But I did use polymorphism with character races</p>

```python
class RaceAttribute(Character):
    @staticmethod
    def Human(ability_scores):
        # Method implementation...
    
    @staticmethod
    def Elf(ability_scores):
        # Method implementation...
```

<p>Charcter races are diffrent than character classes, because races have defined stats and characteristics that are following the rules and are always the same. There are no choices with character races. So polymorphism here was very convienient and simple.</p>

### Design patterns

#### DP1

#### DP2

##Results

## Conclusion


