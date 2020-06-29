class Score():
    def __init__(self):

        self.used_dice = set()
        # set to true if player uses all six dice and get's 
        # to continue rolling with a new set of dice.
        self.score = check_sets + 
        self.extra_turn = False


    
    def check_extra_turn(self):
        self.extra_life = len(used_dice) == 6

    #check for ones and fives
    def check_duplicates(self, dice):
        score = 0
        ones = [_ for _ in dice if _.get_pip_value() == '1']
        twos = [_ for _ in dice if _.get_pip_value() == '2']
        threes = [_ for _ in dice if _.get_pip_value() == '3']
        fours = [_ for _ in dice if _.get_pip_value() == '4']
        fives = [_ for _ in dice if _.get_pip_value() == '5']
        sixes = [_ for _ in dice if _.get_pip_value() == '6']
        #ones give 100 points each, but 1000 for 3 and 1000 more for
        # each additional i.e (100, 200, 1000, 2000, 3000, 4000max)
        score += [100, 200, 1000, 2000, 3000, 4000][len(ones)]
        score += [0, 0, 200, 400, 600, 800][len(twos)]
        score += [0, 0, 300, 600, 900, 1200][len(threes)]
        score += [0, 0, 400, 800, 1200, 1600][len(fours)]
        score += [50, 100, 500, 1000, 1500, 2000][len(fives)]
        score += [0, 0, 600, 1200, 1800, ][len(sixes)]

        
    #check for multiples of three or more
    def check_sets(self, dice)

    #check for three or more of a number
    def check_

    #check if player gets a new set of dice (all dice are used)

