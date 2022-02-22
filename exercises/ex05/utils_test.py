"""Tests the functions for exercise 5."""

__author__ = "730309871"


from utils import only_evens, sub, concat


# only_evens tests
def test_only_evens_empty() -> None:
    """Checks that only_evens can return an empty list when given an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_many() -> None:
    """Tests that only_evens works on a normal list."""
    xs: list[int] = [0, 1, 2, 3, 4, 5]
    assert only_evens(xs) == [0, 2, 4]


def test_only_evens_non_sequential() -> None:
    """Another test for a normal list of integers."""
    xs: list[int] = [0, 21, 34, 6, 50]
    assert only_evens(xs) == [0, 34, 6, 50]


def test_only_evens_odds() -> None:
    """Tests that only_evens can return an empty list when all integers are odd."""
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_only_evens_four() -> None:
    """Tests the output of only_evens when an even number is repeated."""
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


# sub tests
def test_sub_empty() -> None:
    """Tests sub on an empty list."""
    xs: list[int] = []
    a: int = 2
    b: int = 5
    assert sub(xs, a, b) == []


def test_sub_high_end() -> None:
    """Tests sub when the end argument is higher than the length of the list."""
    xs: list[int] = [0, 1, 2, 3]
    a: int = 0
    b: int = 9
    assert sub(xs, a, b) == [0, 1, 2, 3]


def test_sub_basic() -> None:
    """Tests sub."""
    xs: list[int] = [0, 1, 2, 3, 4, 5, 6]
    a: int = 2
    b: int = 5
    assert sub(xs, a, b) == [2, 3, 4]


def test_sub_negative() -> None:
    """Tests sub when the start argument is negative."""
    xs: list[int] = [0, 1, 2, 3]
    a: int = -2
    b: int = 3
    assert sub(xs, a, b) == [0, 1, 2]


def test_sub_too_long() -> None:
    """Tests sub when the start argument is higher than the length of the list."""
    xs: list[int] = [0, 1, 2, 3]
    a: int = 5
    b: int = 7
    assert sub(xs, a, b) == []


def test_sub_negative_end() -> None:
    """Tests sub when the end argument is negative."""
    xs: list[int] = [0, 1, 2, 3]
    a: int = -3
    b: int = -2
    assert sub(xs, a, b) == []


# concat tests
def test_concat_empty() -> None:
    """Tests concat when one of the lists is empty."""
    a: list[int] = []
    b: list[int] = [1, 2, 3]
    assert concat(a, b) == [1, 2, 3]


def test_concat_basic() -> None:
    """Tests concat with two normal lists."""
    a: list[int] = [1, 2, 3]
    b: list[int] = [4, 5, 6]
    assert concat(a, b) == [1, 2, 3, 4, 5, 6]


def test_concat_many() -> None:
    """Tests concat."""
    a: list[int] = [10, 4, 15, -12]
    b: list[int] = [-2, 25, 29, 13]
    assert concat(a, b) == [10, 4, 15, -12, -2, 25, 29, 13]