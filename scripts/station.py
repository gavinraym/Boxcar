from engine import Engine
from coach import Player
import csv
import argparse

if __name__ == '__main__':
    '''ap = argparse.ArgumentParser()'''



    print('Who should play?')
    player_name = input()

    print('How many times?')
    n = int(input())

    player = Player(player_name)
    f = open(f'{player_name}.csv', 'w+')
    f.write(f'{player_name},score,success\n')
    engine = Engine(player, f)

    for _ in range(n):
        engine.play_round()

    # data = pd.read_csv(f'{player_name}.csv, index_col=f'{player_name'}) 