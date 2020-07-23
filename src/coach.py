from hopper import log, display_choice, display_rolling
import random

class Player():
    '''This script houses the VPs. One must be indicated at instantiation
    with a string [name] that matches one of.'''
    def __init__(self, name):
        self.funcs = {
            'karen' : self.karen,
            'wyatte' : self.wyatte,
            'perfect' : self.perfect,
            'random' : self.random,
            'terminal' : self.terminal,
            'judy' : self.judy
        }
        self.name = self.funcs[name]

    def roll_or_stay(self, dice, score):
        return self.name(dice, score)



#==============================================================================

    #### All players are seated below this point.

    # Each player evaluates their choice differenly. But each has to
    # take number of dice and points, returns boolean indicating whether
    # to keep rolling (True), or keep the points and stop (False).

#==============================================================================

    def wyatte(self, dice, score):
        # This VP is based solely on the probability of rolling a success. 
        # In Boxcar, there is a less than 50% chance of scoring when rolling
        # with 2 or less dice, and a greater than 50% chance of scoring with 
        # 3 or more dice.
        return len([_ for _ in dice if _.in_play]) >= 2

#==============================================================================

    def karen(self, dice, score):
        # This VP is based solely on current score.
        if score < 350:
            return True
        elif score > 1000:
            return False
        else:
            return self.wyatte(dice,score)

#==============================================================================

    def perfect(self, dice, score):
        # This VP always rolls.
        return True

#==============================================================================

    def random(self, dice, score):
        # This VP randomly chooses whether to roll.
        return random.choice([True, False])

#==============================================================================

    def terminal(self, dice, score):
    # Choosing terminal allows you to play!
        display_rolling(dice)
        display_choice(dice, score)
        return input() in ['y','Y','yes','Yes','YES']

#==============================================================================

    def judy(self, dice, score):
        # A more sophisticated player
        map = {1:200,2:400,3:600,4:800,5:1100,6:1500,0:2500}
        num = len([_ for _ in dice if _.in_play])
        return score < map[num]