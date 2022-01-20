"""An example of conditional/If-else statements"""

SECRET: int = 3

print("I'm thinking of a number between 1-5. What is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You guessed correctly!")
    print("Have a wonderful day!")
else:
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("Guess lower!")
    else:
        print("Guess higher!")
        if guess == 1:
            print("dummy!")
    print("Try running the program again.")


print("Game over.")