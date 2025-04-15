import itertools
import string
import time

def common_guess(word: str) -> str | None:
    with open("words.txt", "r") as words:
        word_list : list[str] = words.read().splitlines()   
        
    for i, match in enumerate(word_list,start=1):
        if match == word:
            return f'Common match: {match} found at position {i}'