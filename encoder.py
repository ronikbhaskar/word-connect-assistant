"""
This file converts words into integer representations. 
Each representation encodes the characters present in the word,
but it does not differentiate based on frequency or position.
As such, these encodings are not unique.
Instead, they serve to allow for easy lookup when checking for character containment.

Author: Ronik Bhaskar
"""

class Encoder:

    CHAR_LIST = [
        1 << i for i in range(26)
    ]

    ORD_A = 97

    def __init__(self):
        pass

    def _encode_letter(self, word, letter):
        """
        Generates an integer representation for
        """

        if letter in word:
            return Encoder.CHAR_LIST[ord(letter) - Encoder.ORD_A]
        else:
            return 0
        
    def _count_ones(self, x):
        """
        did not come up with this myself
        bit operation only Hamming weight algorithm
        x : integer
         - encoding
        """
        x = (x & (0x55555555)) + ((x >> 1) & (0x55555555))
        x = (x & (0x33333333)) + ((x >> 2) & (0x33333333))
        x = (x & (0x0f0f0f0f)) + ((x >> 4) & (0x0f0f0f0f))
        x = (x & (0x00ff00ff)) + ((x >> 8) & (0x00ff00ff))
        x = (x & (0x0000ffff)) + ((x >> 16) & (0x0000ffff))
        return x;

    def encode(self, word):
        """
        Surprisingly fast
        """

        word = word.lower().strip()

        encoding = 0

        for letter in "abcdefghijklmnopqrstuvwxyz":
            encoding += self._encode_letter(word, letter)

        return encoding
    
    def is_in(self, letters_encoding, word_encoding):
        """
        The crux of this algorithm
        implies a homomorphism between binary strings and whole numbers
        """

        return self._count_ones(letters_encoding) - self._count_ones(word_encoding) == self._count_ones(letters_encoding ^ word_encoding)
    
    def matching_subset(self, letters_encoding, word_encoding_dict):
        """
        Reduce repeated calculations for checking multiple words
        """

        letters_count = self._count_ones(letters_encoding) # only compute once
        return [word for word, encoding in word_encoding_dict.items() \
                if letters_count - self._count_ones(encoding) == self._count_ones(letters_encoding ^ encoding)]