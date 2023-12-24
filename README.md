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
`Please choise: (R)ock, (P)aper, (S)cissors, (Q)uit:`
- **R** or **r** to choose rock
- **P** or **p** to choose paper
- **S** or **s** to choose scissors
- **Q** or **q** to quit game

### Tools:
```
    (R)ock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
```

```
     (P)aper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
```
```
    (S)cissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
```

## Commands
Run the game
```shell
python app.py
```

Run all tests units
```shell
python -m unittest
```

Run by files test unit
```shell
python -m unittest test_core.py
python -m unittest test_visualtext.py
```

Thanks