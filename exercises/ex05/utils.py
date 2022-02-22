"""Docstring."""

__author__ = "730309871"


# define function named only_evens
# parameter: a list of integers
# returns a list of integers, which is the even integers from the parameter
def only_evens(numbers: list[int]) -> list[int]:
    """Identifies the even numbers in a list of integers."""
    evens: list[int] = []
    # go through list and find remainders
    # if remainder = 0, append to evens
    i: int = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            evens.append(numbers[i])
        i += 1
    return evens


# define a function named sub
# parameters: a list and 2 ints
# return: a list that is a section of the parameter with the int parameters as the index
def sub(base_list: list[int], start: int, stop: int) -> list[int]:
    """Returns a section of a list of integers."""
    sub_list: list[int] = []
    if start < 0:
        start = 0
    if stop > len(base_list):
        stop = len(base_list)
    if len(base_list) == 0 or start > len(base_list) or stop <= 0:
        return sub_list
    while start < stop:
        sub_list.append(base_list[start])
        start += 1
    return sub_list


# define a function named concat
# parameters: two lists of ints
# return a new list made of the first list followed by the second
def concat(first: list[int], second: list[int]) -> list[int]:
    """Combines two lists."""
    new_list: list[int] = []
    i: int = 0
    # add the first list
    while i < len(first):
        new_list.append(first[i])
        i += 1
    # add the second list
    counter: int = 0
    while counter < len(second):
        new_list.append(second[counter])
        counter += 1
    return new_list