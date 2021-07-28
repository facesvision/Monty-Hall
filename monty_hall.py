
import random


class MontyHall:

    def __init__(self):
        self.doors = [1, 2, 3, 4]
        self.winner_door = random.choice(self.doors)

    def turn1(self, chosen_door):
        if chosen_door == self.winner_door:
            other_doors = [door for door in self.doors if door != chosen_door]
            return random.choice(other_doors)
        else:
            other_doors = [door for door in self.doors if door != chosen_door and door != self.winner_door]
            return random.choice(other_doors)

    def turn2(self, chosen_door):
        return 1 if chosen_door == self.winner_door else 0





if __name__ == '__main__':
    NUM_EXPTS = 100000

    player_not_change = PlayerNotChange()
    player_change = PlayerChange()

    for expt in range(NUM_EXPTS):
        game = MontyHall()

        player_not_change.play(game)
        player_change.play(game)

    print(f'Player not change: {player_not_change.score / NUM_EXPTS}')
    print(f'Player change: {player_change.score / NUM_EXPTS}')
