import tkinter as tk
from tkinter import messagebox


class StoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mad Libs Story Generator")

        # Labels and Entry fields for inputs
        tk.Label(root, text="Enter a noun:").grid(row=0, column=0, padx=10, pady=5)
        self.noun1_entry = tk.Entry(root)
        self.noun1_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Enter an adjective:").grid(row=1, column=0, padx=10, pady=5)
        self.adjective_entry = tk.Entry(root)
        self.adjective_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Enter a verb:").grid(row=2, column=0, padx=10, pady=5)
        self.verb1_entry = tk.Entry(root)
        self.verb1_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Enter another noun:").grid(row=3, column=0, padx=10, pady=5)
        self.noun2_entry = tk.Entry(root)
        self.noun2_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Enter another verb:").grid(row=4, column=0, padx=10, pady=5)
        self.verb2_entry = tk.Entry(root)
        self.verb2_entry.grid(row=4, column=1, padx=10, pady=5)

        # Button to generate the story
        tk.Button(root, text="Generate Story", command=self.generate_story).grid(
            row=5, column=0, columnspan=2, pady=10
        )

        # Text widget to display the story
        self.story_text = tk.Text(root, wrap=tk.WORD, width=50, height=15)
        self.story_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def generate_story(self):
        # Collect inputs
        noun1 = self.noun1_entry.get()
        adjective = self.adjective_entry.get()
        verb1 = self.verb1_entry.get()
        noun2 = self.noun2_entry.get()
        verb2 = self.verb2_entry.get()

        # Validate inputs
        if not all([noun1, adjective, verb1, noun2, verb2]):
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        # Generate the story
        story = f"""
        Once upon a time, there was a {adjective} {noun1} who loved to {verb1} all day.

        One day, {noun2} walked into the room and caught the {noun1} in the act. 

        {noun2}: "What are you doing?"
        {noun1}: "I'm just {verb1}ing, what's the big deal?"
        {noun2}: "Well, it's not every day that you see a {noun1} {verb1}ing in the middle of the day."
        {noun1}: "I guess you're right. Maybe I should take a break."
        {noun2}: "That's probably a good idea. Why don't we go {verb2} instead?"
        {noun1}: "Sure, that sounds like fun!"

        And so, {noun2} and the {noun1} went off to {verb2} and had a great time. 
        The end.
        """

        # Display the story
        self.story_text.delete(1.0, tk.END)
        self.story_text.insert(tk.END, story)


if __name__ == "__main__":
    root = tk.Tk()
    app = StoryApp(root)
    root.mainloop()