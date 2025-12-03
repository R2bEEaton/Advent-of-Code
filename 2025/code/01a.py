from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=False)

dial = 50
counter = 0

for line in din:
    if line.startswith("L"):
        dial -= int(line[1:])
        dial %= 100
    elif line.startswith("R"):
        dial += int(line[1:])
        dial %= 100

    if dial == 0:
        counter += 1

aocd_submit(counter)