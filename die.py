import random

class Die():
    def __init__(self, die_num):
        self.die_num = die_num
        self.pip_value = int()
        self.in_play = True

    def roll(self):
        if self.in_play:
            self.pip_value = random.randint(1,6)
        return str(self.pip_value)
        
    def set_keep(self):
        self.in_play = False

    def check_in_play(self):
        return self.in_play

    def get_pip_value(self):
        return str(self.pip_value)

    def get_num(self):
        return str(self.die_num)


if __name__ == '__main__':
    
    pass
