"""Using lessons 9 and 10 to recreate wordle."""

__author__ = "730309871"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

counter: int = 0
boxes: str = ""
letter_checker: bool = False
yellow_counter: int = 0

secret_word: str = "python"

# This prompts the player for their guess and saves it as a variable
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

# This while loop checks that the guess is the right number of letters
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

while counter < len(guess):
    if guess[counter] == secret_word[counter]:
        # this adds green boxes if the letter is in the correct place
        boxes = boxes + GREEN_BOX
    else:
        while yellow_counter < len(guess) and not letter_checker:
            # This while loop checks the other letters in the secret word
            if guess[counter] == secret_word[yellow_counter]:
                letter_checker = True
            yellow_counter = yellow_counter + 1
        # The following if/else statement adds the appropriate color box
        if letter_checker:
            boxes = boxes + YELLOW_BOX
        else:
            boxes = boxes + WHITE_BOX
    # These reset the variables so that the while loop functions properly for the next letter
    letter_checker = False
    yellow_counter = 0
    # This changes the index so that the loop does not continue to check the same letter infinitely
    counter = counter + 1

# Lines 45-50 display the correct colors of boxes and give the appropriate response
print(boxes)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")