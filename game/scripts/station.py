from engine import Engine
from coach import Player
import csv
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def return_mean(rounds, tests):
    engine = Engine('perfect')
    for _ in range(tests):
        data = list()
        for _ in range(rounds):
            engine.play_round()
            data.append(engine.round_points)
        return np.mean(data)

def return_perfect_sample(rounds, tests):
    # Returns n number of scores as np.array
    engine = Engine('perfect')
    f = open(f'perfect{rounds}_{tests}.csv', 'w+')
    for _ in range(tests):
        data = list()
        for _ in range(rounds):
            engine.play_round()
            data.append(engine.round_points)
        f.write(f'{int(np.mean(data))}\n')

def define_optimal_sample_size():
    f = open('../data/prelim/batchtests.csv', 'a')
    #f.write('batch_size,mean\n')
    for batches in range(3001, 4000, 100):
        for _ in range(25):
            mean = int(return_mean(batches, 1))
            f.write(f'{batches}, {mean}\n')




def define_optimal_number_of_samples():
    pass

if __name__ == '__main__':
    '''ap = argparse.ArgumentParser()'''


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