#pull a word from a random word bank
import random

with open("wordle-allowed-guesses.txt", "r") as file:
    allowed = file.read()
with open("wordle-answers-alphabetical.txt", "r") as file:
    correct = file.read()
actualCorrect = correct.splitlines()
actualAllowed = allowed.splitlines()
correctAnswer = random.choice(actualCorrect)
correctChar = []
userChar = []
print(correctAnswer)
#ask for user input
tries = 0
while True:
    first = input(f"Guess {tries}: what is your guess? ")
    for a in range(5):
        userChar.append(first[a])
        correctChar.append(correctAnswer[a])
    #win condition
    if first == correctAnswer:
        print("you won!")
        break
    if tries == 5:
        print("You ran out of tries!")
        break
    
    if first in actualAllowed or first in actualCorrect:
        tries = tries + 1 #add tries
        
        #green yellow gray logic
        for i in range(len(correctAnswer)):
            
            if first[i] == correctAnswer[i]:
                print(f"At the {i} position, the letters match")
                correctChar.pop(correctAnswer[i])
                userChar.pop(correctAnswer[i])
            elif first[i] in correctChar:
                index = correctChar.index(first[i])
                correctChar.pop(index)
                userChar.remove(first[i])
                print(f"at the {i} position, the letter is yellow")
            else:
                print(f"at the {i} positon the letter doesn't exist")
        print(correctChar)
        print(userChar)
        userChar.clear()
    else:
        print("Not a word! It needs to be 5 letters! ")
