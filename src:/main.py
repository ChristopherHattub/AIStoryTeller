from ui.interface import GameInterface
from utils.setup_helpers import setup_game
from config.chatgpt_config import chatgpt_config

def main():

    
    # Load the ChatGPT configuration
    chatgpt_config.load_config()
    
    # Game setup: get game-specific settings or initial configurations
    setup_game()

    # Initialize the game interface and run the game loop
    game_interface = GameInterface()
    game_interface.run()

if __name__ == "__main__":
    main()
