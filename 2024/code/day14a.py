from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)

for _ in range(100):
    for robot in din:
        robot[0] += robot[2]
        robot[1] += robot[3]

size = (101, 103)

q1, q2, q3, q4 = 0, 0, 0, 0

for robot in din:
    pos = (robot[0] % size[0], robot[1] % size[1])
    if pos[0] < size[0] // 2 and pos[1] < size[1] // 2:
        q1 += 1
    elif size[0] - (size[0] // 2) <= pos[0] and pos[1] < size[1] // 2:
        q2 += 1
    elif pos[0] < size[0] // 2 and size[1] - (size[1] // 2) <= pos[1]:
        q3 += 1
    elif size[0] - (size[0] // 2) <= pos[0] and size[1] - (size[1] // 2) <= pos[1]:
        q4 += 1

aocd_submit(q1 * q2 * q3 * q4)
