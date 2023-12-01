#!/usr/bin/python3
import sys
from decimal import Decimal

if __name__ == "__main__":
    argument_passed = sys.argv[1:]
    argument_solution = sum(Decimal(argn) for argn in argument_passed)
    print(argument_solution)
