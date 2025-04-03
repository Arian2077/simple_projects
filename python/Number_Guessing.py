from random import randint
import tkinter as tk
from tkinter import messagebox


class NumberGuessingGame:
    def __init__(self, root):
        """Initialize the Number Guessing Game GUI."""
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.configure(bg="#f0f8ff")  # Set background color
        
        # Input Section
        tk.Label(
            root, text="Enter your number:", font=("Arial", 15), bg="#f0f8ff", fg="#333"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.enter_number = tk.Entry(root, font=("Arial", 15), justify="center", bg="#ffffff", fg="#333")
        self.enter_number.grid(row=0, column=1, padx=10, pady=10)
        
        # Generate a random target number between 1 and 100
        self.target_number = randint(1, 100)
        
        # Guess Button
        tk.Button(
            root, text="Guess", font=("Arial", 15), width=10, command=self.guess_number, bg="#4caf50", fg="#ffffff"
        ).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Result Display Section
        self.guessing_result = tk.Text(
            root, wrap=tk.WORD, width=50, height=10, font=("Arial", 12), bg="#e8f5e9", fg="#333"
        )
        self.guessing_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def guess_number(self):
        """Handle the guessing logic."""
        num = self.enter_number.get()
        try:
            num = int(num)  # Convert input to integer
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer.")
            return

        if num < 1 or num > 100:
            messagebox.showerror("Input Error", "Please enter a number between 1 and 100.")
            return

        if num < self.target_number:
            self.guessing_result.insert(tk.END, f"{num} is too low.\n")
        elif num > self.target_number:
            self.guessing_result.insert(tk.END, f"{num} is too high.\n")
        else:
            self.guessing_result.insert(tk.END, f"Congratulations! {num} is correct.\n")
            self.target_number = randint(1, 100)  # Reset the target number for a new game


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()