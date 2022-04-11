"""Examples of default paramaters."""


def add(x: int, y: int = 0, z: int = 0) -> int:
    """Default paramters give more flexibility to a function."""
    return x + y


print(add(1, 2))
print(add(1))
