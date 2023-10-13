import unittest
from unittest.mock import patch
from src import interface

class TestInterface(unittest.TestCase):

    def setUp(self):
        # Set up a dummy environment for the tests. 
        self.game_state = {
            "character_name": "TestChar",
            "current_scenario": "You are in a forest.",
            "choices": ["Go left", "Go right", "Go back"]
        }

    def test_display_character_name(self):
        displayed_name = interface.display_character_name(self.game_state["character_name"])
        self.assertEqual(displayed_name, "TestChar")
    
    @patch('src.interface.input', return_value='1')
    def test_capture_player_choice(self, input_mock):
       
        choice = interface.capture_player_choice(self.game_state["choices"])
        self.assertEqual(choice, "Go left")

    def test_display_scenario(self):
       
        displayed_scenario = interface.display_scenario(self.game_state["current_scenario"])
        self.assertEqual(displayed_scenario, "You are in a forest.")
    
    def test_display_choices(self):
    
        displayed_choices = interface.display_choices(self.game_state["choices"])
        self.assertListEqual(displayed_choices, ["Go left", "Go right", "Go back"])

if __name__ == '__main__':
    unittest.main()
