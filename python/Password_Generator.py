import string
import secrets


def upper_check(password) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False

def symbol_check(password) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

def password_generator(length:int,upper_check: bool,symbol_check:bool):
    
    combination = string.ascii_lowercase + string.digits
    
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
    
if __name__ == "__main__":
    for i in range(5):
        new_password = password_generator(length=15,symbol_check=False,upper_check=False)
        check = f'U:{upper_check(new_password)}, S:{symbol_check(new_password)}'
        print(f'P{i+1} -----> {new_password} | ({check})')