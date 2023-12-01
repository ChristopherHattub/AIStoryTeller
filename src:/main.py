from ui.interface import GameInterface
from utils.setup_helpers import setup_game
from config.chatgpt_config import load_config

def main():

    
    # TODO Fix the ChatGPT configuration 
    #load_config()
    
    # Game setup: get game-specific settings or initial configurations
    setup_game()

    # Initialize the game interface and run the game loop
    game_interface = GameInterface()
    game_interface.run()

if __name__ == "__main__":
    main()
