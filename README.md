# Any Dice simulator

      ____                ____             ____
     /\' .\    _____     /\' .\   _____   /\' .\   _____
    /: \___\  / .  /\   /: \___\ / .  /\ /: \___\ / .  /\
    \' / . / /____/..\  \' / . //____/..\\' / . //____/..\ 
     \/___/  \'  '\  /   \/___/ \'  '\  / \/___/ \'  '\  /
              \'__'\/            \'__'\/          \'__'\/

A Python package to roll any dice combo!

### Installation
```python
pip3 install Any-Dice-Simulator
```
## Usage
### Quick Use
Import the core function using:
```python
from anyDiceSimulator import myfunctions
```
Roll a dice combo:
Example: If you need to roll a 6 sided die 5 times, input 5d6
```python
myfunctions.rolldice('5d6')
```
### Detailed Use
import the die classes using:
```python
from anyDiceSimulator import dieclasses
```
The dieclasses module contains the following classes:
1. **Die** :
      - **Inputs**:  
            - *sides*: Number of sides (Default :6)  
            - *numOnSides*: Die face values (Defualt: [1, 2, 3, 4, 5, 6]  
      - **Functions**:  
            - *dieProperties*: Current state of the Die [Number of sides, Face values, biased?, Bias weights]  
            - *rollDie*:  
                  - *Inputs*:  
                        - n (Int): Number of times the die needs to be rolled  
                  - *Output*:  
                        - Roll result (List): List of roll results  
                        - Sum of Roll results (Int)  
#### Sample Usage:
```python
die1 = Die()
die1.dieProperties() # Print the die properties - (1)
result, sumR = die1.rollDie(100) # Roll the die 100 times - (2)
print(f"Rolling... {result}")
print(f"Sum: {sumR}")
```
Result:
```
(1) -> 
==========================================
Die properties ->
Number of sides: 6
Numbering on sides: [1, 2, 3, 4, 5, 6]
Biased: False
Side weights: None
==========================================

(2) ->
Number of rolls: 100
Rolling... [4, 5, 3, 6, 4, 4, 3, 4, 3, 2, 4, 5, 2, 4, 6, 1, 3, 5, 5, 6, 2, 5, 3, 4, 1, 5, 2, 2, 5, 3, 5, 2, 5, 2, 5, 3, 1, 4, 1, 5, 1, 3, 4, 6, 4, 5, 3, 4, 2, 3, 3, 4, 3, 3, 6, 3, 6, 3, 3, 6, 3, 1, 6, 4, 1, 4, 6, 2, 3, 1, 6, 3, 5, 1, 4, 4, 6, 6, 2, 3, 4, 6, 5, 6, 1, 6, 2, 4, 2, 5, 6, 1, 6, 5, 3, 2, 6, 4, 1, 4]
Sum: 369
```

### Todo [Not exhaustive]
- [ ] Add subclasses for common die sets (d20, d50, d100, etc.)
- [x] Add functionality to roll biased die
- [ ] Functionality to roll multiple types of die at once
- [x] Try an object oriented approach with the code
- [ ] Add external random number generators
- [ ] Add dice rolling graphic

