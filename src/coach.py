from hopper import display_rolling
from hopper import display_choice
import random

class Player():
    '''This script houses the VPs. One must be indicated at instantiation
    with a string [name].'''
    def __init__(self, name='perfect', COE=None):
        self._funcs = {
            'perfect' : self.perfect,
            'random' : self.random,
            'gavin' : self.gavin,
            'terminal' : self.terminal,
            'custom' : self.custom,
            'generate_AI_data' : self.generate_AI_data
        }
        self._name = self._funcs[name]
        self.COE = COE
        self.ten_scores = list()
        self.five_scores = list()
        if name == 'generate_AI_data': 
            self.file = open('data/AI_train_data.csv', 'w')
            self.file.write('score,1,2,3,4,5,6,num_rolls,target\n')

    def roll_or_stay(self, dice, score, num_rolls, past_rolls):
        return self._name(dice, score, num_rolls, past_rolls)



#==============================================================================

    #### All players are seated below this point.

    # Each player evaluates their choice differenly. But each has to
    # take number of dice and points, returns boolean indicating whether
    # to keep rolling (True), or keep the points and stop (False).

#==============================================================================

    def perfect(self, dice, score, num_rolls, past_rolls):
        # This VP always rolls.
        return True

#==============================================================================

    def random(self, dice, score, num_rolls, past_rolls):
        # This VP randomly chooses whether to roll.
        return random.choice([True, False])

#==============================================================================

    def gavin(self, dice, score, num_rolls, past_rolls):
        # This VP is based solely on current score.

        # COE to account for current round score
        COE = {1:350,2:450,3:650,4:800,5:1200,0:1500,}
        #prob = 1 if 
# Use round score and past rolls at first, then we will find out later if those rows affect it

        if score < 350:
            return True




        elif score > 1000:
            return False
        else:
            return random.choice([True, False])
#==============================================================================

    def terminal(self, dice, score, num_rolls, past_rolls):
    # Choosing terminal allows you to play!
        display_rolling(dice)
        display_choice(dice, score)
        return input() in ['y','Y','yes','Yes','YES']

#==============================================================================

    def custom(self, dice, score, num_rolls, past_rolls):
        # Custom uses the coefficients defined at instantiation. This VP
        # was made to allow for testing various COE in order to find the  
        # best possible play style. See chapter 5 for more details.
        num = len([_ for _ in dice if _.in_play])
        return score < self.COE[num]

#==============================================================================
    
    def generate_AI_data(self, dice, score, num_rolls, past_rolls):
        data_list = [score,0,0,0,0,0,0,num_rolls]
        for die in dice:
            data_list[die.pip_value] += 1
        self.file.write(','.join([str(_) for _ in data_list]))
        return True
        

#==============================================================================

    def example(self, dice, score, num_rolls, past_rolls):
        # Feel free to use this example method when creating your own
        # VP. Change the name [example] to the name you specified in
        # _funcs, and write your code below! 

        # [dice] is the list of dice objects used to play the game.
        # You can check how many dice are still in play like this: 
        number_of_in_play_dice = len([_ for _ in dice if _.in_play])
        # This is the number of dice that you will roll if you choose
        # to keep rolling.

        # [score] is the current round score. This is the number of 
        # points you stand to lose if your next roll fails. 

        # Your method needs to return a True or False value. The way 
        # your VP makes that choice is up to you!

if __name__ == '__main__':
    pass
