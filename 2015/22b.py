# Ryan Eaton 2024-11-21 Oh it's so ugly

import functools

def purchase_effect(player, idx, amt, dur):
    player_copy = player.copy()
    player_copy[1] -= amt
    player_copy[3+idx] = dur
    player_copy[6] += amt
    return tuple(player_copy)


@functools.cache
def gen_next_states(player, boss, player_turn):
    player = list(player)
    player[0] -= 1

    if player[0] <= 0 or boss[0] <= 0:
        return [player[0] <= 0, boss[0] <= 0, player[6]]

    next_states = []

    boss = list(boss)

    player[2] = 7 if player[3+0] > 0 else 0 # Shield
    if player[3+1] > 0: # Poison
        boss[0] -= 3
    if player[3+2] > 0: # Recharge
        player[1] += 101

    player[3+0] -= 1 if player[3+0] > 0 else 0
    player[3+1] -= 1 if player[3+1] > 0 else 0
    player[3+2] -= 1 if player[3+2] > 0 else 0

    if player_turn:
        if player[3+0] == 0 and player[1] >= 113:
            next_states.append((purchase_effect(player, 0, 113, 6), tuple(boss), not player_turn))
        if player[3+1] == 0 and player[1] >= 173:
            next_states.append((purchase_effect(player, 1, 173, 6), tuple(boss), not player_turn))
        if player[3+2] == 0 and player[1] >= 229:
            next_states.append((purchase_effect(player, 2, 229, 5), tuple(boss), not player_turn))
        if player[1] >= 53:
            next_states.append(((player[0], player[1] - 53, *player[2:6], player[6] + 53), (boss[0] - 4, boss[1]), not player_turn))
        if player[1] >= 73:
            next_states.append(((player[0] + 2, player[1] - 73, *player[2:6], player[6] + 73), (boss[0] - 2, boss[1]), not player_turn))
        
    else:
        player[0] -= max(boss[1] - player[2], 1) # Boss damage player
        next_states.append((tuple(player), tuple(boss), not player_turn))

    return next_states

# Health, mana, shield, Shield, Poison, Recharge, Spent
player = (50, 500, 0, 0, 0, 0, 0)

# Health, damage
boss = (58, 9)

states = [[player, boss, True]]
min_mana = float('inf')

while states:
    won = False
    new_states = []
    for state in states:
        #print(state)
        next_states_for_this_state = gen_next_states(*state)
        if len(next_states_for_this_state) and isinstance(next_states_for_this_state[0], bool):
            if next_states_for_this_state[1]:
                if next_states_for_this_state[2] < min_mana:
                    min_mana = next_states_for_this_state[2]
                    print("Player won with ", next_states_for_this_state[2])
                    won = True
        else:
            new_states.extend(next_states_for_this_state)
    #print(new_states)
    states = new_states
    if won:
        break
    