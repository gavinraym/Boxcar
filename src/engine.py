from cabouse import Score
from coach import Player
from hopper import display_win, display_loss
import csv

class Engine():
    '''
    The Engine class object drives the simulation. At instantiation, 
    an engine will create the specified player and initialize a score
    object. This is where the round's score is kept, as well as the 
    number of rolls still remaining. The function play_round triggers
    a round to execute. 
    '''
    def __init__(self, player, COE=None):
        # player and score objects used
        self._player = Player(player, COE)
        self._player_name = player
        self._score = Score()
        # A Round starts with 3 dice rolls.
        self._rolls = int() 
        # Past roll's success or failure can be used by ambitious VP's...
        self._past_rolls = list()   
        # Round points are not awarded until end of round
        self.round_points = int()

    
#==============================================================================

    def play_round(self):
        # Each player is afforded a turn.
        # Turns are managed on player.py.
        # Rounds continue until a player reaches 10,000 points.
        self.round_points = 0
        [die.reset() for die in self._score.dice]
        self._rolls = 3     
        self._past_rolls = self._past_rolls[:9]

        # Keep rolling until the player loses, chooses to stop, 
        # fails to score, or runs out of rolls           
        # Your turn, bud!
        self._roll_dice()          

#==============================================================================

    def _roll_dice(self):
        # Players are given three rolls... unless they score with 6 dice!
        self._rolls -= 1
        self._score.roll()
        # Each round accumulates points until the end
        self.round_points += self._score.points
        # Check if player scored
        if self._score.points == 0:
            self._lose_round()
        # Check if player has used all dice to score
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
        # Add success to past rolls list
        self._past_rolls.append(1)
        # Player must decided wether to roll again or keep points
        choice = self._player.roll_or_stay(
                                    self._score.dice,
                                    self.round_points,
                                    self._rolls,
                                    self._past_rolls)
        if choice:
            self._roll_dice()
        else:
            self._win_round()

#==============================================================================

    def _win_round(self):
        # Add success to past rolls list
        self._past_rolls.append(1)
        # terminal is used for human players
        if self._player_name == 'terminal':
            display_win(self._score.dice, self.round_points)
        if self._player_name == 'generate_AI_data':
            self._player.file.write(',1\n')

#==============================================================================

    def _lose_round(self):
        # Add failure to past rolls list
        self._past_rolls.append(0)
        # If a loss, lose all points for this round
        if self._player_name != 'perfect':
            self.round_points = 0
        # terminal is used for human players
        if self._player_name == 'terminal':
            display_loss(self._score.dice)
        if self._player_name == 'generate_AI_data':
            self._player.file.write(',0\n')

#==============================================================================

if __name__ == '__main__':
    pass
