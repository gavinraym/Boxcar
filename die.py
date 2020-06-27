import random

class Die():
    def __init__(self, die_num):
        self.die_num = die_num
        self.value = int()
        self.in_play = True

    def roll(self):
        if self.in_play:
            self.value = random.randint(1,6)
        
    def set_keep(self):
        self.in_play = False

    def get_value(self):
        return self.value

if __name__ == '__main__':
    pass
