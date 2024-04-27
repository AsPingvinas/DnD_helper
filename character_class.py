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
    def __init__(self, armor, weapons, saving_throws, equipment):
        self.armor = armor
        self.weapons = weapons
        self.saving_throws = saving_throws
        self.equipment = equipment

    @staticmethod
    def Cleric():
        armor_choice = input("Choose your armor (a) scale or (b) leather: ").lower()
        if armor_choice == "a":
            armor_class = "medium"
        elif armor_choice == "b":
            armor_class = "light"
        else:
            print("Invalid choice. Defaulting to leather armor.")
            armor_class = "light"

        mace = "mace"
        crossbow = "crossbow"
        pack_choice = input("Choose your pack (a) Priest's pack or (b) Explorer's pack: ").lower()
        if pack_choice == "a":
            pack = "Priest's pack"
        elif pack_choice == "b":
            pack = "Explorer's pack"
        else:
            print("Invalid choice. Defaulting to Priest's pack.")
            pack = "Priest's pack"

        shield = "shield"
        holy_symbol = "holy symbol"

        saving_throws = ["Wisdom", "Charisma"]

        return CharacterClassAttribute(
            armor=armor_class,
            weapons=[mace, crossbow],
            saving_throws=saving_throws,
            equipment=[pack, shield, holy_symbol]
        )

    @staticmethod
    def Fighter():
        armor_choice = input("Choose your armor (a) chain mail or (b) leather armor, longbow: ").lower()
        if armor_choice == "a":
            armor_class = "heavy"
            weapons = []
        elif armor_choice == "b":
            armor_class = "light"
            weapons = ["longbow"]
        else:
            print("Invalid choice. Defaulting to leather armor.")
            armor_class = "light"
            weapons = ["longbow"]

        weapon_choice = input(
            "Choose your weapon option (a) a martial weapon and a shield or (b) two martial weapons: ").lower()
        if weapon_choice == "a":
            weapons.extend(["martial weapon", "shield"])
        elif weapon_choice == "b":
            weapons.extend(["martial weapon", "martial weapon"])
        else:
            print("Invalid choice. Defaulting to option (a).")
            weapons.extend(["martial weapon", "shield"])

        ranged_choice = input(
            "Choose your ranged weapon option (a) a light crossbow or (b) two handaxes: ").lower()
        if ranged_choice == "a":
            weapons.extend(["light crossbow"])
        elif ranged_choice == "b":
            weapons.extend(["handaxe", "handaxe"])
        else:
            print("Invalid choice. Defaulting to option (a).")
            weapons.extend(["light crossbow"])

        pack_choice = input("Choose your pack option (a) a dungeoneer’s pack or (b) an explorer’s pack: ").lower()
        if pack_choice == "a":
            pack = "dungeoneer’s pack"
        elif pack_choice == "b":
            pack = "explorer’s pack"
        else:
            print("Invalid choice. Defaulting to option (a).")
            pack = "dungeoneer’s pack"

        saving_throws = ["Strength", "Constitution"]

        return CharacterClassAttribute(armor=armor_class, weapons=weapons, saving_throws=saving_throws,
                                       equipment=[pack])

    @staticmethod
    def Rogue():
        weapon_choice = input("Choose your weapon (a) rapier or (b) shortsword: ").lower()
        if weapon_choice == "a":
            weapon = "rapier"
        elif weapon_choice == "b":
            weapon = "shortsword"
        else:
            print("Invalid choice. Defaulting to shortsword.")
            weapon = "shortsword"

        ranged_choice = input(
            "Choose your ranged weapon (a) shortbow or (b) shortsword: ").lower()
        if ranged_choice == "a":
            ranged_weapon = ["shortbow"]
        elif ranged_choice == "b":
            ranged_weapon = ["shortsword"]
        else:
            print("Invalid choice. Defaulting to shortsword.")
            ranged_weapon = ["shortsword"]

        pack_choice = input(
            "Choose your pack (a) burglar’s pack, (b) dungeoneer’s pack, or (c) explorer’s pack: ").lower()
        if pack_choice == "a":
            pack = "burglar’s pack"
        elif pack_choice == "b":
            pack = "dungeoneer’s pack"
        elif pack_choice == "c":
            pack = "explorer’s pack"
        else:
            print("Invalid choice. Defaulting to burglar’s pack.")
            pack = "burglar’s pack"

        equipment = ["leather armor", "two daggers", "thieves’ tools"]

        saving_throws = ["Dexterity", "Intelligence"]

        return CharacterClassAttribute(saving_throws=saving_throws ,armor="light", weapons=[weapon] + ranged_weapon, equipment=equipment)

    @staticmethod
    def Wizard():
        weapon_choice = input("Choose your weapon (a) quarterstaff or (b) dagger: ").lower()
        if weapon_choice == "a":
            weapon = "quarterstaff"
        elif weapon_choice == "b":
            weapon = "dagger"
        else:
            print("Invalid choice. Defaulting to dagger.")
            weapon = "dagger"

        focus_choice = input("Choose your focus (a) component pouch or (b) arcane focus: ").lower()
        if focus_choice == "a":
            focus = "component pouch"
        elif focus_choice == "b":
            focus = "arcane focus"
        else:
            print("Invalid choice. Defaulting to component pouch.")
            focus = "component pouch"

        pack_choice = input("Choose your pack (a) scholar’s pack or (b) explorer’s pack: ").lower()
        if pack_choice == "a":
            pack = "scholar’s pack"
        elif pack_choice == "b":
            pack = "explorer’s pack"
        else:
            print("Invalid choice. Defaulting to scholar’s pack.")
            pack = "scholar’s pack"

        equipment = ["spellbook"]
        saving_throws = ["Intelligence", "Wisdom"]

        return CharacterClassAttribute(saving_throws=saving_throws,armor="none", weapons=[weapon], equipment=[focus, pack] + equipment)


