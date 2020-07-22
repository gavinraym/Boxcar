from cabouse import Score
from hopper import display_win, display_loss
from hopper import log
from coach import Player
import csv

class Engine():
    def __init__(self, player):
        # player and score objects used
        self.player = Player(player)
        self.palyer_name = player
        self.score = Score()
        # Round points are not awarded until end of round
        self.round_points = int()
        # A Round starts with 3 dice rolls.
        self.rolls = int()
        # [state], is this round a loss or a win
        self.state = bool
        # count for testing
        self.count = 0
    
#==============================================================================

    def play_round(self):
        # Each player is afforded a turn.
        # Turns are managed on player.py.
        # Rounds continue until a player reaches 10,000 points.
        self.round_points = 0
        [die.reset() for die in self.score.dice]
        self.rolls = 3     

        # Keep rolling until the player loses, chooses to stop, 
        # fails to score, or runs out of rolls           
        # Your turn, bud!
        self.roll_dice()          

#==============================================================================

    def roll_dice(self):
        self.rolls -= 1
        self.score.roll()
        self.round_points += self.score.points
        self.check_dice()

#==============================================================================

    def check_dice(self):
        # Check if player scored
        if self.score.points == 0:
            self.lose_round()
        # Check if player used all dice
        elif len([_ for _ in self.score.dice if _.in_play]) == 0:
            self.rolls = 3
            self.ask_player()
        # Check if player has no more rolls, win!!!
        elif self.rolls == 0:
            self.win_round()
        # Check if player wants to roll again
        else:
            self.ask_player()

#==============================================================================
    
    def ask_player(self):
        # Player must decided wether to roll again or keep points
        choice = self.player.roll_or_stay(self.score.dice, self.round_points)
        if choice:
            self.roll_dice()
        else:
            self.win_round()

#==============================================================================

    def win_round(self):
        self.state = True
        if self.palyer_name == 'terminal':
            display_win(self.score.dice, self.round_points)

#==============================================================================

    def lose_round(self):
        self.state = False
        if self.palyer_name == 'terminal':
            display_loss(self.score.dice)

#==============================================================================

if __name__ == '__main__':
    pass