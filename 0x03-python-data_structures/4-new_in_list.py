#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temporal_list = my_list[:]
    if 0 <= idx < len(my_list):
        temporal_list[idx] = element
        return temporal_list
    return my_list
