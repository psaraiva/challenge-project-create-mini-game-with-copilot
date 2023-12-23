def resultGame(isWin):
    if isWin == -1:
        return "You lose"
    elif isWin == 0:
        return "Draw"
    elif isWin == 1:
        return "You win"
    return "unknown"

def playerTool(inputPlayer):
    if inputPlayer == 'R':
        return playerRock()
    if inputPlayer == 'P':
        return playerPaper()
    if inputPlayer == 'S':
        return playerScissors()
    return "unknown"

def computerTool(inputComputer):
    if inputComputer == 'R':
        return computerRock()
    if inputComputer == 'P':
        return computerPaper()
    if inputComputer == 'S':
        return computerScissors()
    return "unknown"

def playerRock():
    return """
    PLAYER
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

def playerScissors():
    return """
    PLAYER
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def playerPaper():
    return """
     PLAYER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

def computerRock():
    return """
    CPU
    _______
   (____   '---
  (_____)
  (_____)
   (____)
    (___)__.---
"""

def computerScissors():
    return """
      CPU
      _______
 ____(____   '---
(______          
(__________       
      (____)
      (___)__.---
"""

def computerPaper():
    return """
      CPU
      _______
 ____(____    '---
(______           
(_______          
 (_______         
   (__________.---
"""
