import unittest
from unittest.mock import patch
import os
from io import StringIO
import json
from enum import Enum

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

        # Additional test for file content
        with open(file_path, "r") as file:
            character_info = json.load(file)

        expected_keys = ["Name", "Race", "Class", "Level", "Ability Scores", "Hit Points", "Size", "Speed", "Class Attributes"]
        for key in expected_keys:
            self.assertIn(key, character_info)

        # You can add more specific checks for the content of character_info if needed


    @patch('builtins.input', side_effect=["2"])  # Simulate choosing to edit a character
    def test_character_editor_main(self, mock_input):
        # Since the character_editor_main function is calling another function,
        # it's better to test its functionality in integration tests.
        pass

    def test_race_attributes(self):
        # Test each race's attributes
        human_attributes = Race.HUMAN.value
        self.assertEqual(human_attributes, "Human")

        # Add similar assertions for other race attributes

    def test_character_class_attributes(self):
        # Test character class attributes for each class
        pass

    def test_invalid_input_handling(self):
        # Test how the system handles invalid inputs
        user_inputs = ["Invalid Character", "10", "10", "z", "z"]

        with patch('builtins.input', side_effect=user_inputs):
            create_character_file()

        # Ensure that the character file is not created
        file_path = "characters/Invalid Character_character.json"
        self.assertFalse(os.path.exists(file_path))

        # You can also check the output to verify that the system informs the user about the invalid inputs
