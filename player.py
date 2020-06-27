from die import Die
import sys
import time
import random

class Player():
    def __init__(self, player_num):
        self.player_num = player_num
        self.name = str(input("What is Player {}'s name: ".format(player_num)))
        self.score = 0
        self.dice_list

    def __str__(self):
        return f"{self.name} has a score of: {self.score}"

    def get_score(self):
        return self.score

    def take_turn(self):
        # Each turn consists of three stages.
        # First two stages end with the player choosing 
        # which dice to keep.
        self.dice_list = [Die(i) for i in range(1,7)]
        self.roll_dice()
        self.choose_dice()
        self.roll_dice()
        self.choose_dice()
        self.roll_dice()
        self.finish_turn()

    def roll_dice(self):
        # Dice still marked as 'in_play' are rolled.
        stdout = ''
        print(f'{self.name} is rolling...')
        print(stdout)
        for dice in self.dice_list:
            if dice.in_play:
                for _ in range(10):
                    sys.stdout.write(stdout, ' ', random.randint(1,6))
                    time.sleep(.1)
                dice.roll()
                stdout = stdout + ' ' + dice.get_value()
            print(f"Die number :{dice} rolled a :{dice.roll}")
        
    def choose_dice(self):
        # Player can choose to un-mark dice as 'in_play'
        # Only 'in_play' dice are rolled.
        usr_input = input("Which dice would you like to keep: ")
        for dice in self.dice_list:
            if str(dice.die_num) in usr_input:
                dice.set_keep()

    def finish_turn(self):
        # calculate dice score here, then update player.score and finish turn
        print('error: finish turn method is unfinished.')
        pass


if __name__ == '__main__':
    pl = Player(1)
    pl.take_turn()
