from helpers.datagetter import aocd_data_in
from functools import cache

din, aocd_submit = aocd_data_in(split=False, numbers=True)
din = din[0]

stones = din
ans = 0

@cache
def get_nums(stone, depth):
    if depth == 0:
        return 1

    new_stones = []
    tot = 0
    stone_str = str(stone)
    if stone == 0:
        new_stones.append(1)
    elif len(stone_str) % 2 == 0:
        new_stones.append(int(stone_str[:len(stone_str) // 2]))
        new_stones.append(int(stone_str[len(stone_str) // 2:]))
    else:
        new_stones.append(stone * 2024)
    
    for new_stone in new_stones:
        tot += get_nums(new_stone, depth-1)
    return tot
    

for num in stones:
    ans += get_nums(num, 75)

aocd_submit(ans)