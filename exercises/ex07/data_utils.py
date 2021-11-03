"""Utility functions."""

__author__ = "730408456"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(head_dict: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Returns the first N rows of a table."""
    result: dict[str, list[str]] = {}
    for column in head_dict:
        if n >= len(head_dict[column]):
            return head_dict
        list_n: list[str] = []
        i: int = 0
        while i < n:
            item = head_dict[column][i]
            list_n.append(item)
            i += 1
        result[column] = list_n
    return result


def select(select_dict: dict[str, list[str]], select_list: list[str]) -> dict[str, list[str]]:
    """Produce a column based table with only a specific subset of the original columns."""
    solution: dict[str, list[str]] = {}
    for column in select_list:
        solution[column] = select_dict[column]
    return solution


def concat(concat_dict_one: dict[str, list[str]], concat_dict_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a column-based table with two column-based tables combined."""
    value: dict[str, list[str]] = {}
    for key in concat_dict_one:
        value[key] = concat_dict_one[key]
        for keys in value:
            answerlist: list[str] = value[keys]
            for item in concat_dict_two[keys]:
                answerlist.append(item)
            value[keys] = answerlist
        else:
            value[keys] = concat_dict_two[keys]  
    return value
    