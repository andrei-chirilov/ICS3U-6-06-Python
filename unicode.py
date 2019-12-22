#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: December 2019
# This program translates a word to unicode


def unicode_converter(word):
    # This takes a given word and translates it to unicode

    unicode_word = ""

    letters = {
        "a": "61",
        "b": "62",
        "c": "63",
        "d": "64",
        "e": "65",
        "f": "66",
        "g": "67",
        "h": "68",
        "i": "69",
        "j": "6a",
        "k": "6b",
        "l": "6c",
        "m": "6d",
        "n": "6e",
        "o": "6f",
        "p": "70",
        "q": "71",
        "r": "72",
        "s": "73",
        "t": "74",
        "u": "75",
        "v": "76",
        "w": "77",
        "x": "78",
        "y": "79",
        "z": "7a",
    }

    # process
    for letter in word:
        if letter in letters:
            unicode_word = unicode_word + letters[letter] + " "
        else:
            return "Sorry, this character is not in my list."

    return "In unicode the word is: " + unicode_word


def main():
    # This takes the user's word and passes it to UnicodeConverter()

    # input
    word = input("Enter your word that you would like translated here: ")

    # process
    word = unicode_converter(word)

    print(word)


if __name__ == "__main__":
    main()
