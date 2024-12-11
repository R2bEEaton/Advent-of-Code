from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=True, numbers=True)

scanners = {x: y for x, y in din}
scanners_conf = {x: x % (y * 2 - 2) for x, y in din}

ans = 0

for k, v in scanners_conf.items():
    if v == 0:
        ans += k * scanners[k]

aocd_submit(ans)