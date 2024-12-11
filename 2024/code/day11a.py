from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=True)
din = din[0]

stones = din

for _ in range(25):
    new_stones = []
    for stone in stones:
        stone_str = str(stone)
        if stone == 0:
            new_stones.append(1)
        elif len(stone_str) % 2 == 0:
            new_stones.append(int(stone_str[:len(stone_str) // 2]))
            new_stones.append(int(stone_str[len(stone_str) // 2:]))
        else:
            new_stones.append(stone * 2024)
    stones = new_stones
    
aocd_submit(len(new_stones))