#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argument_passed = len(sys.argv) - 1

    if argument_passed == 0:
        print("0 arguments.")
    else:
        print(f"{argument_passed}: argument")

        for k, args in enumerate(sys.argv[1:], start=1):
            print(f"{k}: {args}")
