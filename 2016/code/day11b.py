from helpers.datagetter import aocd_data_in
import functools
import itertools
import copy
import re

din, aocd_submit = aocd_data_in(split=True, numbers=False)

initial = [['eleriumG', 'eleriumM', 'dilithiumG', 'dilithiumM'], [], [], []]
floors = []

for i, line in enumerate(din):
    chips = re.findall(r'([a-z]+)-[a-z]+ .', line)
    generators = re.findall(r'([a-z]+) generator', line)
    floors.append(tuple(sorted([x + "M" for x in chips] + [x + "G" for x in generators] + initial[i])))

floors = tuple(floors)


equivalent_states = set()


def convert_state_to_general(state):
    general = []
    i = 0
    seen = []
    for floor in state:
        flr = []
        for item in floor:
            if item[:-1] not in seen:
                i = len(seen)
                seen.append(item[:-1])
            else:
                i = seen.index(item[:-1])
            flr.append(str(i) + item[-1])
        general.append(tuple(flr))
    return tuple(general)


@functools.cache
def valid(state):
    if convert_state_to_general(state) not in equivalent_states:
        equivalent_states.add(convert_state_to_general(state))
    else:
        return False
    good = True
    for floor in state:
        unmatched = [x for x in floor if x[-1] == "M" and x[:-1] + "G" not in floor]
        if unmatched and any([True for x in floor if x[-1] == "G"]):
            good = False
            break
    return good


def tuple_to_list(tpl):
    out = []
    for item in tpl:
        if isinstance(item, tuple):
            out.append(tuple_to_list(sorted(item)))
        else:
            out.append(item)
    return out


def list_to_tuple(tpl):
    out = []
    for item in tpl:
        if isinstance(item, list):
            out.append(list_to_tuple(sorted(item)))
        else:
            out.append(item)
    return tuple(out)


@functools.cache
def get_next_states(floor_num, state):
    combinations = list(itertools.combinations(list(state[floor_num]), 2)) + [[x] for x in list(state[floor_num])]
    next_states = []

    for group in combinations:
        if not group:
            continue
        updown = []
        if floor_num + 1 <= 3:
            updown.append(1)
        if floor_num - 1 >= 0:
            updown.append(-1)
        for i in updown:
            state_copy = tuple_to_list(copy.deepcopy(state))
            for item in group:
                state_copy[floor_num].remove(item)
                state_copy[floor_num+i].append(item)
            state_copy = list_to_tuple(state_copy)
            if valid(state_copy):
                next_states.append((floor_num+i, state_copy))

    return next_states


states_to_search = set()
states_to_search.add((0, floors))

steps = 0
while states_to_search:
    print(steps, len(states_to_search))
    new_states_to_search = set()
    for state in states_to_search:
        if not state[1][0] and not state[1][1] and not state[1][2]:
            aocd_submit(steps)
            exit()
        new_states_to_search.update(get_next_states(*state))
    states_to_search = new_states_to_search
    steps += 1
