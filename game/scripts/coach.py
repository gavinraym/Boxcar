from hopper import log

class Player():
    '''This script houses all the different players (located in the 
    /passengers directory). One must be indicated at instantiation
    with a string [name].'''
    def __init__(self, name):
        self.roll = True
        self.stay = False

        self.funcs = {
            'karen' : self.karen,
            'wyatte' : self.wyatte,
            'perfect' : self.perfect
        }
        
        self.name = self.funcs[name]
        self.dice = None
        self.score = int()

    def roll_or_stay(self, dice, score):
        self.dice = dice
        self.score = score
        return self.name()



#==============================================================================

    #### All players are seated below this point.

    # Each player evaluates their choice differenly. But each has to
    # take number of dice and points, returns boolean indicating whether
    # to keep rolling (True), or keep the points and stop (False).

#==============================================================================

    def wyatte(self):
        dice_list = [_ for _ in self.dice if _.in_play]

        if len(dice_list) >= 2:
            return self.roll
        else:
            return self.stay

#==============================================================================

    def karen(self):
        if self.score > 750:
            return self.stay
        else:
            return self.roll
#==============================================================================

    def stan(self, dice):
        pass

#==============================================================================

    def perfect(self):
        log('perfect\'s turn')
        return self.roll

#==============================================================================

    def terminal(self):
        pass
    # Choosing terminal allows you to play! (Not finished)
    # playable_dice = [_ for _ in dice if _.check_in_play()]
    # stdout = 'Which dice would you like to keep:\n'
    # for dice in dice:
    #     stdout = stdout + ' ' + dice.get_pip_value()
    #     stdout = stdout + '\n ^ ^ ^ ^ ^ ^\n 1 2 3 4 5 6'
    #     display(stdout)
    #     usr_input = input()
    #     for dice in self.dice_list:
    #         if dice.get_num() in usr_input:
    #             dice.set_keep()
    #     if len(playable_dice) == len([_ for _ in self.dice_list if _.check_in_play()]):
    #         display('You must choose at least one die!', 3)
    #         self.choose_dice()

    # def roll_display(self):
    #     # Dice still marked as 'in_play' are rolled.
    #     for _ in range(10):
    #         stdout = ''
    #         for dice in self.dice_list:
    #             if dice.in_play:
    #                 stdout = stdout + ' ' + dice.roll()
    #             else:
    #                 stdout = stdout + ' ' + dice.get_pip_value()

    #         display(str(self.name + ' is rolling...\n' + stdout), .25)

        