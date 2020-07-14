from coach import Player
from cabouse import Score
from hopper import display
from hopper import log

class Engine():
    def __init__(self, rounds=1):
        # [rounds] indicates how many rounds should be played total
        self.rounds = rounds
        # player and score objects used
        self.player = Player()
        self.score = Score()
        # Round points are not awarded until end of round
        self.round_points = int()
        # A Round starts with 3 dice rolls.
        self.rolls = int()
        # [state], is this round a loss or a win
        self.state = bool
    
#==============================================================================

    def play_round(self):
        # Each player is afforded a turn.
        # Turns are managed on player.py.
        # Rounds continue until a player reaches 10,000 points.
        self.round_points = 0
        self.score.reset_dice()
        self.rolls = 3     

        # Keep rolling until the player loses, chooses to stop, 
        # fails to score, or runs out of rolls
        log(f'Round: rolls = {self.rolls}')            
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
        # Check if player has no more rolls, win!!!
        elif self.rolls == 0:
            self.win_round()
        # Check if player wants to roll again
        else:
            self.ask_player()

#==============================================================================
    
    def ask_player(self):
        # Player must decided wether to roll again or keep points
        if self.player.roll_or_stay(self.score):
            self.roll_dice()
        else:
            self.win_round()

#==============================================================================

    def win_round(self):
        log(f'round won: {self.round_points}')

#==============================================================================

    def lose_round(self):
        log(f'round lost.')

#==============================================================================

if __name__ == '__main__':
    game = Engine()
    game.play_round()