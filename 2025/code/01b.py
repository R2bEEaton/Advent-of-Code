from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)

dial = 50
counter = 0

for line in din:
    direction = 0
    if line.startswith("L"):
        direction = -1
    elif line.startswith("R"):
        direction = 1

    for _ in range(int(line[1:])):
        dial += direction
        dial %= 100

        if dial == 0:
            counter += 1

aocd_submit(counter)