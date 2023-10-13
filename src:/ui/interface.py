import tkinter as tk
from engine.story_engine import StoryEngine

class GameInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AIStoryTeller")
        self.root.geometry("600x400")
        self.root.configure(bg="white")

        # Player's name input
        self.name_label = tk.Label(self.root, text="Enter your name:", bg="white")
        self.name_label.pack(pady=10)
        
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=10)
        
        self.submit_button = tk.Button(self.root, text="Submit", command=self.start_game)
        self.submit_button.pack(pady=10)

        # Initialized when the game starts
        self.character_name_label = None
        self.scenario_label = None
        self.choices_buttons = []

    def start_game(self):
        # Get the player's name and remove input widgets
        player_name = self.name_entry.get()
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.submit_button.pack_forget()
        
        # Show player's name at the top
        self.character_name_label = tk.Label(self.root, text=player_name, bg="white", font=("Arial", 20))
        self.character_name_label.pack(pady=10)
        
        self.show_next_scenario()

    def show_next_scenario(self):
        scenario = StoryEngine.generate_scenario()
        self.scenario_label = tk.Label(self.root, text=scenario, bg="white", wraplength=550, justify=tk.LEFT)
        self.scenario_label.pack(pady=10)
        
        choices = StoryEngine.generate_choices(scenario)
        for choice in choices:
            choice_button = tk.Button(self.root, text=choice, command=lambda c=choice: self.handle_choice(c))
            choice_button.pack(pady=10)
            self.choices_buttons.append(choice_button)

    def handle_choice(self, chosen_choice):
        # Remove unchosen buttons
        for button in self.choices_buttons:
            if button["text"] != chosen_choice:
                button.pack_forget()

        # Show continuation of the story based on the choice
        reaction = StoryEngine.generate_reaction(chosen_choice)
        reaction_label = tk.Label(self.root, text=reaction, bg="white", wraplength=550, justify=tk.LEFT)
        reaction_label.pack(pady=10)

        # Wait for a bit
        self.root.after(5000, self.show_next_scenario)

    def run(self):
        self.root.mainloop()


# Start the game
if __name__ == "__main__":
    game = GameInterface()
    game.run()
