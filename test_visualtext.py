import unittest
from visualtext import *

class TestVisualText(unittest.TestCase):
    def test_menuXbox(self):
        self.assertEqual(menuXbox(), "Please choise: [X]Rock, [A]Paper, [Y]Scissors, [B]Quit: ")

    def test_resultGame(self):
        self.assertEqual(resultGame(-1), "You lose")
        self.assertEqual(resultGame(0), "Draw")
        self.assertEqual(resultGame(1), "You win")
        self.assertEqual(resultGame(10), "unknown")

    def test_playerTool(self):
        self.assertEqual(playerTool("R"), playerRock())
        self.assertEqual(playerTool("P"), playerPaper())
        self.assertEqual(playerTool("S"), playerScissors())
        self.assertEqual(playerTool("A"), "unknown")

    def test_computerTool(self):
        self.assertEqual(computerTool("R"), computerRock())
        self.assertEqual(computerTool("P"), computerPaper())
        self.assertEqual(computerTool("S"), computerScissors())
        self.assertEqual(computerTool("A"), "unknown")

    def test_playerRock(self):
        expect = """
    PLAYER        
    _______       
---'   ____)      
      (_____)     
      (_____)     
      (____)      
---.__(___)       
"""
        self.assertEqual(playerRock(), expect)

    def test_playerScissors(self):
        expect = """
    PLAYER        
    _______       
---'   ____)____  
          ______) 
       __________)
      (____)      
---.__(___)       
"""
        self.assertEqual(playerScissors(), expect)

    def test_playerScissors(self):
        expect = """
    PLAYER        
    ________      
---'    ____)____ 
           ______)
          _______)
         _______) 
---.__________)   
"""
        self.assertEqual(playerPaper(), expect)

    def test_computerRock(self):
        expect = """
    CPU           
    _______       
   (____   '---   
  (_____)         
  (_____)         
   (____)         
    (___)__.---   
"""
        self.assertEqual(computerRock(), expect)

    def test_computerScissors(self):
        expect = """
      CPU         
      _______     
 ____(____   '--- 
(______           
(__________       
      (____)      
      (___)__.--- 
"""
        self.assertEqual(computerScissors(), expect)

    def test_computerPaper(self):
        expect = """
      CPU         
      ________    
 ____(____    '---
(______           
(_______          
 (_______         
   (__________.---
"""
        self.assertEqual(computerPaper(), expect)

    def test_playerRockComputerRock(self):
        expect = """
    PLAYER            CPU           
    _______           _______       
---'   ____)         (____   '---   
      (_____)       (_____)         
      (_____)       (_____)         
      (____)         (____)         
---.__(___)           (___)__.---   
"""
        self.assertEqual(playerRockComputerRock(), expect)

    def test_playerRockComputerPaper(self):
        expect = """
    PLAYER              CPU         
    _______             ________    
---'   ____)       ____(____    '---
      (_____)     (______           
      (_____)     (_______          
      (____)       (_______         
---.__(___)          (__________.---
"""
        self.assertEqual(playerRockComputerPaper(), expect)

    def test_playerRockComputerScissors(self):
        expect = """
    PLAYER              CPU         
    _______             _______     
---'   ____)       ____(____   '--- 
      (_____)     (______           
      (_____)     (__________       
      (____)            (____)      
---.__(___)             (___)__.--- 
"""
        self.assertEqual(playerRockComputerScissors(), expect)

    def test_playerScissorsComputerScissors(self):
        expect = """
    PLAYER              CPU         
    _______             _______     
---'   ____)____   ____(____   '--- 
          ______) (______           
       __________)(__________       
      (____)            (____)      
---.__(___)             (___)__.--- 
"""
        self.assertEqual(playerScissorsComputerScissors(), expect)

    def test_playerScissorsComputerRock(self):
        expect = """
    PLAYER            CPU           
    _______           _______       
---'   ____)____     (____   '---   
          ______)   (_____)         
       __________)  (_____)         
      (____)         (____)         
---.__(___)           (___)__.---   
"""
        self.assertEqual(playerScissorsComputerRock(), expect)

    def test_playerScissorsComputerPaper(self):
        expect = """
    PLAYER              CPU         
    _______             ________    
---'   ____)____   ____(____    '---
          ______) (______           
       __________)(_______          
      (____)       (_______         
---.__(___)          (__________.---
"""
        self.assertEqual(playerScissorsComputerPaper(), expect)

    def test_playerPaperComputerPaper(self):
        expect = """
    PLAYER              CPU         
    ________            ________    
---'    ____)____  ____(____    '---
           ______)(______           
          _______)(_______          
         _______)  (_______         
---.__________)      (__________.---
"""
        self.assertEqual(playerPaperComputerPaper(), expect)

    def test_playerPaperComputerScissors(self):
        expect = """
    PLAYER              CPU         
    ________            _______     
---'    ____)____  ____(____   '--- 
           ______)(______           
          _______)(__________       
         _______)       (____)      
---.__________)         (___)__.--- 
"""
        self.assertEqual(playerPaperComputerScissors(), expect)

    def test_playerPaperComputerRock(self):
        expect = """
    PLAYER            CPU           
    ________          _______       
---'    ____)____    (____   '---   
           ______)  (_____)         
          _______)  (_____)         
         _______)    (____)         
---.__________)       (___)__.---   
"""
        self.assertEqual(playerPaperComputerRock(), expect)

if __name__ == '__main__':
    unittest.main()
