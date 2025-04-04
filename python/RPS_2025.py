import random
import sys


class RPS:
    def __init__(self):
        print("Welcome to the RPS game!")
        self._choices = {'rock': '🪨', 'paper': '📃', 'scissors': '✂️'}
        self._valid_choices = list(self._choices.keys())

    def start_game(self):
        """Starts the game loop."""
        while True:
            user_choice = self._get_user_choice()
            if user_choice == "exit":
                print("Hope to see you again, bye! 👋🏼")
                sys.exit()
            
            ai_choice = self._get_ai_choice()
            self._display_choices(user_choice, ai_choice)
            self._determine_winner(user_choice, ai_choice)

    def _get_user_choice(self):
        """Handles user input and validates it."""
        while True:
            user_choice = input("Rock, Paper, or Scissors (or type 'exit' to quit) >>> ").lower()
            if user_choice in self._valid_choices or user_choice == "exit":
                return user_choice
            print(f"Invalid choice. Please choose from: {self._valid_choices}")

    def _get_ai_choice(self):
        """Generates a random choice for the AI."""
        return random.choice(self._valid_choices)

    def _display_choices(self, user_choice, ai_choice):
        """Displays the choices made by the user and the AI."""
        print("----------------------------------------")
        print(f"You chose: {self._choices[user_choice]}")
        print(f"AI chose: {self._choices[ai_choice]}")
        print("----------------------------------------")

    def _determine_winner(self, user_choice, ai_choice):
        """Determines and displays the winner."""
        if user_choice == ai_choice:
            print("It's a tie! 🙌🏼")
        elif (user_choice == "rock" and ai_choice == "scissors") or \
             (user_choice == "paper" and ai_choice == "rock") or \
             (user_choice == "scissors" and ai_choice == "paper"):
            print("You win! 🎉")
        else:
            print("AI wins! 😢")


if __name__ == "__main__":
    game = RPS()
    game.start_game()