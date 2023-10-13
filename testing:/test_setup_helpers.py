import unittest
from src import setup_helpers

class TestSetupHelpers(unittest.TestCase):

    def setUp(self):
        # Sample data or state for the tests
        self.sample_character_name = "Alex"
    
    def test_create_character(self):
       
        character = setup_helpers.create_character(self.sample_character_name)
        
        # Check if character was created correctly
        self.assertEqual(character.name, self.sample_character_name)

    def test_validate_character_name(self):
       
        self.assertTrue(setup_helpers.validate_character_name(self.sample_character_name))

        # Test invalid names
        self.assertFalse(setup_helpers.validate_character_name(""))
        self.assertFalse(setup_helpers.validate_character_name("A"*101))  # Assuming a max length of 100 for names
    
    def test_initial_setup(self):
        
        game_state = setup_helpers.initial_setup()
        
     
        self.assertIsNotNone(game_state.character)
        self.assertEqual(game_state.story_progress, 0)

        



if __name__ == '__main__':
    unittest.main()
