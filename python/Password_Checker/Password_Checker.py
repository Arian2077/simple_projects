import itertools
import string
import time

def common_guess(word: str) -> str | None:
    with open("words.txt", "r") as file:
        words = file.read().splitlines()