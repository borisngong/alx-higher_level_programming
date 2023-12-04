#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for k in my_string:
        if (k != 'c') and (k != 'C'):
            new_str += k
    return (new_str)
