#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newly_created_list = []
    for element in my_list:
        if element == search:
            newly_created_list.append(replace)
        else:
            newly_created_list.append(element)
    return newly_created_list
