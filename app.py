from __future__ import division, print_function

import arguments
import sys
from Game import Game
from bots import *
from Player import Player


# Change these to edit the default Game parameters
DEFAULT_VERBOSITY = True
DEFAULT_MIN_ROUNDS = 300
DEFAULT_AVERAGE_ROUNDS = 1000
DEFAULT_END_EARLY = False
DEFAULT_PLAYERS = ([Player()] * 5) + ([Player1()] * 5) + ([Player2()] * 5) + ([Player3(0.0001)] * 5) + ([Freeloader()] * 5) + ([Alternator()] * 1) + ([MaxRepHunter()] * 5) + ([Random(0.3)] * 2) + ([Random(0.96)] * 2) + ([FairHunter()] * 2) + ([BoundedHunter(0.8,0.999)] * 5) + ([AverageHunter()] * 3) + ([Pushover()] * 1) 


# Bare minimum test game. See README.md for details.

if __name__ == '__main__':
    (players, options) = arguments.get_arguments()
    # The list of players for the game is made up of
    #   'Player' (your strategy)
    #   bots from get_arguments (the bots to use)
    player_list = players
    # **options -> interpret game options from get_arguments
    #              as a dictionary to unpack into the Game parametersi

    winnerMap = {}
    for i in range(200) :
        game = Game(player_list, **options)
        
        winner = game.play_game()
        print ("Winner: " + winner)
        sys.stdout.flush()
        if (not winner in winnerMap):
            winnerMap[winner] = 1
        else :
            winnerMap[winner] += 1;
    print (str(winnerMap))