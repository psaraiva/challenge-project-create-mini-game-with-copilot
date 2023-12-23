import core
import visualtext

# @todo: add counter
# @todo: add score

dev = False

def main():
    while True:
        inputPlayer = core.getUserInput()
        inputComputer = core.getComputerChoice()

        if core.isValidInput(inputPlayer) == False:
            if inputPlayer == 'Q':
                print("200: Good Bye!")
                break
            print("404: Command not found")
            continue

        if dev:
            print("[DEBUG] Input Player", inputPlayer, "Input CPU", inputComputer)

        print(visualtext.playerTool(inputPlayer))
        print(visualtext.computerTool(inputComputer))
        isWin = core.checkWin(inputPlayer, inputComputer)

        if dev:
            print("[DEBUG] Input Player", inputPlayer, "Input Computer", inputComputer)

        print(visualtext.resultGame(isWin))

main()
