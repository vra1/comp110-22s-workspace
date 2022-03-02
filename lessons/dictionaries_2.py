def main() -> None:
    game0: dict[str, int] = {"KJ": 0, "ML": 1}
    game1: dict[str, int] = {"EW": 2, "ML": 3}
    merged: dict[str, int] = merge(game0, game1)
    print(merged)


def merge(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    result: dict[str, int] = {}
    for key in a: 
        result[key] = a[key]
    for key in b:
        result[key] = b[key]
    return result


if __name__ == "__main__":
    main()