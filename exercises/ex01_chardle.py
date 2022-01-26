"""EX01 - Chardle - a cute step toward Wordle."""

__author__ = "730309871"

word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character: ")

if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + letter + " in " + word)

if word[0] == letter:
    print(letter + " found at index 0")
if word[1] == letter:
    print(letter + " found at index 1")
if word[2] == letter:
    print(letter + " found at index 2")
if word[3] == letter:
    print(letter + " found at index 3")
if word[4] == letter:
    print(letter + " found at index 4")

matches: int = 0
if word[0] == letter:
    matches = matches + 1
if word[1] == letter:
    matches = matches + 1
if word[2] == letter:
    matches = matches + 1
if word[3] == letter:
    matches = matches + 1
if word[4] == letter:
    matches = matches + 1

if matches == 0:
    print("No instances of " + letter + " found in " + word)
else: 
    if matches == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(matches) + " instances of " + letter + " found in " + word)