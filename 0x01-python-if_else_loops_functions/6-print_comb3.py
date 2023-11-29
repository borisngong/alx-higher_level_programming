#!/usr/bin/python3
for k in range(10):
    for j in range(k + 1, 10):
        print("{:d}{:d}{}".format(k, j, ", " if j != 9 or k != 8 else ""),
              end="" if j != 9 or k != 8 else "\n")
