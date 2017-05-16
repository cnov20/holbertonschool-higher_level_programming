#!/usr/bin/python3
def text_indentation(text):

    if type(text) is not str:
        raise TypeError('text must be a string')

    ch = 0
    delimiter = set('.?:')
    for letter in delimiter:
        if letter in text:
            text = text.replace(letter, letter + '\n\n')

    words = text.split('\n')
    print('\n'.join(format(letter).strip() for letter in words), end='')
