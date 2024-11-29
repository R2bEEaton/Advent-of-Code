from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)

tot = 0
for line in din:
    tot += max(line) - min(line)

aocd_submit(tot)