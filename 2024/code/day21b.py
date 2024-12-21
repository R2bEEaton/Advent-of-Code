from helpers.datagetter import aocd_data_in
from helpers.matrix import from_grid
from functools import cache
import re

din, aocd_submit = aocd_data_in(split=True, numbers=False)

numeric = from_grid('789\n456\n123\n 0A')
directional = from_grid(' ^A\n<v>')


def score_path(path):
    dir_changes = 0
    for i in range(len(path) - 2):
        dir_changes += path[i] != path[i+1]
    dir_changes *= 10
    if len(path) >= 2:
       dir_changes += (3 if path[-2] in "<" else 0) + (2 if path[-2] in "v" else 0) + (1 if path[-2] in "^>" else 0)
    return dir_changes


def shortest_path(nspos, ngpos, out_grid):
    q = [[nspos]]
    paths = []

    while q:
        path = q.pop(0)
        curr = path[-1]

        if curr == ngpos:
            paths.append(path)
            continue

        for nei, val in out_grid.neighbors(curr):
            if val in [None, ' '] or nei in path:
                continue
            q.append(path + [nei])

    path_dirss = []
    for path in paths:
        path_dirs = []
        for i in range(len(path) - 1):
            diff = tuple(path[i + 1][j] - path[i][j] for j in range(2))
            if diff == (0, -1):
                path_dirs.append("<")
            elif diff == (0, 1):
                path_dirs.append(">")
            elif diff == (-1, 0):
                path_dirs.append("^")
            elif diff == (1, 0):
                path_dirs.append("v")
        path_dirs.append("A")
        path_dirss.append(path_dirs)

    min_path = min([len(path) for path in path_dirss])
    path_dirss = filter(lambda x: len(x) == min_path, path_dirss)
    path_dirs = sorted(path_dirss, key = lambda x: score_path(x))[0]
    return path_dirs


shortest_paths_dir_to_num = {}
shortest_paths_dir_to_dir = {}

for nspos, nsval in numeric:
    if nsval == ' ':
        continue
    for ngpos, ngval in numeric:
        if ngval == ' ':
            continue
        shortest_paths_dir_to_num[(nspos, ngpos)] = shortest_path(nspos, ngpos, numeric)

for nspos, nsval in directional:
    if nsval == ' ':
        continue
    for ngpos, ngval in directional:
        if ngval == ' ':
            continue
        shortest_paths_dir_to_dir[(nspos, ngpos)] = shortest_path(nspos, ngpos, directional)


num_directional_pads = 26
prevs = [numeric.findall('A')[0]] + [directional.findall('A')[0] for _ in range(num_directional_pads)]


@cache
def get_presses(i, string):
    global prevs

    tot = 0
    if i == num_directional_pads + 1:
        return 1

    for char in string:
        curr = numeric.findall(char)[0] if i == 0 else directional.findall(char)[0]
        path1 = shortest_paths_dir_to_num[prevs[i], curr] if i == 0 else shortest_paths_dir_to_dir[prevs[i], curr]
        tot += get_presses(i + 1, tuple(path1))
        prevs[i] = curr

    return tot


ans = 0
for line in din:
    tot_path = get_presses(0, line)
    print(tot_path, int(re.findall(r'\d+', line)[0]))
    ans += tot_path * int(re.findall(r'\d+', line)[0])

aocd_submit(ans)