# DnD_helper


## Introduction

### What is the application

<p>This is my coursework project for university. I had to follow the man 4 OOP pillars and had to use 2 diffrent design patters. Of course the results will be covered and analysed with diffrent levels of succssess.</p>

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

#### Encapsulation/Abstraction

<p>Encapsulation is a principle that seeks to hide the implementation details of objects from the outside world. It states that all important information is contained within the object; only selected data is available externally. </p>

<p>In my case, the "Character" class best shows the case of encapsulation. Most of the information is contained in itself however the ability for child classes (RaceAttribute from race.py) to use the ability score attribute which is overriden. </p>

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

```python
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
<p>Abstraction refers to the concept of hiding the complex implementation details and showing only the necessary features of an object. In the provided code, abstraction is evident in various aspects
<ul>
    <li>The RaceAttribute and CharacterClassAttribute classes abstract away the specific implementations of racial and class attributes, respectively. They provide a clean interface for accessing and manipulating these attributes without exposing the underlying complexity.</li>
    <li>The Character class abstracts away details about a character, providing a high-level representation of a character's properties (name, race, class, etc.) without exposing the internal implementation details.</li>
</ul>
</p>

#### Inheritance/Polymorphism

<p>Inheritance is </p>


<p>For my program and it's porpuses, inheritance and polymorhpism had very similar uses/meanings. Inhiretance helps developers create classes based on existing classes, and polymorphism is essentially an extension to inheritance, that allows for sub-classes to use mehods of the same name, but with diffrent/similar functionality. In my coursework I didn't find the need to use polymorphism, because my program is one giant factory. My program builds characters witht the use of diffrent methods, and if diffrent methods had the same name, but diffrent functiionality, it would make for confusing, dificult and unreadable code. For my purposes simple inheritance helped fulfill my needs.  </p>

<p>For example, if I implemented a featre to my program that can calculate damage, then polymorphism would be useful since every character class has a diffrent type of armour (same name,difrent usage). </p>

<p>I had an oopurtunity to use inheritance in the "character_class.py" file like this: </p>

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

<p>However I didn't use inheritance becasuse while , there are multiple choices on what items a character class will have. If I were to use inheritance, there would have been too many diffrent classes and methods which would have been difficult to keep track of. But I did use inheritamce with character races: </p>

```python
class RaceAttribute(Character):
    @staticmethod
    def Human(ability_scores):
        # Method implementation...
    
    @staticmethod
    def Elf(ability_scores):
        # Method implementation...
```

<p>Charcter races are diffrent than character classes, because races have defined stats and characteristics that are following the rules and are always the same. There are no choices with character races. So inheritace here was very convienient and simple. In the end the RaceAttribute class adds existing functionality to an already existing class (Character). </p>


### Design patterns

#### Factory method pattern

<p>A factory method pattern provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.</p>

<p>My entire program is designed around this specific design patter. I have diffrent Race attributes/Class attributes which end up buiding a whole playable character. </p>

```def create_character_file():
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

    ..........................................................

    ability_scores, size, speed, traits = race_attributes_map.get(race)(ability_scores)

    ..........................................................

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
```
<p>This function uses diffrent class methods assemble a character.</p>
<p>We can say that this is smi</p>

#### Singleton

<p>This design pattern isn't explicity implimented, however the "main.py" file works as a main menu and as a single accssess point to all of the other files.</p>
<p>By definition a singleton Lets you ensure that a class has only one instance, while providing a global access point to this instance. From my experiene singletons are useful in game dev for finding when objects collide with the player.Of course my singleton implementation in this project isn't the same with the definition, but is reminicent. </p>
##Results

##Results

<ul>
    <li>It was difficult to find a use for the "Polymorphism" pillar for my pogram</li>
    <li>Missed oppurtunity to use inheritance with teh  CharacterClass </li>
    <li>It was challenging to figure out the file reading/editing system</li>
</ul>

## Conclusion

<p>Overall, the program ended up not too bad, it works as intended and quite well. In the future I can add live healthbar, XP meter, UI and even more character classes. This was my very first bigger program that serves a purpose, I found using OOP priciples quite intersting. The whole concept of classes and their own methods is interesting. I learned alot making this program altho it isn't perfect and there is alot of room for inprovement.</p>

### Notes

<p>While making the program I made the mistake of not writing any unittests. In the end I ended up brute-forcing the test myself which made the project slower and more time consuming. After writing all of the final code, unittest were difficult to write. </p>

### References

<p>https://career.softserveinc.com/en-us/stories/what-is-object-oriented-programming-oop-explaining-four-major-principles</p>
<p>https://refactoring.guru/design-patterns/python</p>

