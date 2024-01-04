# Challenge Project: Create mini game with Copilot

[challenge](https://learn.microsoft.com/pt-br/training/modules/challenge-project-create-mini-game-with-copilot/)

## How does it work?
### Table rules:
```
+-------------------------------------+
| tool     | vs | tool     | win      |
|----------+----+----------+----------+
| rock     | vs | scissors | rock     |
| scissors | vs | papaer   | scissors |
| papaer   | vs | rock     | papaer   |
| rock     | vs | rock     | -        |
| scissors | vs | scissors | -        |
| papaer   | vs | papaer   | -        |
+-------------------------------------+

```

### Menu:
```
Please choise: (R)ock, (P)aper, (S)cissors, (Q)uit:
```
- **R** or **r** to choose rock
- **P** or **p** to choose paper
- **S** or **s** to choose scissors
- **Q** or **q** to quit game

### Tools:
```
    Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
```

```
     Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
```
```
    Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
```

## Outputs
Rock vs Rock
```
    PLAYER            CPU           
    _______           _______       
---'   ____)         (____   '---   
      (_____)       (_____)         
      (_____)       (_____)         
      (____)         (____)         
---.__(___)           (___)__.---   

Draw
```
Rock vs Paper
```
    PLAYER              CPU         
    _______             ________    
---'   ____)       ____(____    '---
      (_____)     (______           
      (_____)     (_______          
      (____)       (_______         
---.__(___)          (__________.---

You lose
```
Rock vs Scissors
```
    PLAYER              CPU         
    _______             _______     
---'   ____)       ____(____   '--- 
      (_____)     (______           
      (_____)     (__________       
      (____)            (____)      
---.__(___)             (___)__.--- 

You win
```
Scissors vs Scissors
```
    PLAYER              CPU         
    _______             _______     
---'   ____)____   ____(____   '--- 
          ______) (______           
       __________)(__________       
      (____)            (____)      
---.__(___)             (___)__.--- 

Draw
```
Scissors vs Rock
```
    PLAYER            CPU           
    _______           _______       
---'   ____)____     (____   '---   
          ______)   (_____)         
       __________)  (_____)         
      (____)         (____)         
---.__(___)           (___)__.---   

You lose
```
Scissors vs Paper
```
    PLAYER              CPU         
    _______             ________    
---'   ____)____   ____(____    '---
          ______) (______           
       __________)(_______          
      (____)       (_______         
---.__(___)          (__________.---

You win
```
Paper vs Paper
```
    PLAYER              CPU         
    ________            ________    
---'    ____)____  ____(____    '---
           ______)(______           
          _______)(_______          
         _______)  (_______         
---.__________)      (__________.---

Draw
```
Paper vs Scissors
```
    PLAYER              CPU         
    ________            _______     
---'    ____)____  ____(____   '--- 
           ______)(______           
          _______)(__________       
         _______)       (____)      
---.__________)         (___)__.--- 

You lose
```
Paper vs Rock
```
    PLAYER            CPU           
    ________          _______       
---'    ____)____    (____   '---   
           ______)  (_____)         
          _______)  (_____)         
         _______)    (____)         
---.__________)       (___)__.---   

You win
```

## Using Xbox 360 Controller (only Windows)
```
Please choise: [X]Rock, [A]Paper, [Y]Scissors, [B]Quit:
```
Execute `python winxbox.py`

## Commands
Run the game
```shell
python main.py
```

Run all tests units
```shell
python -m unittest
```

Run by files test unit
```shell
python -m unittest test_core.py
python -m unittest test_visualtext.TestVisualText
python -m unittest test_visualtext.TestVisualText.test_playerPaperComputerRock
```

Thanks
