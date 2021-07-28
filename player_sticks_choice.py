import random
from monty_hall import MontyHall

class PlayerSticksWithChoice:

    def __init__(self):
        self.score = 0
    
    def play(self, game: MontyHall):
        chosen_door = random.choice(game.doors)
        game.turn1(chosen_door)
        self.score += game.turn2(chosen_door)