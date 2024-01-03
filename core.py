import random
import visualtext as vt

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
def printResultLandscape(playerTool, computerTool):
    if playerTool == 'R':
        if computerTool == 'R':
            return vt.playerRockComputerRock()
        elif computerTool == 'P':
            return vt.playerRockComputerPaper()
        elif computerTool == 'S':
            return vt.playerRockComputerScissors()
    elif playerTool == 'P':
        if computerTool == 'R':
            return vt.playerPaperComputerRock()
        elif computerTool == 'P':
            return vt.playerPaperComputerPaper()
        elif computerTool == 'S':
            return vt.playerPaperComputerScissors()
    elif playerTool == 'S':
        if computerTool == 'R':
            return vt.playerScissorsComputerRock()
        elif computerTool == 'P':
            return vt.playerScissorsComputerPaper()
        elif computerTool == 'S':
            return vt.playerScissorsComputerScissors()
    return "unknown"
