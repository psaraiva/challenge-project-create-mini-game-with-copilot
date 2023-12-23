import random

inputTool = ('R', 'P', 'S')

def getComputerChoice():
    return random.choice(inputTool)

def isValidInput(inputPlayer):
    if type(inputPlayer) == str:
        return inputPlayer.upper() in inputTool
    return False

def getUserInput():
    return input("Please choise: (R)ock, (P)aper, (S)cissors,  (Q)uit: ").upper()

def checkWin(inputPlayer, inputComputer):
    if inputPlayer == inputComputer:
        return 0
    if inputPlayer == 'R' and inputComputer == 'S':
        return 1
    if inputPlayer == 'P' and inputComputer == 'R':
        return 1
    if inputPlayer == 'S' and inputComputer == 'P':
        return 1
    return -1
