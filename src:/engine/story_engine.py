import json
from chatgpt.api_handler import APIHandler
import random

# Load the story elements from the database (JSON file).
with open("database/story_elements.json", "r") as file:
    STORY_ELEMENTS = json.load(file)


class StoryEngine:

    @staticmethod
    def _select_random_element(element_type):
        """Select a random story element from the given type."""
        return random.choice(STORY_ELEMENTS[element_type])

    @staticmethod
    def generate_scenario():
        """Generate a random story scenario."""
        time_period = StoryEngine._select_random_element("timePeriod")
        class_role = StoryEngine._select_random_element("classRole")
        story_event = StoryEngine._select_random_element("storyEvents")

        # Create a prompt for ChatGPT based on the selected elements.
        prompt_text = f"In the {time_period['name']} era, a {class_role['name']} encounters {story_event['description']}..."
        
        # Get the scenario continuation from ChatGPT.
        scenario_continuation = APIHandler.generate_scenario(prompt_text)
        
        return f"{prompt_text} {scenario_continuation}"

    @staticmethod
    def generate_choices(scenario):
        """Generate player choices based on the given scenario."""
        prompt_text = f"What should the protagonist do next after {scenario}?"
        
        # Get possible choices from ChatGPT
        # TODO expand for multiple choices
        choice = APIHandler.generate_choices(prompt_text)
        
        return [choice]

    @staticmethod
    def generate_reaction(choice):
        """Generate the outcome or reaction after a player's choice."""
        prompt_text = f"Given that the protagonist chose to {choice}, what happens next?"
        
        return APIHandler.generate_scenario(prompt_text)


# Testing the Story Engine
if __name__ == "__main__":
    scenario = StoryEngine.generate_scenario()
    print(f"Scenario: {scenario}")

    choices = StoryEngine.generate_choices(scenario)
    print(f"Choices: {choices}")

    reaction = StoryEngine.generate_reaction(choices[0])
    print(f"Reaction: {reaction}")
