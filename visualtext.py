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
    ________      
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
      ________    
 ____(____    '---
(______           
(_______          
 (_______         
   (__________.---
"""

def playerRockComputerRock():
    return """
    PLAYER            CPU           
    _______           _______       
---'   ____)         (____   '---   
      (_____)       (_____)         
      (_____)       (_____)         
      (____)         (____)         
---.__(___)           (___)__.---   
"""

def playerRockComputerPaper():
    return """
    PLAYER              CPU         
    _______             ________    
---'   ____)       ____(____    '---
      (_____)     (______           
      (_____)     (_______          
      (____)       (_______         
---.__(___)          (__________.---
"""

def playerRockComputerScissors():
    return """
    PLAYER              CPU         
    _______             _______     
---'   ____)       ____(____   '--- 
      (_____)     (______           
      (_____)     (__________       
      (____)            (____)      
---.__(___)             (___)__.--- 
"""

def playerScissorsComputerScissors():
    return """
    PLAYER              CPU         
    _______             _______     
---'   ____)____   ____(____   '--- 
          ______) (______           
       __________)(__________       
      (____)            (____)      
---.__(___)             (___)__.--- 
"""

def playerScissorsComputerRock():
    return """
    PLAYER            CPU           
    _______           _______       
---'   ____)____     (____   '---   
          ______)   (_____)         
       __________)  (_____)         
      (____)         (____)         
---.__(___)           (___)__.---   
"""

def playerScissorsComputerPaper():
    return """
    PLAYER              CPU         
    _______             ________    
---'   ____)____   ____(____    '---
          ______) (______           
       __________)(_______          
      (____)       (_______         
---.__(___)          (__________.---
"""

def playerPaperComputerPaper():
    return """
    PLAYER              CPU         
    ________            ________    
---'    ____)____  ____(____    '---
           ______)(______           
          _______)(_______          
         _______)  (_______         
---.__________)      (__________.---
"""

def playerPaperComputerScissors():
    return """
    PLAYER              CPU         
    ________            _______     
---'    ____)____  ____(____   '--- 
           ______)(______           
          _______)(__________       
         _______)       (____)      
---.__________)         (___)__.--- 
"""

def playerPaperComputerRock():
    return """
    PLAYER            CPU           
    ________          _______       
---'    ____)____    (____   '---   
           ______)  (_____)         
          _______)  (_____)         
         _______)    (____)         
---.__________)       (___)__.---   
"""
