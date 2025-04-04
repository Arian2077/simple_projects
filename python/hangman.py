from random import choice

class HangmanGame:
    def __init__(self):
        self.word: str = choice(['apple','python','spiderman','kratos','secret','banana','watermelon'])
        self.guessed: str = ''
        self.tries: int = 3

    def display_word(self):
        """Display the current state of the word with guessed letters."""
        blanks = 0
        print('Word: ', end='')
        for char in self.word:
            if char in self.guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1
        print()  # Add a blank line
        return blanks

    def get_user_input(self) -> str:
        """Prompt the user for a letter and validate input."""
        while True:
            guess = input('Enter a letter: ').lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single valid letter.")
            elif guess in self.guessed:
                print(f'You already used: "{guess}". Please try with another letter!')
            else:
                return guess

    def check_guess(self, guess: str) -> None:
        """Check if the guessed letter is in the word."""
        self.guessed += guess
        if guess not in self.word:
            self.tries -= 1
            print(f'Sorry, that was wrong... ({self.tries} tries remaining)')

    def play(self) -> None:
        """Run the main game loop."""
        username: str = input('What is your name? >> ')
        print(f'Welcome to hangman, {username}!')

        while self.tries > 0:
            blanks = self.display_word()

            if blanks == 0:
                print('You got it! Congratulations!')
                break

            guess = self.get_user_input()
            self.check_guess(guess)

            if self.tries == 0:
                print(f'No more tries remaining... You lose. The word was "{self.word}".')

if __name__ == '__main__':
    game = HangmanGame()
    game.play()