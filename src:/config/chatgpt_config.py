import os

# Default configuration settings
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
API_KEY = os.environ.get("CHATGPT_API_KEY")  

def load_config():
    """
    Load the ChatGPT configuration from environment variables or other sources if needed.
    """
    global API_ENDPOINT, API_KEY

    # Check if environment variables are set and override default configurations
    if "CHATGPT_API_ENDPOINT" in os.environ:
        API_ENDPOINT = os.environ["CHATGPT_API_ENDPOINT"]

    if "CHATGPT_API_KEY" in os.environ:
        API_KEY = os.environ["CHATGPT_API_KEY"]


    # Validate that the configurations are set correctly
    if not API_KEY or not API_ENDPOINT:
        raise ValueError("ChatGPT configurations are not set properly. Ensure API_KEY and API_ENDPOINT are provided.")

if __name__ == "__main__":
    # Testing
    load_config()
    print(f"API Endpoint: {API_ENDPOINT}")
    print(f"API Key: {API_KEY}")
