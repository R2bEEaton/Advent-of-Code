from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)

scanners = {x: y for x, y in din}

i = 0
while True:
    scanners_conf = {x: (i + x) % (y * 2 - 2) for x, y in din}
    if 0 not in scanners_conf.values():
        aocd_submit(i)
        break
    i += 1