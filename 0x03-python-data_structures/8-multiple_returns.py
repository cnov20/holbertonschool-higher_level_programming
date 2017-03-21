#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        first_character = None
    else:
        first_character = sentence[0]

    string_length = len(sentence)
    return(string_length, first_character)
