"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730309871"


class Simpy:
    """Class for working with a list of float values."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor with values as attributes."""
        self.values = values

    def __str__(self) -> str:
        """Represents Simpy objects."""
        return f"Simpy({self.values})"

    def fill(self, a: float, b: int) -> None:
        """Fills a Simpy object with a value repeated a certain number of times."""
        new_list: list[float] = []
        i: int = 0
        while i < b:
            new_list.append(a)
            i += 1
        self.__init__(new_list)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills a Simpy object with a range of values that are a certain amount apart."""
        assert step != 0.0
        values: list[float] = []
        current: float = start
        if step > 0:
            while current < stop:
                values.append(current)
                current += step
        else: 
            while current > stop:
                values.append(current)
                current += step
        self.__init__(values)
    
    def sum(self) -> float:
        """Adds all the values."""
        result: float = 0.0
        for item in self.values:
            result += item
        return result

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overloads the addition operator."""
        new_list: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                a: float = 0.0
                a = self.values[i] + rhs.values[i]
                new_list.append(a)
                i += 1
        else:
            for value in self.values:
                new_list.append(value + rhs)
        return Simpy(new_list)
    
    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overloads the exponent operator."""
        new_list: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                a: float = 0.0
                a = self.values[i] ** rhs.values[i]
                new_list.append(a)
                i += 1
        else:
            for value in self.values:
                new_list.append(value ** rhs)
        return Simpy(new_list)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloads the == operator."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else: 
                    result.append(False)
                i += 1
        else: 
            for value in self.values:
                if value == rhs:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on the relationship between two Simpy objects or a Simpy and a float."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        else:
            for value in self.values:
                if value > rhs:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloads the subscription operator."""
        if isinstance(rhs, int):
            result: float = 0.0
            result = self.values[rhs]
            return result
        else:
            new_list: list[float] = []
            i: int = 0
            while i < len(self.values):
                if rhs[i] is True:
                    new_list.append(self.values[i])
                i += 1
            return Simpy(new_list)