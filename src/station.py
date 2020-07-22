from engine import Engine
from coach import Player
import csv
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def return_mean(rounds):
    
    engine = Engine('perfect')
    data = list()
    for _ in range(rounds):
        engine.play_round()
        data.append(engine.round_points)
    return np.mean(data)

def define_optimal_sample_size(n=1000):
    f = open('../data/batchtests.csv', 'a')
    for _ in range(100):
        mean = int(return_mean(n))
        f.write(f'{n}, {mean}\n')
        print(_)

def take_sample(vp_name='perfect', n=8000):
    # Returns n number of scores as np.array
    engine = Engine(vp_name)
    f = open(f'../data/{vp_name}1.csv', 'w+')
    f.write('score,outcome\n')
    for _ in range(n):
        engine.play_round()
        f.write(f'{engine.round_points},{engine.state}\n')


if __name__ == '__main__':
    pass

#     print('Who should play?')
#     player_name = input()

#     print('How many rounds per test?')
#     rounds = int(input())

#     print('How many tests?')
#     tests = int(input())

#     player = Player(player_name)
#     f = open(f'{player_name}.csv', 'w+')
#     engine = Engine(player)

   

#     # play round and store results in np_array

#     test_array = np.array([
#         np.mean([
#             engine.play_round()
#             for _ in range(rounds)
#         ])
#             for _ in range(tests)
#     ])

#     test_array.to_csv(f)

# pd.DataFrame.hist(  )