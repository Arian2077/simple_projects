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
    
