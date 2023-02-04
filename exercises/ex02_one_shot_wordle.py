"""EX02 - One-Shot-Wordle!!!"""
__author__ = "730560412"

secret_word = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index_counter = 0
wordle = ""
guess: str = input("What is your 6-letter guess? ")
while (int(len(guess)) != 6):
        print(f"That was not {len(secret_word)} letters! Try again: ")
        guess = input("What is your 6-letter guess? ") 

if (guess == secret_word):
        while (index_counter < 6):
                wordle = wordle + GREEN_BOX
                index_counter+=1        
        print(wordle)
        print ("Woo! You got it!")

if (len(guess) == len(secret_word) and guess != secret_word):
        while (index_counter < 6):
                if(guess[index_counter] == secret_word[index_counter]):
                        wordle = wordle + GREEN_BOX
                        index_counter+=1
                else:
                        yellow = False
                        yellowindex = 0
                        while (yellow is False and yellowindex < 6):
                                 if(guess[index_counter] == secret_word[yellowindex]):
                                        yellow = True
                                        wordle = wordle + YELLOW_BOX         
                                 else:
                                  yellowindex += 1 
                                
                                 if(yellow is False and yellowindex == 6):
                                        wordle = wordle + WHITE_BOX
                        index_counter+=1
        print (wordle)
        print("Not quite. Play again soon!")


