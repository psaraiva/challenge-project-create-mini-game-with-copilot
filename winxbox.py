from __future__ import print_function
from inputs import get_gamepad
import os
import core
import visualtext

dev = False

def main():
    print(visualtext.menuXbox())
    while True:
        events = get_gamepad()
        inputPlayer = idenifyCommand(events)
        inputComputer = core.getComputerChoice()

        if core.isValidInput(inputPlayer) == False:
            if inputPlayer == 'Q':
                print("200: Good Bye!")
                break
            continue

        os.system('cls')
        print(visualtext.menuXbox())

        if dev:
            print("[DEBUG] Input Player", inputPlayer, "Input CPU", inputComputer)
        print(core.printResultLandscape(inputPlayer, inputComputer))
        isWin = core.checkWin(inputPlayer, inputComputer)

        if dev:
            print("[DEBUG] Input Player", inputPlayer, "Input Computer", inputComputer)
        print(visualtext.resultGame(isWin))

def idenifyCommand(events):
    for event in events:
        if event.code == "BTN_SOUTH" and event.state == 1: #A
            return "P"
        elif event.code == "BTN_EAST" and event.state == 1: #B
            return "Q"
        elif event.code == "BTN_NORTH" and event.state == 1: #Y
            return "S"
        elif event.code == "BTN_WEST" and event.state == 1: #X
            return "R"
    return "unknown"

if __name__ == "__main__":
    main()
