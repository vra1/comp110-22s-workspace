"""Testing dictionaries."""

__author__ = "730309871"


from dictionary import invert, favorite_color, count
import pytest


# invert tests
def test_invert_short() -> None:
    """Tests invert on just one key."""
    xs: dict[str, str] = {"A": "B"}
    assert invert(xs) == {"B": "A"}


def test_invert_normal() -> None:
    """Tests invert function on a normal dictionary."""
    xs: dict[str, str] = {"A": "1", "B": "2", "C": "3"}
    assert invert(xs) == {"1": "A", "2": "B", "3": "C"}


def test_invert_longer() -> None:
    """Tests invert function on a larger dictionary."""
    xs: dict[str, str] = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "E"}
    assert invert(xs) == {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5"}


with pytest.raises(KeyError):
    """Tests whether a KeyError is raised when a key is repeated."""
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


# favorite_color tests
def test_favorite_color_simple() -> None:
    """Tests favorite_color on a basic dictionary of names and colors."""
    xs: dict[str, str] = {"Jane": "green", "June": "red", "John": "green", "Jean": "blue"}
    assert favorite_color(xs) == "green"


def test_favorite_color_tie() -> None:
    """Tests favorite_color when there is a tie between two colors."""
    xs: dict[str, str] = {"Jane": "blue", "June": "red", "John": "blue", "Jean": "red"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_none() -> None:
    """Tests favorite_color when there is a tie between many colors."""
    xs: dict[str, str] = {"Jane": "blue", "June": "red", "John": "green", "Jean": "pink"}
    assert favorite_color(xs) == "blue"


# count tests
def test_count_repeat() -> None:
    """Tests count when there is a repeated value."""
    xs: list[str] = ["a", "b", "a", "c"]
    assert count(xs) == {"a": 2, "b": 1, "c": 1}


def test_count_no_repeats() -> None:
    """Tests count with no repeated values."""
    xs: list[str] = ["a", "b", "c", "d"]
    assert count(xs) == {"a": 1, "b": 1, "c": 1, "d": 1}


def test_count_empty() -> None:
    """Tests count when there are no values."""
    xs: list[str] = []
    assert count(xs) == {}