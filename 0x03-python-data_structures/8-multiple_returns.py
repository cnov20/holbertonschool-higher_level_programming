#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence[0] = None

    string_length = len(sentence)
    return(string_length, sentence[0])
