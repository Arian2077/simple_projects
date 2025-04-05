import string
import secrets
import customtkinter as ctk

class PasswordGenerator:
    def __init__(self):
        self.combination = string.ascii_lowercase + string.digits

    def upper_check(self, password) -> bool:
        for char in password:
            if char.isupper():
                return True
        return False

    def symbol_check(self, password) -> bool:
        for char in password:
            if char in string.punctuation:
                return True
        return False

    def generate_password(self, length: int, upper_check: bool, symbol_check: bool) -> str:
        combination = self.combination
        if upper_check:
            combination += string.ascii_uppercase
        if symbol_check:
            combination += string.punctuation

        combination_length = len(combination)
        new_password = ''
        for i in range(length):
            # Use secrets.choice for cryptographic security
            new_password += combination[secrets.randbelow(combination_length)]
        return new_password

class PasswordGeneratorApp:
    def __init__(self):
        self.generator = PasswordGenerator()
        self.root = ctk.CTk()
        self.root.title("Password Generator")
        self.root.geometry("500x300")

        # Title Label
        self.title_label = ctk.CTkLabel(self.root, text="Password Generator", font=("Arial", 20))
        self.title_label.pack(pady=10)

        # Length Slider
        self.length_label = ctk.CTkLabel(self.root, text="Password Length:")
        self.length_label.pack()
        self.length_slider = ctk.CTkSlider(self.root, from_=8, to=32, number_of_steps=24)
        self.length_slider.set(15)
        self.length_slider.pack(pady=5)

        # Uppercase Checkbox
        self.uppercase_var = ctk.BooleanVar()
        self.uppercase_checkbox = ctk.CTkCheckBox(self.root, text="Include Uppercase Letters", variable=self.uppercase_var)
        self.uppercase_checkbox.pack(pady=5)

        # Symbols Checkbox
        self.symbol_var = ctk.BooleanVar()
        self.symbol_checkbox = ctk.CTkCheckBox(self.root, text="Include Symbols", variable=self.symbol_var)
        self.symbol_checkbox.pack(pady=5)

        # Generate Button
        self.generate_button = ctk.CTkButton(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        # Output Entry
        self.output_entry = ctk.CTkEntry(self.root, width=400, font=("Arial", 14))
        self.output_entry.pack(pady=10)

    def generate_password(self):
        length = int(self.length_slider.get())
        include_upper = self.uppercase_var.get()
        include_symbols = self.symbol_var.get()
        password = self.generator.generate_password(length, include_upper, include_symbols)
        self.output_entry.delete(0, ctk.END)
        self.output_entry.insert(0, password)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.run()