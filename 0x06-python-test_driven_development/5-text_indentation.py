#!/usr/bin/python3
def text_indentation(text):

    if type(text) is not str:
        raise TypeError('text must be a string')

#   words = text.split()
    i = 0
    letter = text[i]
    delimiter = set('.?:')
    for letter in text:
        print('{:s} '.join(format(letter)), end='')

        if letter in delimiter:
            print()
