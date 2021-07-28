import argparse

from monty_hall import MontyHall
from player_sticks_choice import PlayerSticksWithChoice
from player_change_door import PlayerChange


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--doors', help='Number of doors', default=3)
parser.add_argument('-e', '--experiments', help='Number of experiments', default=1000)
args = parser.parse_args()

doors = int(args.doors)
experiments = int(args.experiments)

print(f'Game Setup with a total of {doors} doors with reward behind exactly 1 door')
print(f'Running {experiments} experiments in total')

player_sticks = PlayerSticksWithChoice()
player_changes = PlayerChange()

for expt in range(experiments):
    game = MontyHall()

    player_sticks.play(game)
    player_changes.play(game)

print(f'Player that sticks won {player_sticks.score} games out of {experiments} total games, equalling probability of {player_sticks.score / experiments}.')
print(f'Player that changes won {player_changes.score} games out of {experiments} total games, equalling probability of {player_changes.score / experiments}.')