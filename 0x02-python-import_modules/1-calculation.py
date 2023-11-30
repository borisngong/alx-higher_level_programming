#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
add_soln = add(a, b)
sub_soln = sub(a, b)
mul_soln = mul(a, b)
div_soln = div(a, b)
print("{} + {} = {}".format(a, b, add_soln))
print("{} - {} = {}".format(a, b, sub_soln))
print("{} * {} = {}".format(a, b, mul_soln))
print("{} / {} = {}".format(a, b, div_soln))
