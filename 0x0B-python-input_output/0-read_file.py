#!/usr/bin/python3
"""This function is used to read the contents of a text file"""


def read_file(filename=""):
    """Read a UTF8 text file and print its contents to stdout."""
    try:
        with open(filename, encoding="utf-8") as file:
            for line in file:
                print(line, end="")
                print()  # Add a new line at the end
    except:
        pass
