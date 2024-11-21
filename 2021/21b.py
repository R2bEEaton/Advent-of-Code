with open("input21.txt") as f:
    lines = f.readlines()
    a_start = int(lines[0].split(" ")[-1].strip())
    b_start = int(lines[1].split(" ")[-1].strip())

from collections import Counter
import time

rolls = []
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            rolls.append(sum([a, b, c]))

class Game:
    def __init__(self, turn, score, pos):
        self.turn = turn
        self.score = score
        self.pos = pos

    def __str__(self):
        return f"{self.turn} {self.score} {self.pos}"

    def __eq__(self, other):
        return all([self.turn == other.turn, self.score == other.score, self.pos == other.pos])

    def __hash__(self):
        return hash(str(self))

    def convolve(self):
        out = []

        for roll in rolls:
            if self.turn == 1:
                new_score = (self.score[0] + (self.pos[0] + roll) % 10 + 1, self.score[1])
                new_pos = ((self.pos[0] + roll) % 10, self.pos[1])
            else:
                new_score = (self.score[0], self.score[1] + (self.pos[1] + roll) % 10 + 1)
                new_pos = (self.pos[0], (self.pos[1] + roll) % 10)
            out.append(Game(2 if self.turn == 1 else 1, new_score, new_pos))

        return out

games = {Game(1, (0, 0), (a_start - 1, b_start - 1)): 1}
wins = [0, 0]

start = time.time()
while games:
    new_games = {}
    for game, count in games.items():
        convolves = game.convolve()
        unique = Counter(convolves)
        for new_game, game_count in unique.items():
            if max(new_game.score) >= 21:
                wins[new_game.turn - 2] += game_count * count
            else:
                if new_game in new_games:
                    new_games[new_game] += game_count * count
                else:
                    new_games[new_game] = game_count * count
    games = new_games

print(wins)
print(time.time() - start)