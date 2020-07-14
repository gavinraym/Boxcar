from bum import Die
from hopper import log
import time
import random

class Player():
    def __init__(self):
        pass
#==============================================================================

    def roll_or_stay(self, score):
    # Takes number of dice and points, returns boolean indicating whether
    # to keep rolling (True), or keep the points and stop (False).

        dice_list = [_ for _ in score.dice if _.in_play]
        log(f'Player dice length {len(dice_list)}')
        roll = True
        stay = False
        if len(dice_list) >= 3:
            log('Player rolls!')
            return roll
        elif len(dice_list) == 2 and score.points < 500:
            log('Player rolls!')
            return roll
        else:
            log('Player stays!')
            return stay