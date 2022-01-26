"""Using lessons 9 and 10 to recreate wordle."""

___author___ = "7303099871"

secret_word: str = "python"

guess: str = input(f"What is your {len(secret_word)}-letter guess?")

# Check whether the word is the right length
while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again:")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# These are variables that will be used in the while loop
counter: int = 0
boxes: str = ""
letter_checker: bool = False
yellow_counter: int = 0

while counter < len(guess):
    if guess[counter] == secret_word[counter]:
        boxes = boxes + GREEN_BOX
        # This determines if the right letter is in the right place and adds a green box
    else:
        while yellow_counter < len(guess) and not letter_checker:
            # This while loop checks for the letter in other places in the word
            if guess[counter] == secret_word[yellow_counter]:
                letter_checker = True
            yellow_counter = yellow_counter + 1
        # After checking for the letter, this if-else statement adds the appropriate box
        if letter_checker:
            boxes = boxes + YELLOW_BOX
        else:
            boxes = boxes + WHITE_BOX
    # These reset the variables for the yellow and white boxes 
    letter_checker = False
    yellow_counter = 0
    # Adding one to the counter variable causes the loop to evaluate the next letter of the guess
    counter = counter + 1

print(boxes)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
    exit()