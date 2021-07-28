
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


class PlayerNotChange:

    def __init__(self):
        self.score = 0
    
    def play(self, game: MontyHall):
        chosen_door = random.choice(game.doors)
        game.turn1(chosen_door)
        self.score += game.turn2(chosen_door)


class PlayerChange:

    def __init__(self):
        self.score = 0

    def play(self, game: MontyHall):
        chosen_door = random.choice(game.doors)
        loser_door = game.turn1(chosen_door)
        other_doors = [door for door in game.doors if door != chosen_door and door != loser_door]
        self.score += game.turn2(random.choice(other_doors))


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
