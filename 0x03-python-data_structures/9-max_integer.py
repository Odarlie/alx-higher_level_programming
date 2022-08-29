#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for el in my_list:
            if el > max:
                max = el
        return max
    return None
