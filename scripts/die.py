import random

class Die():
    def __init__(self):
        self.pip_value = random.randint(1,6)
        self.in_play = True
