import string
import secrets

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

    def run(self):
        for i in range(5):
            new_password = self.generate_password(length=15, symbol_check=True, upper_check=True)
            check = f'U:{self.upper_check(new_password)}, S:{self.symbol_check(new_password)}'
            print(f'P{i+1} -----> {new_password} | ({check})')

if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run()