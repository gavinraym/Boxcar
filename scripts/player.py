from die import Die
from hopper import display, score_this
import time
import random
from turn import Turn

class Player():
    def __init__(self, player_num):
        self.player_num = player_num
        self.name = str(input("What is Player {}'s name: ".format(player_num)))
        # self.score is the players total score for the game, not turn score
        self.score = 0

    def __str__(self):
        return f"{self.name} has a score of: {self.score}"

    def get_score(self):
        # only used by engine to check if player has enough points to win
        return self.score

        if win == False:
            print('Ya basic')

        print('error: finish turn method is unfinished.')
        pass

    def take_turn(self, turn_score=0):
        # Each turn consists of three stages.
        # First two stages end with the user choosing 
        # which dice to keep.
        #  
        # turn score is used when user receives a new set of dice to 
        # play with (i.e. player used all 6 dice to score.)
        #
        # dice score is used to keep track of this set of dice's score

        dice_score = 0
        # Instantiate the dice
        self.dice_list = [Die(i) for i in random.randint(1,6)]

        # Player is given a first roll
        self.roll_dice()
        self.choose_dice()
        if dice_score >= score_this(self.dice_list):
            self.finish_turn(False)

        #player receives a second roll
        else:
            dice_score = score_this(self.dice_list)        
            self.roll_dice()
            self.choose_dice()
            if dice_score >= score_this(self.dice_list): 
                self.finish_turn(False)
            
            #player receives a third roll
            else:
                self.roll_dice()   
                if dice_score >= score_this(self.dice_list):
                    self.finish_turn(False)
                else:
                    self.finish_turn()

    def roll_dice(self):
        # Dice still marked as 'in_play' are rolled.
        for _ in range(10):
            stdout = ''
            for dice in self.dice_list:
                if dice.in_play:
                    stdout = stdout + ' ' + dice.roll()
                else:
                    stdout = stdout + ' ' + dice.get_pip_value()

            display(str(self.name + ' is rolling...\n' + stdout), .25)
        
    def choose_dice(self):
        # Player can choose to un-mark dice as 'in_play'
        # Only 'in_play' dice are rolled.
        playable_dice = [_ for _ in self.dice_list if _.check_in_play()]
        stdout = 'Which dice would you like to keep:\n'
        for dice in self.dice_list:
            stdout = stdout + ' ' + dice.get_pip_value()
        stdout = stdout + '\n ^ ^ ^ ^ ^ ^\n 1 2 3 4 5 6'
        display(stdout)
        usr_input = input()
        for dice in self.dice_list:
            if dice.get_num() in usr_input:
                dice.set_keep()
        if len(playable_dice) == len([_ for _ in self.dice_list if _.check_in_play()]):
            display('You must choose at least one die!', 3)
            self.choose_dice()

    def finish_turn(self, win=True):
        # If win == True, update player.score and finish turn, next player can steal
        # Else the player loses
        # if player receives scoring points from all six dice
        # player is given a new set of dice
        if len(score_this(dice_list)[1])
            turn_score = turn_score +

if __name__ == '__main__':
    pl = Player(1)
    pl.take_turn()