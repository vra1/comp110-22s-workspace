"""An exercise on dictionaries."""

__author__ = "730309871"


# figure out the whole key error thing
def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary."""
    result: dict[str, str] = {}
    for key in a:
        if a[key] not in result:
            result[a[key]] = key
        else:
            raise KeyError("Cannot repeat keys.")
    return result


def favorite_color(a: dict[str, str]) -> str:
    """Identifies the most popular color."""
    votes: dict[str, int] = {}
    for name in a:
        if a[name] not in votes:
            votes[a[name]] = 1
        else:
            votes[a[name]] += 1
    popular: str = ""
    i: int = 0
    for key in votes:
        if votes[key] > i:
            i = votes[key]
            popular = key
    return popular


def count(a: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a list."""
    times: dict[str, int] = {}
    for key in a:
        if key in times:
            times[key] += 1
        else:
            times[key] = 1
    return times