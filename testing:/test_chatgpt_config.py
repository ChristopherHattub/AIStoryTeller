import unittest
from unittest.mock import patch
from src import chatgpt_config

class TestChatGPTConfig(unittest.TestCase):

    def setUp(self):
        # Mocking the environment variable for API key during tests
        self.mocked_api_key = "MOCKED_API_KEY"
    
    @patch.dict('os.environ', {'CHATGPT_API_KEY': 'MOCKED_API_KEY'})
    def test_api_key_loading(self):
        # Test if the API key is loaded correctly from environment variable
        loaded_api_key = chatgpt_config.get_api_key()
        self.assertEqual(loaded_api_key, self.mocked_api_key)
    
    @patch.dict('os.environ', {})
    def test_missing_api_key(self):
        # Test the behavior when API key is not set in the environment
        with self.assertRaises(Exception): 
            chatgpt_config.get_api_key()



if __name__ == '__main__':
    unittest.main()
