from __future__ import division, print_function

import arguments
from Game import Game
from bots import *
from Player import Player


# Change these to edit the default Game parameters
DEFAULT_VERBOSITY = True
DEFAULT_MIN_ROUNDS = 300
DEFAULT_AVERAGE_ROUNDS = 1000
DEFAULT_END_EARLY = False
DEFAULT_PLAYERS = ([Player()] * 3) + ([Freeloader()] * 20) + ([Alternator()] * 1) + ([MaxRepHunter()] * 20) + ([Random(0.3)] * 2) + ([Random(0.96)] * 2) + ([FairHunter()] * 2) + ([BoundedHunter(0.8,0.999)] * 14) + ([AverageHunter()] * 3) + ([Pushover()] * 1) 

# Bare minimum test game. See README.md for details.

if __name__ == '__main__':
    (players, options) = arguments.get_arguments()
    # The list of players for the game is made up of
    #   'Player' (your strategy)
    #   bots from get_arguments (the bots to use)
    player_list = players
    # **options -> interpret game options from get_arguments
    #              as a dictionary to unpack into the Game parameters
    game = Game(player_list, **options)
    game.play_game()
