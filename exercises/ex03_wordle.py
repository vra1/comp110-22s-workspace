"""Another, more complete, version of Wordle."""

__author__ = "730309871"


def contains_char(guess: str, letter: str) -> bool:
    """A function to check for a letterin a word."""
    assert len(letter) == 1
    counter: int = 0
    while counter < len(guess):
        if guess[counter] == letter:
            return True
        else:
            counter += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """A function to insert emojis based on whether a letter appears in a word."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret)
    i: int = 0
    boxes: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            boxes += GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                boxes += YELLOW_BOX
            else:
                boxes += WHITE_BOX
        i += 1
    return boxes


def input_guess(length: int) -> str:
    """Checks that the guess is the correct length."""
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    turns: int = 1
    secret: str = "codes"
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turns}/6 turns!")
            exit()
        turns += 1
    print(f"X/{len(secret)} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()