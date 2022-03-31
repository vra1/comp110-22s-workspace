"""Dictionary related utility functions."""

__author__ = "730309871"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of all values in a column whose name is the other parameter."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a list of rows to a dictionary of columns.."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], number: int) -> dict[str, list[str]]:
    """Produce a column based table with only the first (number) rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        values: list[str] = []
        i: int = 0
        while i < number and i < len(table):
            values.append(table[column][i])
            i += 1
        result[column] = values
    return result


def select(table: dict[str, list[str]], subset: list[str]) -> dict[str, list[str]]:
    """Produces a column based table with a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for title in subset:
        result[title] = table[title]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column-based tables."""
    result: dict[str, list[str]] = {}
    for column in table_one:
        result[column] = table_one[column]
    for column in table_two:
        if column in result:
            result[column] += table_two[column]
        else:
            result[column] = table_two[column]
    return result


def count(a: list[str]) -> dict[str, int]:
    """Turns a list into dictionary where the value is the number of times the key occurs."""
    result: dict[str, int] = {}
    for item in a:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def high_values(a: dict[str, int], b: int) -> dict[str, int]:
    """Returns all values in a dictionary that are greater than or equal to a certain value."""
    result: dict[str, int] = {}
    for key in a:
        if a[key] >= b:
            result[key] = a[key]
    return result