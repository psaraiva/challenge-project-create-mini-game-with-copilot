import unittest
from visualtext import *

class TestResultGame(unittest.TestCase):
    def test_resultGame(self):
        self.assertEqual(resultGame(-1), "You lose")
        self.assertEqual(resultGame(0), "Draw")
        self.assertEqual(resultGame(1), "You win")
        self.assertEqual(resultGame(10), "unknown")

class TestPlayerTool(unittest.TestCase):
    def test_playerTool(self):
        self.assertEqual(playerTool("R"), playerRock())
        self.assertEqual(playerTool("P"), playerPaper())
        self.assertEqual(playerTool("S"), playerScissors())
        self.assertEqual(playerTool("A"), "unknown")

class TestComputerTool(unittest.TestCase):
    def test_computerTool(self):
        self.assertEqual(computerTool("R"), computerRock())
        self.assertEqual(computerTool("P"), computerPaper())
        self.assertEqual(computerTool("S"), computerScissors())
        self.assertEqual(computerTool("A"), "unknown")

class TestPlayerRock(unittest.TestCase):
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

class TestPlayerScissors(unittest.TestCase):
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

class TestPlayerPaper(unittest.TestCase):
    def test_playerScissors(self):
        expect = """
     PLAYER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
        self.assertEqual(playerPaper(), expect)

class TestComputerRock(unittest.TestCase):
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

class TestComputerScissors(unittest.TestCase):
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

class TestComputerPaper(unittest.TestCase):
    def test_computerPaper(self):
        expect = """
      CPU
      _______
 ____(____    '---
(______           
(_______          
 (_______         
   (__________.---
"""
        self.assertEqual(computerPaper(), expect)

if __name__ == '__main__':
    unittest.main()
