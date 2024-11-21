# Ryan Eaton 2024-11-21

import re
import itertools

shop = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""

shop_vals = []

for line in shop.split("\n"):
    shop_vals.append(re.findall(r'\d+', line))

weapons = [x for x in shop_vals[1:6]]
armors = [x for x in shop_vals[8:13]]
rings = [x[1:] for x in shop_vals[15:21]]

def sim_game(health, damage, armorpts):
    players = [0, [health, damage, armorpts], [int(x) for x in re.findall(r'\d+', open('input21.txt', 'r').read())]]
    turn = 1
    while players[1][0] > 0 and players[2][0] > 0:
        players[-turn][0] -= max(players[turn][1] - players[-turn][2], 1)
        turn *= -1
    return players[1][0] > 0

max_cost = float('-inf')

for weapon in weapons:
    for armor in armors:
        for ringset in list(itertools.combinations(rings, 2)) + [tuple([x]) for x in rings]:
            cost = int(weapon[0]) + int(armor[0]) + sum([int(x[0]) for x in ringset])
            damage = int(weapon[1]) + int(armor[1]) + sum([int(x[1]) for x in ringset])
            armorpts = int(weapon[2]) + int(armor[2]) + sum([int(x[2]) for x in ringset])
            if not sim_game(100, damage, armorpts):
                max_cost = max(max_cost, cost)

print(max_cost)
