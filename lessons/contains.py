"""Example of a function that searches through a list."""


def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davidson"]))


# Define a function named contains
# Two parameters
# 1. needle - the string we're searching for
# 2. haystack - the list we're searching through
def contains(needle: str, haystack: list[str]) -> bool:
    # Algorithm
    #  For each item in the haystack, test if it is equal to the needle
    #       if so, return True
    #   After testing all items, return false, because not found
    for item in haystack:
        if item == needle:
            return True
    return False
# Returns true if needle in haystack, false otherwise


main()