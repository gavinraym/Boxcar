import random
class Die():
    def __init__(self):
        self.pip_value = random.randint(1,6)
        self.in_play = True
        # Tells hopper if this dice should show as rolling
        self.show = True
    def roll(self):
        if self.in_play:
            self.pip_value = random.randint(1,6)
    def freeze(self):
        self.in_play = False
    def pips(self):
        return self.pip_value if self.in_play else 0
    def reset(self):
        self.in_play = True
        self.show = True
        self.pip_value = random.randint(1,6)

if __name__ == '__main__':
    pass


