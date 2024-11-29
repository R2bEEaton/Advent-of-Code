from helpers.datagetter import aocd_data_in

din, aocd_submit = aocd_data_in(split=False, numbers=False)

tot = 0
for i in range(len(din)):
    if din[i] == din[(i + len(din) // 2) % len(din)]:
        tot += int(din[i])
aocd_submit(tot)