"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730560412"

charcounter = 0
wordleword: str = input("Please enter a 5-character word: ")
if len(wordleword) != 5:
    print("Error: Word must contain 5 characters")
    exit()

wordlechar: str = input("Please enter a single character: ")
if len(wordlechar) != 1:
    print("Error: Character must be a single character.")
    exit()
else:
    print("Searching for " + wordlechar + " in " + wordleword)

if wordlechar == wordleword[0]:
    print(wordlechar + " found at index 0")
    charcounter += 1
if wordlechar == wordleword[1]:
    print(wordlechar + " found at index 1")
    charcounter += 1
if wordlechar == wordleword[2]:
    print(wordlechar + " found at index 2")
    charcounter += 1
if wordlechar == wordleword[3]:
    print(wordlechar + " found at index 3")
    charcounter += 1
if wordlechar == wordleword[4]:
    print(wordlechar + " found at index 4")
    charcounter += 1

if charcounter == 1:
    print(str(charcounter) + " instance of " + wordlechar + " found in " + wordleword)  
elif charcounter > 1:
    print(str(charcounter) + " instances of " + wordlechar + " found in " + wordleword)  
else:
    print("No instances of " + wordlechar + " found in " + wordleword)  