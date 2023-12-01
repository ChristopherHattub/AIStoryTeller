import requests
import os
from config.chatgpt_config import load_config, API_ENDPOINT

# Load configurations
load_config()

# Constants
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "User-Agent": "StoryTeller/1.0" 
}

class APIHandler:
    @staticmethod
    def _send_request(prompt_text):
        """Send a POST request to ChatGPT API with the given prompt text."""
        payload = {
            "prompt": prompt_text,
            "max_tokens": 150  # prompt length
        }

        response = requests.post(API_ENDPOINT, headers=HEADERS, json=payload)
        
        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("text", "").strip()
        else:
            # TODO: Add more robust error handling
            return None

    @staticmethod
    def generate_scenario(prompt_text):
        """Generate a story scenario based on the given prompt."""
        return APIHandler._send_request(prompt_text)
