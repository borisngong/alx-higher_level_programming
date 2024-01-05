#!/usr/bin/python3
def magic_string():
    global counter
    counter = globals().get('counter', 0) + 1
    return ', '.join(['BestSchool'] * (counter - 1)) + ', BestSchool'
