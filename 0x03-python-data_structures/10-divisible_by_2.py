#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result_list = my_list[:]
    for count, num in enumerate(my_list):
        if num % 2 == 0:
            result_list[count] = True
        else:
            result_list[count] = False
    return result_list
