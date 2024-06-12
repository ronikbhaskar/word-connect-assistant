"""
Author: Ronik Bhaskar
"""

import os
import json
from encoder import Encoder

WORD_ENCODINGS_PATH = "word_encodings"

def get_encodings(length):
    with open(os.path.join(WORD_ENCODINGS_PATH, f"length_{length}.json")) as f:
        encodings = json.load(f)

    return encodings

def force_input(message, matches_format, wrapper):
    while 1:
        i = wrapper(input(message))
        if matches_format(i):
            return i

def thorough_check(sorted_letters, word):
    """
    assumes letters are sorted alphabetically and stored as list
    """

    sorted_word = list(sorted(word))
    num_letters = len(sorted_letters)
    li, wi = 0, 0

    while li < num_letters:
        if sorted_letters[li] == sorted_word[wi]:
            wi += 1
        if wi == len(word):
            return True
        li += 1
    
    return wi == len(word)

def main():
    enc = Encoder() 
    letters = force_input("Please enter the available letters: ", lambda x: x.isalpha(), lambda x: x.lower().strip())
    length = force_input("Please enter the number of letters in the remaining word: ", lambda x: 3 <= x <= 9, int)

    encodings = get_encodings(length)
    letters_encoding = enc.encode(letters)
    shortlist = enc.matching_subset(letters_encoding, encodings)

    sorted_letters = list(sorted(letters))

    print("Potential candidates:")

    potential_candiates = list(filter(lambda x: thorough_check(sorted_letters, x), shortlist))
    if len(potential_candiates) > 0:
        for word in potential_candiates:
            print(word)
    else:
        print("unable to find any valid words")


if __name__ == "__main__":
    main()