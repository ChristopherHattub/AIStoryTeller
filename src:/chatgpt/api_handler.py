import requests
import os


# Constants
BASE_URL = "https://api.openai.com/v1/completions" 
API_KEY = os.environ.get("CHATGPT_API_KEY")  
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

        response = requests.post(BASE_URL, headers=HEADERS, json=payload)
        
        if response.status_code == 200:
            return response.json().get("choices", [{}])[0].get("text", "").strip()
        else:
            # TODO more error handling
            return None

    @staticmethod
    def generate_scenario(prompt_text):
        """Generate a story scenario based on the given prompt."""
        return APIHandler._send_request(prompt_text)

    @staticmethod
    def generate_choices(prompt_text):
        """Generate player choices based on the given prompt."""
        return APIHandler._send_request(prompt_text)


# Testing the API Handler
if __name__ == "__main__":
    scenario = APIHandler.generate_scenario("In a medieval setting, a knight named Arthur encounters...")
    print(scenario)

    choice = APIHandler.generate_choices("What should Arthur do when he sees the dragon?")
    print(choice)
