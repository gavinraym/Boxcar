from player import Player

class Engine():
    def __init__(self):
        self.players = list()
        for i in range(int(input("Number of players: "))):
            self.players.append(Player(i+1))
    
    def play_round(self):
        # Each player is afforded a turn.
        # Turns are managed on player.py.
        # Rounds continue until a player reaches 10,000 points.
        for player in self.players:
            player.take_turn()
            print('Current score: ', player)

    def end_game(self):
        # declare winner (etc) here.
        pass
            
if __name__ == '__main__':
    game = Engine()
    game.play_round()