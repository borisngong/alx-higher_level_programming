#!/usr/bin/python3
def print_sorted_dictionary(my_dictionary):
    sorted_key = sorted(my_dictionary)
    for key in sorted_key:
        value = my_dictionary[key]
        print(f"{key}: {value}")
