#!/usr/bin/python3
"""Defines a function for looking up an object's attributes."""


def lookup(obj):
    """Return a list of available attributes of an object."""
    return dir(obj)
