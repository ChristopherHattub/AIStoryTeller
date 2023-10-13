import unittest
from unittest.mock import patch, Mock
from src import api_handler

class TestApiHandler(unittest.TestCase):

    def setUp(self):
        # Sample mocked data for the tests
        self.sample_request_payload = {"prompt": "test prompt", "max_tokens": 50}
        self.sample_response_data = {"choices": [{"text": "test response"}]}

    @patch('src.api_handler.requests.post')
    def test_send_request(self, mock_post):
        # Mocking the API response
        mock_response = Mock()
        mock_response.json.return_value = self.sample_response_data
        mock_post.return_value = mock_response

       
        response = api_handler.send_request(self.sample_request_payload)
        self.assertEqual(response, self.sample_response_data)

        # Ensure the API was called with correct URL and data
        mock_post.assert_called_with(api_handler.API_ENDPOINT, json=self.sample_request_payload)

    @patch('src.api_handler.requests.post')
    def test_process_response(self, mock_post):
        # Mocking the API response
        mock_response = Mock()
        mock_response.json.return_value = self.sample_response_data
        mock_post.return_value = mock_response

        
        processed_data = api_handler.process_response(mock_response)
        
        # TODO: Add assertions based on how process_response is supposed to work. 
        # For now, just checking if it extracts text from the response:
        self.assertEqual(processed_data, "test response")


if __name__ == '__main__':
    unittest.main()
