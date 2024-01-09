#!/usr/bin/python3
"""This function is used to read the contents of a text file"""


def read_file(filename=""):
    """Read a UTF8 text file and print its contents to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
