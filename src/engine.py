from cabouse import Score
from hopper import display_win, display_loss
from hopper import log
from coach import Player
import csv

class Engine():
    '''
    The Engine class object drives the simulation. At instantiation, 
    an engine will create the specified player and initialize a score
    object. This is where the round's score is kept, as well as the 
    number of rolls still remaining. The function play_round triggers
    a round to execute. 
    '''
    def __init__(self, player):
        # player and score objects used
        self._player = Player(player)
        self._palyer_name = player
        self._score = Score()
        # A Round starts with 3 dice rolls.
        self._rolls = int() 
        # Round points are not awarded until end of round
        self.round_points = int()
        # [state], is this round a loss or a win
        self.state = bool
        # count used for testing
        self.count = 0
    
#==============================================================================

    def play_round(self):
        # Each player is afforded a turn.
        # Turns are managed on player.py.
        # Rounds continue until a player reaches 10,000 points.
        self.round_points = 0
        [die.reset() for die in self._score.dice]
        self._rolls = 3     

        # Keep rolling until the player loses, chooses to stop, 
        # fails to score, or runs out of rolls           
        # Your turn, bud!
        self._roll_dice()          

#==============================================================================

    def _roll_dice(self):
        self._rolls -= 1
        self._score.roll()
        self.round_points += self._score.points
        self._check_dice()

#==============================================================================

    def _check_dice(self):
        # Check if player scored
        if self._score.points == 0:
            self._lose_round()
        # Check if player used all dice
        elif len([_ for _ in self._score.dice if _.in_play]) == 0:
            self._rolls = 3
            self._ask_player()
        # Check if player has no more rolls, win!!!
        elif self._rolls == 0:
            self._win_round()
        # Check if player wants to roll again
        else:
            self._ask_player()

#==============================================================================
    
    def _ask_player(self):
        # Player must decided wether to roll again or keep points
        choice = self._player.roll_or_stay(self._score.dice, self.round_points)
        if choice:
            self._roll_dice()
        else:
            self._win_round()

#==============================================================================

    def _win_round(self):
        self.state = True
        if self._palyer_name == 'terminal':
            display_win(self._score.dice, self.round_points)

#==============================================================================

    def _lose_round(self):
        self.state = False
        if self._palyer_name == 'terminal':
            display_loss(self._score.dice)

#==============================================================================

if __name__ == '__main__':
    pass