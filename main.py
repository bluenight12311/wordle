#pull a word from a random word bank
import random

with open("wordle-allowed-guesses.txt", "r") as file:
    allowed = file.read()
with open("wordle-answers-alphabetical.txt", "r") as file:
    correct = file.read()
actualCorrect = correct.splitlines()
actualAllowed = allowed.splitlines()
correctAnswer = random.choice(actualCorrect)
print(correctAnswer)
#ask for user input
first = input("what is your first word? ")
#check user input against a bank of words

if first in actualAllowed or first in actualCorrect:
    #check if it is word
    for i in range(len(correctAnswer)):
        if first[i] == correctAnswer[i]:
            print(f"At the {i} position, the letters match")
        else:
            print(f"at the {i} position, the letter don't match")
    
else:
    print("Not a word! It needs to be 5 letters! ")
