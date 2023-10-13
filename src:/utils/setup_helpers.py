import json

def load_story_elements():
    """
    Load story elements from the JSON file into memory for the game's usage.
    """
    with open("story_elements.json", "r") as file:
        story_elements = json.load(file)
    return story_elements

def setup_game():
    """
    Initialize game-specific settings or initial configurations.
    """
    # Load story elements
    story_elements = load_story_elements()
    
    # TODO add player history, start page expanded

    
    print("Welcome to AIStoryTeller")
    print("Loading story elements and preparing the game...")

    return story_elements

if __name__ == "__main__":
    # Testing
    setup_game()
