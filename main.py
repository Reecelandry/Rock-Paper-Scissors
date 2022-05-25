# Rock Paper Scissors AI
# Create by Reece Landry
# Project includes: Inputs, Conditional Logic, Recursion, Enum, Random

import random
from enum import IntEnum

def getUserSelection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choicesStr = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choicesStr}): "))
    if selection > 2:
        print("Invalid selection...")
        # Recursion call
        return getUserSelection()
    action = Action(selection)
    return action

def getComputerSelection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def didUserWin(userAction, computerAction):
    if userAction == computerAction:
        return Results.Tie
    elif userAction == Action.Rock:
        # User chooses Rock
        if computerAction == Action.Paper:
            return Results.Computer
        else:
            return Results.User
    elif userAction == Action.Paper:
        # User chooses Paper
        if computerAction == Action.Rock:
            return Results.User
        else:
            return Results.Computer
    elif userAction == Action.Scissors:
        # User chooses Scissors
        if computerAction == Action.Paper:
            return Results.User
        else:
            return Results.Computer

def printWinner(result):
    if result == Results.User:
        print("Congratulations! You Win!")
    elif result == Results.Computer:
        print("Oh No! You lost.")
    else:
        print("Its a tie!")

def replay():

    playAgain = input("Would you like to play again? (y/n) ")
    if playAgain != 'y' and playAgain != 'n':
        print("Invalid input...")
        # Recursion Call
        return replay()
    elif playAgain == 'n':
        return False
    else:
        return True

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

class Results(IntEnum):
    User = 0
    Computer = 1
    Tie = 2

# Main loop
while True:
    user = getUserSelection()
    computer = getComputerSelection()
    result = didUserWin(user, computer)
    printWinner(result)

    if not replay():
        print("Thank you for playing! Bye.")
        break



