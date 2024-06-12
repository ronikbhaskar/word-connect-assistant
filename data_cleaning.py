"""
Reducing the length of the number of words to look at.

Author: Ronik Bhaskar
"""

import json
from encoder import Encoder

def main():
    with open("words_alpha.txt", "r") as f:
        list_of_words = [word.strip() for word in f]

    length_3 = []
    length_4 = []
    length_5 = []
    length_6 = []
    length_7 = []
    length_8 = []
    length_9 = []

    print("putting words in buckets")

    for word in list_of_words:
        if len(word) == 3:
            length_3.append(word)
        elif len(word) == 4:
            length_4.append(word)
        elif len(word) == 5:
            length_5.append(word)
        elif len(word) == 6:
            length_6.append(word)
        elif len(word) == 7:
            length_7.append(word)
        elif len(word) == 8:
            length_8.append(word)
        elif len(word) == 9:
            length_9.append(word)

    encoder = Encoder()

    print("now encoding")
    for l, name in [
        (length_3, "length_3"),
        (length_4, "length_4"),
        (length_5, "length_5"),
        (length_6, "length_6"),
        (length_7, "length_7"),
        (length_8, "length_8"),
        (length_9, "length_9"),
    ]:
        print(name)
        data = {word: encoder.encode(word) for word in l}
        with open(f"{name}.json", "w") as f:
            json.dump(data, f)

if __name__ == "__main__":
    main()