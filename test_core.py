import unittest
from core import *

class TestGetComputerChoice(unittest.TestCase):
    def test_getComputerChoice(self):
        got = getComputerChoice()
        assert got in inputTool

class TestCheckWin(unittest.TestCase):
    def test_checkWin(self):
        self.assertEqual(checkWin('R', 'R'), 0)
        self.assertEqual(checkWin('R', 'S'), 1)
        self.assertEqual(checkWin('P', 'R'), 1)
        self.assertEqual(checkWin('S', 'P'), 1)
        self.assertEqual(checkWin('R', 'P'), -1)
        self.assertEqual(checkWin('P', 'S'), -1)
        self.assertEqual(checkWin('S', 'R'), -1)

if __name__ == '__main__':
    unittest.main()
