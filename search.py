#!python
import math

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""

    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index >= len(array):
        return None

    if array[index] == item:
        return index

    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


## TODO: Try doing with index rather than mutating the array.

def binary_search_iterative(array, item):
    offset = 0

    while (len(array) is not 1):
        middle = len(array) / 2
        print(middle + offset)
        if (array[middle] == item):
            return middle + offset
        if (array[middle] < item):
            array =  array[middle:]
            offset += int(math.ceil(middle))
        else:
            array = array[:middle]


    return 0 if array[0] == item else None


def binary_search_recursive(array, item, offset=0):
    if(len(array) is 1):
        return 0 if array[0] == item else None

    middle = len(array) / 2

    if (array[middle] == item):
        return  middle + offset

    if(array[middle] < item):
        return binary_search_recursive(array[middle:], item, offset + math.ceil(len(array) / 2))
    else:
        return binary_search_recursive(array[:middle], item, offset)
