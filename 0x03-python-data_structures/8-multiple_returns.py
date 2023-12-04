#!/usr/bin/python3
def multiple_returns(sentence):
    longii = len(sentence)
    first_char = sentence[0] if longii > 0 else "None"
    tup = longii, first_char
    return tup
