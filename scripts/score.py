from die import Die
from hopper import display

class Score():
    def __init__(self, dice_list):
        '''Takes in a list of dice, any size, and
        and returns a tuple of (dice, points).'''
        # set to true if player uses all six dice and get's 
        # to continue rolling with a new set of dice.
        self.score = 0

        self.in_play_dice = [_ for _ in dice_list if _.in_play]


        if self.check_boxcar(): pass
        elif self.straight(): pass
        else:
            pass


    def check_boxcar(self):
        if len(self.in_play_dice) == 6:
            group = set([_.pip_value for _ in self.in_play_dice])
            if len(group)
            return True
        return False

    def straight(self):
        return False

    #check for ones and fives
    def check_duplicates(self, dice):    
        score = 0
        ones = [_ for _ in dice if _.get_pip_value() == '1']
        twos = [_ for _ in dice if _.get_pip_value() == '2']
        threes = [_ for _ in dice if _.get_pip_value() == '3']
        fours = [_ for _ in dice if _.get_pip_value() == '4']
        fives = [_ for _ in dice if _.get_pip_value() == '5']
        sixes = [_ for _ in dice if _.get_pip_value() == '6']
        # Each number is scored differently, but always increasing 
        # with the number of duplicates.
        score += [100, 200, 1000, 2000, 3000, 4000][len(ones)]
        score += [0, 0, 200, 400, 600, 800][len(twos)]
        score += [0, 0, 300, 600, 900, 1200][len(threes)]
        score += [0, 0, 400, 800, 1200, 1600][len(fours)]
        score += [50, 100, 500, 1000, 1500, 2000][len(fives)]
        score += [0, 0, 600, 1200, 1800, ][len(sixes)]

        
    #check for multiples of three or more
    def check_sets(self, dice):
        pass

    #check for three or more of a number
    

    #check if player gets a new set of dice (all dice are used)

    #Awards the player points and adds dice to 


if __name__ == '__main__':
    dice_list = [Die() for _ in range(6)]
    score = Score(dice_list)

