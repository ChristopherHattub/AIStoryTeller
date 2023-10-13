import unittest
from unittest.mock import patch, Mock
from src import story_engine

class TestStoryEngine(unittest.TestCase):

    def setUp(self):
        # Sample data or state for the tests
        self.sample_scenario = {
            "setting": "Medieval Castle",
            "situation": "You are approached by a knight.",
            "problem": "He challenges you to a duel. What do you do?"
        }
    
    def test_generate_scenario(self):
       
        scenario = story_engine.generate_scenario()
        
        # Check if scenario was generated correctly
        for key in self.sample_scenario:
            self.assertIn(key, scenario)

    @patch('src.story_engine.get_choices_from_chatgpt')
    def test_generate_choices(self, mock_get_choices):
        # Mocking the ChatGPT choice response
        mock_choices = ["Accept the challenge", "Decline politely", "Run away"]
        mock_get_choices.return_value = mock_choices

      
        choices = story_engine.generate_choices(self.sample_scenario)
        
        self.assertEqual(choices, mock_choices)

    def test_handle_player_choice(self):
        
        response = story_engine.handle_player_choice(self.sample_scenario, "Accept the challenge")
        
        # Sample assertions based on what you expect. Checking for a non-empty response.
        self.assertTrue(response)


if __name__ == '__main__':
    unittest.main()
