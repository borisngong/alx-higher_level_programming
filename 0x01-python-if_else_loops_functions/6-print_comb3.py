#!/usr/bin/python3
for k in range(10):
    for l in range(k + 1, 10):
        print("{:d}{:d}{}".format(k, l, ", " if l != 9 or k != 8 else ""), end="")
print()