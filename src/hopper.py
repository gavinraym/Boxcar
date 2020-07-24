from os import system, name
import time
import random
    
"""
A Hopper is a type of traincar. It's steep sides allow for
    the transportation of large quantities of raw material,
    like coal. This class does the same for the boxcar game.
    It containes functions for the other objects to use, mainly
    for displaying information to the terminal.
"""

#==============================================================================

# Prints a log to terminal. Used in testing.
def log(logstring):
    print(f'log: {logstring}')

#==============================================================================

def clear():
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear')

#==============================================================================

def display_dice(dice):
    clear()
    print(' '.join([str(die.pip_value) for die in dice]))
    
#==============================================================================

def display_rolling(dice):
    # Runs animation of dice rolling.
    for _ in range(5):
        clear()
        pips = []
        for die in dice:
            if die.show:
                pips.append(str(random.choice([1,2,3,4,5,6])))
            else:
                pips.append(str(die.pip_value))
        print(' '.join(pips))
        print(' '.join(['^' if die.show else ' ' for die in dice]))
        time.sleep(.1)
    for die in dice:
        die.show = die.in_play


#==============================================================================

def display_win(dice, score):
    display_dice(dice)
    print('\n\nCongrats on the win!')
    print(f'\n\n{score} points recorded.')
    input()

#==============================================================================

def display_loss(dice):
    display_rolling(dice)
    display_dice(dice)
    print('\n\nIf you learn from a loss you have not lost.')
    input()

#==============================================================================

def display_choice(dice, score):
    num = len([_ for _ in dice if _.in_play])
    display_dice(dice)
    if num > 0:
        print(' '.join(['^' if die.in_play else ' ' for die in dice]))
        print(f'\n\nCurrent Score: {score}')
        print(f'\nCurrent Dice: {num}')
    else:
        print('^ ^ ^ ^ ^ ^')
        print(f'\n\nCurrent Score: {score}')
        print(f'\nCurrent Dice: 6')

    print(f'\n\nAre you going to keep rolling? (y/n)')


    

  