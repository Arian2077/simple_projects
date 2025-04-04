from random import choice
import sys


class RPS:
    def __init__(self):
        print("welcome to RPS game!")
        self.choices = {'rock':'🪨','paper':'📃','scissors':'✂️'}
        self.valid_choices = list(self.choices.keys())
        self.play_game()
        
    def play_game(self):
        user_choice : str = input("Rock,Paper or Scissors >>>> ").lower()
        
        if user_choice == "exit":
            print("Hope to see you again,bye👋🏼")
            sys.exit()
        elif user_choice is not self.valid_choices:
            print(f"please choose among valid choices >>> {self.valid_choices}")
            return self.play_game()
        else:
            ai_choice = choice([self.valid_choices])
            
            self.display(user_choice,ai_choice)
        
                
             
        
    def display(self,user_choice,ai_choice):
        ...
        
    def check(self,user_choice,ai_choice):
        ...    

if __name__ == "__main__":
    game = RPS()
    game.play_game()    