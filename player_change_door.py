import random
from monty_hall import MontyHall

class PlayerChange:

    def __init__(self):
        self.score = 0

    def play(self, game: MontyHall):
        chosen_door = random.choice(game.doors)
        loser_door = game.turn1(chosen_door)
        other_doors = [door for door in game.doors if door != chosen_door and door != loser_door]
        self.score += game.turn2(random.choice(other_doors))