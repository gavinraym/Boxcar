from engine import Engine
from coach import Player
import csv

if __name__ == '__main__':
    print('Who should play?')
    player_name = input()
    player = Player(player_name)
    f = open(f'{player_name}', 'w+')
    f.write(f'{player_name}\nscore, success\n')
    engine = Engine(player, f)
    print('How many times?')
    n = int(input())
    for _ in range(n):
        engine.play_round()

    


