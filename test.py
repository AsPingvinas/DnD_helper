import unittest
from unittest.mock import patch
import os
from io import StringIO
import json

from character_creator import create_character_file
from race import Race

class TestCharacterCreation(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_character_file(self, mock_stdout):
        user_inputs = ["Test Character", "1", "1", "a", "a"]

        with patch('builtins.input', side_effect=user_inputs):
            create_character_file()

        file_path = "characters/Test Character_character.json"
        self.assertTrue(os.path.exists(file_path))

        with open(file_path, "r") as file:
            character_info = json.load(file)

        expected_keys = ["Name", "Race", "Class", "Level", "Ability Scores", "Hit Points", "Size", "Speed", "Class Attributes"]
        for key in expected_keys:
            self.assertIn(key, character_info)

    @patch('builtins.input', side_effect=["2"])
    def test_character_editor_main(self, mock_input):
        pass

    def test_race_attributes(self):
        # Test each race's attributes
        human_attributes = Race.HUMAN.value
        self.assertEqual(human_attributes, "Human")

        elf_attributes = Race.ELF.value
        self.assertEqual(elf_attributes, "Elf")

    def test_character_class_attributes(self):
        pass

    def test_invalid_input_handling(self):
        user_inputs = ["Invalid Character", "10", "10", "z", "z"]

        with patch('builtins.input', side_effect=user_inputs):
            create_character_file()

        file_path = "characters/Invalid Character_character.json"
        self.assertFalse(os.path.exists(file_path))

    def test_file_content(self):
        user_inputs = ["Test Character", "1", "1", "a", "a"]

        with patch('builtins.input', side_effect=user_inputs):
            create_character_file()

        file_path = "characters/Test Character_character.json"
        with open(file_path, "r") as file:
            character_info = json.load(file)


    def test_character_creation_failure(self):
        pass

if __name__ == '__main__':
    unittest.main()
#PASITIKEKIT KODAS VEIKIA ALL GOOD